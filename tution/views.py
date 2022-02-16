from http.client import HTTPResponse
from operator import mod
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib import messages

from django.shortcuts import render,HttpResponse
from .models import Contact
from .forms import ContactForm,PostForm
from .models import Post,Subject,Class_in
from django.db.models import Q


class PostDetailView(DetailView):
    model=Post;
    template_name='post_detail.html'
    
def contact(request):
    initials={
        'name':'My Name is Rasel',
        'phone':'My Phoner number is 01254555555'
    }
    if request.method=="POST":
        form=ContactForm(request.POST,initial=initials)
        if form.is_valid():
            messages.success(request,"Form successfully submitted")
            form.save()
    else:
        form=ContactForm(initial=initials)
    return render(request,'contact.html',{'form':form})
    
class ContactView(View):
    class_form=ContactForm
    class_view='contact.html'
    
    # success_url='/'
    # def form_valid(self,form):
    #     form.save()
    #     return super().form_valid(form)
    # def form_invalid(self,form):
    #     print("invalid form")
    #     return super().form_invalid(form)

    
    def get(self, request,*args, **kwargs):
        form=self.class_form()
        return render(request,self.class_view,{'form':form})
    def post(self,request, *args, **kwargs):
        form=self.class_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request,self.class_view,{'form':form})
      
# def home_page(request):
#           return HttpResponse(request,"Okay")

# def home_page(request):
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             # name=form.cleaned_data['name']
#             # phone=form.cleaned_data['phone']
#             # contact=Contact(name=name,phone=phone);
#             # contact.save();
#             form.save()
#     else:
#         form=ContactForm()
        
#     return render(request,'home.html',{'form':form})
class postDeleteView(DeleteView):
    model=Post;
    template_name="delete.html"
    success_url=reverse_lazy('tution:postlist')
    
class PostListView(ListView):
    template_name='postlist.html'
    queryset=Post.objects.all()
    context_object_name="posts"

def view_post(request):
    post=Post.objects.all();
    contex={
        'post':post
    }

    return render(request,'post.html',contex)
class PostEditView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='updatepost.html'
    def get_success_url(self):
        id=self.object.id
        return reverse_lazy('tution:postdetail',kwargs={'pk':id})
    
class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    template_name="create_post.html"
    success_url='/'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)



def postcreate(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            sub=form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HTTPResponse("Success")
    else:
        form=PostForm()
        return render(request,'create_post.html',{'form':form})
def subview(request):
    subject=Subject.objects.get(name='Chemistry')
    post=subject.subject_set.all()
    context={
        'subject':subject,
        'post':post
    }
    
    return render(request,'subject.html',context)
def searchitem(request):
    query=request.POST.get('search','')
    if query:
        queryset=(Q(title__incontains= query)) | (Q
                (category__incontains= query)) | (Q
                (medium__incontains= query)) | (Q
                (class_in__name__incontains= query)) | (Q
                (detail__incontains= query))
        results=Post.objects.filter(queryset).distinct()
    else:
        results=[]
    context={
        'results':results
    }
    return render(request,'search.html',context)
    
