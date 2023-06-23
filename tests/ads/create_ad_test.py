import pytest

from ads.models import Ad


@pytest.mark.django_db
def test_create_ad(client, user_token):

    expected_response = {
        "id": 1,
        "author": 1,
        "name": "Продам гараж",
        "price": 50,
        "description": None,
        "is_published": False,
        "image": None,
        "category": None
    }

    response = client.post("/ad/create/", data={
        "author": 1,
        "name": "Продам гараж",
        "price": 50,
    }, HTTP_AUTHORIZATION="Bearer " + user_token)

    assert response.data == expected_response
    assert response.status_code == 201
