from django.views import View
from django.shortcuts import render
from .models import *
from .form import RegistrationForm

class HomeView(View):
    def get(self, request):
        products = Product.objects.all()[:8]
        context = {"products":products}
        return render(request, 'base/home.html', context)

    # def post(self, request):
    #    pass

class LoginView(View):
    def get(self, request):
        return render(request, 'base/login.html')
    

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {"form":form}
        return render(request, 'base/register.html',context)



class ProductDetailView(View):
    def get(self, request,category_slug,product_slug):
        products = Product.objects.all()[:8]
        product = Product.objects.get(slug=product_slug)
        
        context = {"product":product,"products":products}
        return render(request, 'base/product_details.html',context)