from django.db.models import Sum
from .models import CartItem

def counter(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    return {'cart_count': cart_count}
