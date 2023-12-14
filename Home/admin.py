from django.contrib import admin
from .models import Message,ApplicationForm,UserProfile,User
# Register your models here.
admin.site.register(Message)
admin.site.register(UserProfile)
admin.site.register(ApplicationForm)
admin.site.register(User)