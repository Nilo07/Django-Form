from imaplib import _Authenticator
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
#from online import settings
#from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, "online/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        address = request.POST['address']
        pincode = request.POST['pincode']


        INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]
        date_of_birth = forms.IntegerField(label="Enter your date of birth: ", widget=forms.Select(choices=INTEGER_CHOICES))

        date_of_birth = request.POST['date_of_birth']
        blood_group = request.POST['blood-group']
        gender = request.POST['gender']
        district = request.POST['district']





        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(phoneno) != 10:
            messages.error(request, "Phone No doesn't exist")
            return redirect('signin')
        
        if pass1 != pass2:
            messages.error(request, "Password Didn't match!")
            return redirect('signin')
        
        if len(pincode) != 6:
            messages.error(request, "Pincode doesn't exist")
            return redirect('signin')

        
        





        

        myuser = User.objects.create_user(username, phoneno, pass1)
        myuser.first_name = fname


        myuser.save()

        messages.success(request, "You have successfully registered.")


        #Welcome Mail

        #subject = "Welcome to Online - DJango Login."
        #message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Online!! \n Thank You for registering. \n We have also sent you a confirmationemail, please confirm your email address in order to activate your account \n\n Thanking You\n Ashish Debnath"
        #from_email = settings.EMAIL_HOST_USER
        #to_user = [myuser.email]
        #send_mail(subject, message, from_email, to_user, fail_silently=True)
        
        return redirect('signin')






    return render(request, "online/registration.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']


        user = authenticate(username = username, password = pass1)


        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "online/index.html", {'fname': fname})

        else:
            messages.error(request,"Incorrect Credentials!")
            return redirect('home')




    return render(request, "online/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

