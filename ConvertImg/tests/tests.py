from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class ImageConversionTestCase(APITestCase):

    def test_fail_with_invalid_image(self):
        data = {
            'image' : SimpleUploadedFile(
                name='test_invalid_img',
                content=open('ConvertImg/tests/static/test_invalid_img', 'rb').read(),
                content_type='image/jpeg')
        }
        response = self.client.post("", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_success_with_jpeg_image(self):
        data = {
            'image' : SimpleUploadedFile(
                name='test_image.jpg',
                content=open('ConvertImg/tests/static/test_image.jpg', 'rb').read(),
                content_type='image/jpeg')
        }
        response = self.client.post("", data)

        file1 = open("ConvertImg/tests/static/testobj_base64.txt", "r+")
        self.assertEqual(response.data['Base 64'], file1.read())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_success_with_png_image(self):
        data = {
            'image' : SimpleUploadedFile(
                name='test_image_2.png',
                content=open('ConvertImg/tests/static/test_image_2.png', 'rb').read(),
                content_type='image/png')
        }
        response = self.client.post("", data)

        file1 = open("ConvertImg/tests/static/testobj_base64.txt", "r+")
        self.assertEqual(response.data['Base 64'], file1.read())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
