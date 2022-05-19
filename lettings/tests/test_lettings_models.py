import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_model():
    adress = Address.objects.create(
        number="13",
        street="rue openclassroom",
        city="Paris",
        state="France",
        zip_code="75000",
        country_iso_code="FRA",
    )
    expected_value = "13 rue openclassroom"
    assert str(adress) == expected_value


@pytest.mark.django_db
def test_letting_model():
    address = Address.objects.create(
        number="13",
        street="rue openclassroom",
        city="Paris",
        state="France",
        zip_code="75000",
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(
        title="miss student",
        address=address
    )
    expected_value = "miss student"
    assert str(letting) == expected_value
