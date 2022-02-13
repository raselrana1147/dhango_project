from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=191)
    phone=models.CharField(max_length=191)

class Post(models.Model):
	CATEGORY=(
			('Teacher','Teacher'),
			('Student','Student'),
		)
	id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=191)
	slug=models.CharField(max_length=191,default=title)
	email=models.EmailField()
	salary=models.FloatField()
	detail=models.TextField()
	image=models.ImageField(upload_to="media/tution/image",default='default.jpg')
	available=models.BooleanField()
	category=models.CharField(max_length=191,choices=CATEGORY)
	created_at=models.DateTimeField(default=now)

	def save(self,*args,**kwargs):
		self.title=slugify(self.title)
		super(Post,self).save(*args,**kwargs)
		img=Image.open(self.image.path)
		if img.height > 300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

 