from django.shortcuts import render
from .models import Product

def product_detail_view(request):
    obj = Product.objects.get(id=2)
    """
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    """

    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)