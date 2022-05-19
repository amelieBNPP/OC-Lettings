import pytest

from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_letting_index_view():
    address_student = Address.objects.create(
        number="13",
        street="rue openclassroom",
        city="Paris",
        state="France",
        zip_code="75000",
        country_iso_code="FRA",
    )
    Letting.objects.create(
        title="miss student",
        address=address_student
    )
    address_mentor = Address.objects.create(
        number="13",
        street="rue soutenance",
        city="Paris",
        state="France",
        zip_code="75000",
        country_iso_code="FRA",
    )
    Letting.objects.create(
        title="mr mentor",
        address=address_mentor
    )
    client = Client()
    path = reverse('lettings:index')
    response = client.get(path)
    response_content = response.content.decode()
    expected_content = [
        '<title>Lettings</title>',
        '<a href="/lettings/1/">',
        '<a href="/lettings/2/">',
        'miss student',
        'mr mentor',
    ]
    for content in expected_content:
        assert content in response_content
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view():
    address_student = Address.objects.create(
        number="13",
        street="rue openclassroom",
        city="Paris",
        state="France",
        zip_code="75000",
        country_iso_code="FRA",
    )
    letting_student = Letting.objects.create(
        title="miss student",
        address=address_student
    )

    client = Client()
    path = reverse('lettings:letting', kwargs={'letting_id': letting_student.pk})

    response = client.get(path)
    response_content = response.content.decode()
    expected_content = [
        '<title>miss student</title>',
        '<h1>miss student</h1>',
        '<p>13 rue openclassroom</p>',
        '<p>Paris, France 75000</p>',
        '<p>FRA</p>'
    ]
    for content in expected_content:
        assert content in response_content
    assert response.status_code == 200
