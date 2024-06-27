from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#Abstract user insted of user in case of variable users
class CustomUser(AbstractUser):
    userType=models.CharField(max_length=50)
    viewpassword=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.username

class Userregistration(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dob=models.DateTimeField()
    regdate=models.DateField(auto_now_add=True)
    uname=models.CharField(max_length=50,null=True)
    img=models.ImageField(upload_to="profile",null=True)
    def __str__(self):
        return self.name
class Counsilerregistration(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    desig=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dob=models.DateTimeField()
    regdate=models.DateField(auto_now_add=True)

    uname=models.CharField(max_length=50,null=True)
    img=models.ImageField(upload_to="profile",null=True)
    aboutme=models.CharField(max_length=1000,null=True)
    video=models.ImageField(upload_to="video",null=True)
    def __str__(self):
        return self.name
class Requestuser(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    requests=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    gender=models.CharField(max_length=100)
    def __str__(self):
        return self.requests
class Question(models.Model):
    
    question=models.CharField(max_length=100)
    answer1=models.CharField(max_length=100)
    answer2=models.CharField(max_length=100)
    answer3=models.CharField(max_length=100)
    answer4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    
    def __str__(self):
        return self.question
class Message(models.Model):
    frm=models.CharField(max_length=100)
    to=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    filetype=models.CharField(max_length=100)
    file=models.CharField(max_length=300)
    date=models.DateField(auto_now_add=True)
class Answeruser(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
class Booking(models.Model):
    councelr=models.ForeignKey(Counsilerregistration,on_delete=models.CASCADE)
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    request=models.CharField(max_length=100,default="")
    typ=models.CharField(max_length=100,default="")
    bookingdate=models.CharField(max_length=100)
    dateofbook=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100)
class Authmessage(models.Model):
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    messages=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    video=models.ImageField(upload_to="video",null=True)
    status=models.CharField(max_length=100)
class Mytab(models.Model):
    name=models.CharField(max_length=50)
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
class feedback(models.Model):
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    feedbackss=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
class payment(models.Model):
    usr=models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    con=models.ForeignKey(Counsilerregistration,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    