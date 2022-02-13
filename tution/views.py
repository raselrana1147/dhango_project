from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import ListView

from django.shortcuts import render,HttpResponse
from .models import Contact
from .forms import ContactForm,PostForm
from .models import Post,Subject,Class_in


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
class PostListView(ListView):
    template_name='postlist.html'
    queryset=Post.objects.filter(user=2)
    context_object_name="posts"

def view_post(request):
    post=Post.objects.all();
    contex={
        'post':post
    }

    return render(request,'post.html',contex)
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
    
