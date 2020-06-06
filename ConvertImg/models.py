from django.db import models

# Create your models here.

class Image(models.Model):
    input_image = models.ImageField(upload_to = 'uploads/input_image')
    base64_conversion = models.CharField(max_length = 2000)
    MD5_hash_string = models.CharField(max_length = 40)
