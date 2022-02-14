from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Contact, Post

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
        #     'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone number'})
        # }
        
        # labels={
        #     'name':'Enter your name',
        #     'phone':'Enter your phone number',
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].initial="My Name"
        self.fields['phone'].initial="My phone"
    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_of_w=value.split(' ')
        if len(num_of_w) > 10:
            self.add_error('name',"Your name should be less than 3 character")
        else:
            value
        
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','id','slug','created_at',]
        widgets={
			'class_in':forms.CheckboxSelectMultiple(attrs={
				'multiple':True
			}),
			'subject':forms.CheckboxSelectMultiple(attrs={
				'multiple':True
			})
		}
        
        
