from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class UserProfile(models.Model):
    GENRE_CHOICES=(
        ('Male','Male'),
        ('Female','Female'),
    )
    CATEGORY=(
        ('Teacher','Teacher'),
        ('Student','Student')
    )
    BLOOD_GROUP=(
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),
    )
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date=models.DateField()
    blood_group=models.CharField(max_length=3,choices=BLOOD_GROUP)
    gender=models.CharField(max_length=6,choices=GENRE_CHOICES)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=15)
    nationality=models.CharField(max_length=100)
    religion=models.CharField(max_length=50)
    biodata=models.TextField()
    profession=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg',upload_to='session/images')
    def __str__(self):
        f'{self.user.username} Profile'
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
        
    
    
    
    
