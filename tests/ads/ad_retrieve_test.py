import pytest


@pytest.mark.django_db
def test_ad_retrieve(client, ad, user_token):
    expected_response = {
        "id": ad.id,
        "author": ad.author.username,
        "category": None,
        "name": ad.name,
        "price": ad.price,
        "description": ad.description,
        "is_published": False,
        "image": None
    }
    response = client.get(f'/ad/{ad.id}/', HTTP_AUTHORIZATION="Bearer " + user_token)

    assert response.status_code == 200
    assert response.data == expected_response
