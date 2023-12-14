from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser , User
# Create your models here.
class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
 




class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message= models.TextField()

    def __str__(self) -> str:
        return self.email + "  " + self.subject


class ApplicationForm(models.Model):
    
    user = models.ForeignKey(UserProfile, related_name="copyprofile", blank=True, default=True ,null = True,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Father_Name = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Mobile_No = models.CharField(max_length=12)
    Postal_code = models.IntegerField()
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.TextField()

    def __str__(self) -> str:
        return self.Name

def  post_user_created_signal(sender, instance, created, **kwargs):
    #print(instance,created)
    if created:
        UserProfile.objects.create(user=instance)
        #form.save(commit=False)

post_save.connect(post_user_created_signal,sender=User)
