from django.urls import reverse, resolve


def test_get_index():
    path = reverse('home')
    assert path == "/"
    assert resolve(path).view_name == "home"
