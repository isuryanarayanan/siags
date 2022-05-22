"""
Testing the create user api endpoint.
"""
# Other imports
import json
from requests.auth import HTTPBasicAuth
# Django imports
from django.test import TestCase

from django.core.exceptions import ObjectDoesNotExist
# Rest framework imports
from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    RequestsClient,
    APITestCase
)
# My imports
from accounts.models.user import User


class CreateUserTestCase(APITestCase):

    version = 'v1'
    host = '127.0.0.1'
    port = '8000'
    endpoint = f'/accounts/api/{version}/create_user/'
    url = f'http://{host}:{port}{endpoint}'

    # Inorder for the test to run in order it is named
    # alphabetically increasing.

    def test_A_endpoint(self):
        # Making sure the endpoint works.
        print("\nRunning endpoint check.. (create_user)")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"Endpoint status {response.status_code}")

    def test_B_customer_creation(self):
        # Try creating a user with standard parameters.
        print("\nRunning user creation test for customer users..")
        user = {
            "user_type": "customer",
            "username": "customer",
            "email": "customer@sds.com",
            "password1": "customer1",
            "password2": "customer1"
        }
        print(user)
        response = self.client.post(self.url, user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username='customer').mode, 1)
        print(f'Created user {User.objects.get(username="customer")}')

    def test_C_vendor_creation(self):
        # Try creating a user with standard parameters.
        print("\nRunning user creation test for vendor users..")
        user = {
            "user_type": "vendor",
            "username": "vendor",
            "email": "vendor@sds.com",
            "password1": "vendor1",
            "password2": "vendor1"
        }
        print(user)
        response = self.client.post(self.url, user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username='vendor').mode, 2)
        print(f'Created user {User.objects.get(username="vendor")}')

    def test_D_administrator_creation_A(self):
        # Try creating a user with standard parameters.

        print(
            "\nRunning user creation test for administrator users (without authorization)")

        user = {
            "user_type": "administrator",
            "username": "administrator",
            "email": "administrator@sds.com",
            "password1": "administrator1",
            "password2": "administrator1"
        }

        print(user)
        response = self.client.post(self.url, user, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        try:
            User.objects.get(username="administrator")
            print(f'Created user {User.objects.get(username="administrator")}')
            print('It should not be created since administrator is a protected view')
        except ObjectDoesNotExist:
            print("Administrator not created.")

    def test_D_administrator_creation_B(self):
        # Try creating a user with standard parameters.

        print("\nRunning user creation test for administrator users (with authorization)")
        print("Creating an authorized user")

        authorized_user = User.objects.create_user(
            'authorizedUser',
            'authorizedUser@gmail.com',
            3,
            'authorizedUser1',
        )

        # Authenticating the user forcefully
        self.client.force_authenticate(
            User.objects.get(username='authorizedUser'))

        user = {
            "user_type": "administrator",
            "username": "administrator",
            "email": "administrator@sds.com",
            "password1": "administrator1",
            "password2": "administrator1"
        }
        print(user)
        response = self.client.post(self.url, user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get(username='administrator').mode, 3)
        print(
            f'Created user {User.objects.get(username="administrator")} by {authorized_user.username}')
