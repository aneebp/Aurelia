from django.views import View
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .form import RegistrationForm
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#email verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()[:8]
        context = {"products":products}
        return render(request, 'base/home.html', context)

    # def post(self, request):
    #    pass


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'base/login.html')

    def post(self, request):
        username = request.POST.get("username") 
        password = request.POST.get("password")
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid login info")
        else:
            messages.error(request, "Username and password are required")
        
        return render(request, 'base/login.html')

        
class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('login')
        


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'base/register.html', {'form': form})

    def post(self, request):    
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password1"]

            
            user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    
                )
            user.set_password(password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, "Successfully Registered")
            return redirect('login')
    
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field.capitalize()}: {error}")
        
        return render(request, 'base/register.html', {'form': form})


class ProductDetailView(View):
    def get(self, request,category_slug,product_slug):
        products = Product.objects.all()[:8]
        product = Product.objects.get(slug=product_slug)
        
        context = {"product":product,"products":products}
        return render(request, 'base/product_details.html',context)