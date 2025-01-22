from django.shortcuts import render ,redirect
from django.core.exceptions import ValidationError
from .models import register ,Login
from django.contrib import messages




def user_register(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Location = request.POST.get('Location')

        try:
        
            if register.objects.filter(Name=Name).first():
                messages.error(request, "Username already exists")
                return redirect("/register")

            
            if register.objects.filter(Email=Email).first():
                messages.error(request, "Email is already registered")
                return redirect("/register")

        
            new_user = register(Name=Name, Email=Email, Address=Address, Location=Location)
            
            
            new_user.save()  
            return redirect("/home/")  
            
        except Exception as e:
            print(e)  
            messages.error(request, "Something went wrong. Please try again.")
            return redirect("/register")  


    return render(request, 'app/register.html', {
        'Username': request.POST.get('Username'),
        'PhoneNumber': request.POST.get('PhoneNumber'),
        'email': request.POST.get('email')
    })

def user_login(request):
    if request.method == 'POST':
        Code = request.POST.get('Code')

        try:
            user = register.objects.get(Code=Code) 
            if Code(Code, user.Code): 
                messages.success(request, "Code Submit successful!")
                return redirect('home')  
            else:
                messages.error(request, "Incorrect Code")
        except register.DoesNotExist:
            messages.error(request, "Code does not exist")

    return render(request, 'app/login.html')




def home(request):
    return render(request, 'app/home.html')
            
           