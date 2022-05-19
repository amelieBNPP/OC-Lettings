import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_index_view():
    client = Client()
    path = reverse('home')
    response = client.get(path)
    response_content = response.content.decode()
    expected_content = [
        '<title>Holiday Homes</title>',
        '<h1>Welcome to Holiday Homes</h1>',
        '<a href="/profiles/">Profiles</a>',
        '<a href="/lettings/">Lettings</a>',
    ]
    for content in expected_content:
        assert content in response_content
    assert response.status_code == 200
