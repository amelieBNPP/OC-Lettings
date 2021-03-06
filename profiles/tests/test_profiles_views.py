import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_index_view():
    user_student = User.objects.create(
        username="student openclassroom",
    )
    Profile.objects.create(
        user=user_student,
        favorite_city="Paris"
    )
    user_mentor = User.objects.create(
        username="mentor openclassroom",
    )
    Profile.objects.create(
        user=user_mentor,
        favorite_city="London"
    )
    client = Client()
    path = reverse('profiles:index')
    response = client.get(path)
    response_content = response.content.decode()
    expected_content = [
        '<title>Profiles</title>',
        'href="/profiles/student%20openclassroom/"',
        'href="/profiles/mentor%20openclassroom/"',
        'mentor openclassroom',
        'student openclassroom',
    ]
    for content in expected_content:
        assert content in response_content
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view():
    user_student = User.objects.create(
        username="student openclassroom",
        first_name="student",
        last_name="openclassroom",
        email="student@openclassroom.com"
    )
    Profile.objects.create(
        user=user_student,
        favorite_city="Paris"
    )

    client = Client()
    path = reverse('profiles:profile', kwargs={'username': "student openclassroom"})

    response = client.get(path)
    response_content = response.content.decode()
    expected_content = [
        '<title>Profiles</title>',
        '<h1>student openclassroom</h1>',
        '<p class="lead">First name: student</p>',
        '<p class="lead">Last name: openclassroom</p>',
        '<p class="lead">Email: student@openclassroom.com</p>',
        '<p class="lead">Favorite city: Paris</p>'
    ]
    for content in expected_content:
        assert content in response_content
    assert response.status_code == 200
