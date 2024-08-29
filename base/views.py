from django.views import View
from django.shortcuts import render,redirect
from .models import *
from .form import RegistrationForm
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'base/login.html')
    


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

            try:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.phone_number = phone_number
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'An error occurred during registration: {str(e)}')
        else:
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