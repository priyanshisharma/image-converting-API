from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ImageConversionSerializer

# Create your views here.

@api_view(['POST'])
def image_conversion(request):

    serializer = ImageConversionSerializer(data=request.data)

    if serializer.is_valid():
        image = serializer.save()
        data = {}
        data['Base 64'] = image.base64_conversion
        data['MD5 String'] = image.MD5_hash_string

        return Response(data, status.HTTP_200_OK)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
