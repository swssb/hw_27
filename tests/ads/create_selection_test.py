import pytest

from ads.models import Selection


@pytest.mark.django_db
def test_create_selection(client, user_token, selection, ad):
    # Selection.objects.create(name="my select", owner=2, items=[1, 2, 5])
    expected_response = {
        "id": 2,
        "name": selection.name,
        "owner": selection.owner.id,
        "items": [ad.id]
    }
    response = client.post("/selection/create/", data={
        "name": selection.name,
        "owner": selection.owner.id,
        "items": [ad.id]
    }, HTTP_AUTHORIZATION="Bearer " + user_token)

    # assert response.status_code == 201
    assert response.data == expected_response
