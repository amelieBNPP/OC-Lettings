import pytest

from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_user_model():
    user = User.objects.create(
        username="student openclassroom",
    )
    expected_value = "student openclassroom"
    assert str(user) == expected_value


@pytest.mark.django_db
def test_profile_model():
    user = User.objects.create(
        username="student openclassroom",
    )
    profiles = Profile.objects.create(
        user=user,
        favorite_city="Paris"
    )

    expected_value = "student openclassroom"
    assert str(profiles) == expected_value
