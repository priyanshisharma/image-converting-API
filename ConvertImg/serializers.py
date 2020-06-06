import base64
import hashlib
from rest_framework import serializers
from .models import Image


class ImageConversionSerializer(serializers.ModelSerializer):
    '''
    This serializer reads the image for conversion, and
    convefrts it to an MD5 string and Base 64
    '''

    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ['image']

    def save(self):

        base64_conversion = base64.b64encode(self.validated_data['image'].read())
        MD5_hash_string = f'{hashlib.md5(base64_conversion)}'

        image = Image(
            input_image=self.validated_data['image'],
            base64_conversion=base64_conversion.decode("utf-8"),
            MD5_hash_string=MD5_hash_string
        )
        image.save()
        return image
