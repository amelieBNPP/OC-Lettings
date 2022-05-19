from django.urls import reverse, resolve


def test_get_lettings_index():
    path = reverse('lettings:index')
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


def test_get_letting():
    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
