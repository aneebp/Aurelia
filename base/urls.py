from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('product-details',views.ProductDetails.as_view(),name='produt_details')
]
