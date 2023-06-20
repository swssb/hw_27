import pytest

from ads.models import Ad


@pytest.mark.django_db
def test_create_ad(client, token):
    Ad.objects.create(
        author=1,
        name="Gena",
        price=50,
    )

    expected_response = {
        "author": 1,
        "name": "Gena",
        "price": 50,
        "description": None,
        "is_published": False,
        "image": None,
        "category": None
    }

    response = client.post("/ad/create/", data={
        "author": 1,
        "name": "Gena",
        "price": 50,
    }, HTTP_AUTHORIZATION="Bearer " + token)

    assert response.status_code == 201
    assert response.data == expected_response