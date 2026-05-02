import pytest
from django.core import mail
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from accounts.models import VerificationToken


User = get_user_model()

@pytest.fixture()
def user_test(db):
    return User.objects.create_user(username="user_test", password="1234567", email="nick@test.com")


def test_registration(db):
    client=APIClient()
    user={"username": "nick","email":"nick@test.com", "first_name":"nick", "password":"1234567", "second_password":"1234567"}
    response = client.post("/api/auth/registration/", user)

    assert response.status_code == 201

    
    assert len(mail.outbox) == 1
    assert mail.outbox[0].to == ["nick@test.com"]
    
    
    
# def test_registrationVertification(user_test):
#     client=APIClient()
#     token_obj = VerificationToken.objects.create(
#         user=user_test,
#         token="abc123"
#     )
    
#     print(token_obj.token)
#     response=client.post("/api/register_vertify/", {"token": "abc123"})
#     assert response.status_code==200
    