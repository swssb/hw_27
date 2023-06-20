import pytest

from ads.models import Selection


@pytest.mark.django_db
def test_create_selection(client, token):
    Selection.objects.create(name="my select", owner=2, items=[1, 2, 5])
    expected_response = {
        "name": "my select",
        "owner": 2,
        "items": [1, 2, 5]
    }
    response = client.post("/selection/create/", data={
        "name": "my select",
        "owner": 2,
        "items": [1, 2, 5]
    }, HTTP_AUTHORIZATION="Bearer " + token)

    assert response.status_code == 201
    assert response.data == expected_response
