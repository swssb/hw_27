import pytest


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "swissik"
    password = "lol123"
    # location = 1
    email = "swssb@bk.ru"
    birth_date = "2000-12-25"

    django_user_model.objects.create_user(
        username=username, password=password, email=email, birth_date=birth_date, role='admin')

    response = client.post(
        "/user/token/",
        {
            "username": username,
            "password": password,
        },
        format='json'
    )

    return response.data["access"]