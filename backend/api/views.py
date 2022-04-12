import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from product.models import Product


def api_home(request, *args, **kwargs):
    # model_data = Product.objects.all().order_by("?").first()
    print(request.GET['abc'])
    model_data = Product.objects.filter(id=request.GET['abc']).first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
