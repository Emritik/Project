from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

class SignupView(generic.CreateView):
    template_name = "core/signup.html"
    form_class = CustomUserCreationForm
    
    #email = self.request.POST['email']

    #send_mail("SignUp", "You are successfully Creating a new account \n  We are appricating your step toward the make Digital India by usnig the application of our portal \n Thanks for Support \n Team STET", email, ['STETinfoexam@gmail.com'],fail_silently = False)


    def get_success_url(self):
        return (reverse("login"))


"""def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or Password is incorrect")
            return render(request,'core/login.html')
        
        return render(request,'core/login.html')
   
    elif request.method=='GET':
        return render(request,'core/login.html')"""
 
#@login_required(login_url='/login/')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
       # print(message)
        from_email = settings.EMAIL_HOST_USER
        to_email = email
        Message.objects.create(name = name , email = email, subject = subject, message = message)
        # send mail to admin
        send_mail("Feedback", "Thanks for providing the feedbacks.\n I hope you like your services and if you have any other feedback than please provide to us so, your team try to resolve this problem imedatelly.\nYou are successfully Creating a new account \n  We are appricating your step toward the make Digital India by usnig the application of our portal \n Thanks for Support \n Team STET",
         from_email, [to_email],fail_silently = False)
        return render(request,'core/contact.html')
    elif request.method == 'GET':
        return render(request,'core/contact.html') 
    return render(request,'core/contact.html')  

@login_required(login_url='/login/')
def application(request):
    if request.method=="POST":
        user = request.user.userprofile
        print(user)
        name = request.POST['name']
        email = request.POST['email']
        father_name = request.POST['fname']
        mother_name = request.POST['mname']
        mobile_no = request.POST['phone']
        qualification = request.POST['Qualification']
        dob = request.POST['DOB']
        code = request.POST['code']
        address = request.POST['Address']
        from_email = settings.EMAIL_HOST_USER
        ApplicationForm.objects.create(user = user,Name=name,Father_Name=father_name,Mother_Name=mother_name,Email = email
                                        ,Mobile_No=mobile_no,Qualification= qualification,DOB=dob,
                                        Postal_code= code,Address=address
                                        )
        send_mail("Application form", "You are successfully Submit the application From. ", from_email, [email],fail_silently = False)

        messages.info(request,"Applied Successfully")
        return redirect("/application/")
    else:
        messages.warning(request,"Please fill all fields correctly")
            
    messages.error(request,"Failed to apply")
    context={}
    return render(request,'core/application.html',context)
@login_required(login_url='/login/')
def userprofile(request):
    userprofile = request.user.userprofile
    #print(userprofile)
    data = ApplicationForm.objects.filter(id=userprofile.id)
    #print(data)
    context = {'detail':data}
    return render(request, 'core/userprofile.html',context)
