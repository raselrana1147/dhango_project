from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=191)
    phone=models.CharField(max_length=191)

class Subject(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
    		return self.name
	
    
class Class_in(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
    		return self.name
	
    
class Post(models.Model):
	CATEGORY=(
			('Teacher','Teacher'),
			('Student','Student'),
		)
	MEDIUM=(
		('Bangla','bangla'),
        ('English','English'),
        ('Urdu','Urdu'),
        ('Arabic','Arabic'),
        ('Hindi','Hindi'),
	)
	user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=191)
	slug=models.CharField(max_length=191,default=title)
	email=models.EmailField()
	salary=models.FloatField()
	detail=models.TextField()
	image=models.ImageField(upload_to="media/tution/image",default='default.jpg')
	available=models.BooleanField()
	category=models.CharField(max_length=191,choices=CATEGORY)
	medium=MultiSelectField(max_length=100,max_choices=4,choices=MEDIUM,default='bangla')
	subject=models.ManyToManyField(Subject, related_name='subject_set')
	class_in=models.ManyToManyField(Class_in,related_name='class_set')
	created_at=models.DateTimeField(default=now)
 

	def save(self,*args,**kwargs):
		self.title=slugify(self.title)
		super(Post,self).save(*args,**kwargs)
		img=Image.open(self.image.path)
		if img.height > 300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
	def __str__(self):
    		return self.title
	
   
   

