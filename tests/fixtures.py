import pytest


@pytest.fixture()
@pytest.mark.django_db
def token(client, django_user_model):
    username = "swiss1"
    password = "lol123"

    django_user_model.objects.create_user(
        username=username, password=password, role="user")

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["token"]