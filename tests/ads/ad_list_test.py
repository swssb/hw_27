import pytest

from ads.models import Ad
from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client, ad):

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": 1,
                "author": ad.author.username,
                "category": None,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
                "is_published": False,
                "image": None
             }
            ]
        }
    response = client.get('/ad/')
    assert response.status_code == 200
    assert response.data == expected_response

