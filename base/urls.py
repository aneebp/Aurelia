from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_details'),
    
]
