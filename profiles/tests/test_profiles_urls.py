from django.urls import reverse, resolve


def test_get_profiles_index():
    path = reverse('profiles:index')
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


def test_get_profile():
    path = reverse('profiles:profile', kwargs={'username': 'username'})
    assert path == "/profiles/username/"
    assert resolve(path).view_name == "profiles:profile"
