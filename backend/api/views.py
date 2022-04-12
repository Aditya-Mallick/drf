import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializers


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    # DRF API View
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializers(instance).data
    return Response(data)
