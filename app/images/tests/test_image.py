from io import BytesIO

import pytest
from PIL import Image
from django.core.files.base import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


@staticmethod
def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new('RGB', size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


@pytest.mark.django_db
def test_create_image(basic_user, api_client):
    file = get_image_file()
    data = {
        'original_file': file,
    }

    response = api_client.post(reverse('images-list'), data=data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_create_image_wrong_extension(api_client):
    file = SimpleUploadedFile('test.mp4', b'test', 'video/mp4')
    data = {
        'original_file': file,
    }

    response = api_client.post(reverse('images-list'), data=data)

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_image_no_file(api_client):
    data = {}

    response = api_client.post(reverse('images-list'), data=data)
    assert response.status_code == 400
    assert response.json() == {'original_file': ['No file was submitted.']}
