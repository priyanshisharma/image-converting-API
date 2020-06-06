import base64
import hashlib
from rest_framework import serializers
from .models import Image


class ImageConversionSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['image']

    def save(self):

        base64_conversion = base64.b64encode(self.validated_data['image'].read())
        MD5_hash_string = hashlib.md5(base64_conversion)
        
        image = Image(
            input_image=image,
            base64_conversion=base64_conversion,
            MD5_hash_string=MD5_hash_string
        )
        image.save()
        return image
