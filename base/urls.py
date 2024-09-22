from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('<slug:category_slug>/<slug:product_slug>', views.ProductDetailView.as_view(), name='product_details'),
    path('products/',views.ProductsListView.as_view(),name='products'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('about/',views.ProductsListView.as_view(),name='about'),
    path('add_cart/<slug:product_slug>/',views.AddCartView.as_view(),name="add_cart"),
    path('cart/',views.CartView.as_view(),name="cart"),
    path('update_quantity/', views.UpdateQuantityView.as_view(), name='update_quantity'),
     path('delete_cart/<slug:product_slug>/', views.DeleteCartView.as_view(), name='delete_cart'),

    
]
