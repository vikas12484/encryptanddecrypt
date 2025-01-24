from django.shortcuts import render ,redirect
from django.core.exceptions import ValidationError
from .models import register ,Login
from django.contrib import messages
import random
import string
import qrcode
from io import BytesIO
from PIL import Image
import base64




def generate_code():
    """Generate a random 6-digit code."""
    return ''.join(random.choices(string.digits, k=6))

def user_register(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        Location = request.POST.get('Location')

        errors = {}
        if register.objects.filter(Name=Name).first():
            errors['Name'] = "Username already exists"
        if register.objects.filter(Email=Email).first():
            errors['Email'] = "Email is already registered"

        # If no errors, proceed with registration
        if not errors:
            try:
                new_user = register(Name=Name, Email=Email, Address=Address, Location=Location)
                new_user.Code = generate_code()  # Generate and save the code
                new_user.save()

                # Generate QR code for the user's code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4
                )
                qr.add_data(new_user.Code)  # The user's unique code
                qr.make(fit=True)
                img = qr.make_image(fill="black", back_color="white")
                
                # Convert image to BytesIO and then to base64
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                qr_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

                # Success message and redirect to the page showing the QR code
                return render(request, 'app/qr.html', {'qr_image': qr_image_base64, 'code': new_user.Code})

            except Exception as e:
                messages.error(request, "Something went wrong. Please try again.")
                return redirect("/register")
        else:
            # Pass errors to the template if any
            return render(request, 'app/register.html', {'errors': errors, 'Name': Name, 'Email': Email, 'Address': Address, 'Location': Location})

    return render(request, 'app/register.html')

def user_login(request):
    if request.method == 'POST':
        Code = request.POST.get('Code')

        try:
            # Get the user based on the Code
            user = register.objects.get(Code=Code)

            # Login successful message
            messages.success(request, "Login successful! Welcome back.")
            return render(request, 'app/login.html', {'user': user})

        except register.DoesNotExist:
            messages.error(request, "Incorrect code. Please try again.")
            return redirect("/login")

    return render(request, 'app/login.html')
def home(request):
    if request.user.is_authenticated:  # If the user is logged in
        try:
            
            user = register.objects.get(Email=request.user.email)
            code = user.Code  # Get the user's code
        except register.DoesNotExist:
            code = None
    else:
        code = None

    return render(request, 'app/home.html', {'code': code})    

           