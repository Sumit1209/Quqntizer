from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=225)
    phone=models.CharField(max_length=15)
    discription=models.TextField()
    
    def __str__(self):
        return self.email
    
class Home1(models.Model):
    heading=models.CharField(max_length=80)
    subheading=models.CharField(max_length=150)

    def __str__(self):
        return (self.heading)
    
class Product(models.Model):
    label=models.CharField(max_length=150)
    rating=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    pic1=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic2=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic3=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic4=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic5=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic6=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    Text=HTMLField()
    

    

    def __str__(self):
        return self.label
    
class Product2(models.Model):
    label=models.CharField(max_length=150)
    rating=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    pic1=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic2=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic3=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic4=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic5=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic6=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    Text=HTMLField()
    

    def __str__(self):
        return self.label
    
class Product3(models.Model):
    label=models.CharField(max_length=150)
    rating=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    pic1=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic2=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic3=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic4=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic5=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    pic6=models.FileField(upload_to="Home/",max_length=1000,null=True,default=None)
    Text3=HTMLField()
    

    def __str__(self):
        return self.label
