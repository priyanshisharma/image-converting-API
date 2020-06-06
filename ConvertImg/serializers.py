import base64
from rest_framework import serializers
from models import Image

class ImageConversionSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()

    class Meta:
        model = image
        fields = ['input_image']

    base64_conversion = base64.b64encode(image.read())

