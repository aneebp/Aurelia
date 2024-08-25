from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'base/home.html', context)

    # def post(self, request):
    #    pass


class ProductDetails(View):
    def get(self, request):
        context = {}
        return render(request, 'base/product_details.html',context)