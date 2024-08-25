from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True)
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    tags = models.CharField(max_length=200)
    deals = (("New","New"),("Trending","Trending"))
    status = models.CharField(max_length=100,choices=deals, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reversed("product_details",args=[self.category.slug, self.slug])

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    #to access the totalamount like an attribute rather than a method
    @property
    def get_total_amount(self):
        return self.Product.price * self.quantity
    
    def __str__(self):
        return  f"{self.Product.title} (Quantity: {self.quantity})"
    

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(max_length=400)
    country = models.CharField(100)
    city = models.CharField(100)
    pin = models.IntegerField()
    phone = models.IntegerField()
    quantity= models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.country} {self.pin}"
    
    def get_total_amount(self):
        price = self.product.price * self.quantity
        total_price = price + 10 
        return total_price