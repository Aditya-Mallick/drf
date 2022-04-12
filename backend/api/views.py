import json
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from yaml import serialize

from product.models import Product
from product.serializers import ProductSerializers


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "Not good data"})
