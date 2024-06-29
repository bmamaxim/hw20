from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """
    Класс тестирование пользователя.
    """

    def setUp(self) -> None:
        self.user = User.objects.create(email="testoff@mail.ru", password="llleike11")
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """
        Тест регистрация пользователя.
        """
        data = {
            "email": "test_1@mail.ru",
            "password": "qwe123",
        }
        response = self.client.post(reverse("users:register"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())

    def test_user_list(self):
        """
        Тест просмотр пользователей.
        :return:
        """
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        """
        Тест изменить пользователя.
        """
        url = reverse("users:user-update", args=(self.user.pk,))
        data = {
            "first_name": "test",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'email': 'testoff@mail.ru',
                'first_name': 'test',
                'password': 'llleike11',
                'payment': [],
            }
        )
