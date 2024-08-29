from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)


    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Category, self).save(*args,**kwargs)
        
    def get_product_count(self):
        return Product.objects.filter(category=self).count()

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
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
        return reverse("product_details",args=[self.category.slug, self.slug])
    
    #to get the tags supperated by comma
    @property
    def get_tags_list(self):
        return self.tags.split(",") if self.tags else []

    
    #to generate auto slug when adding the products
    def save(self,*args,**kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Product, self).save(*args,**kwargs)


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