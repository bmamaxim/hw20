from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Direction, Subscription
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="testoff@mail.ru", password="llleike11")
        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(
            title_lesson="test_test",
            description_lesson="test_test",
            url_lesson="https://www.youtube.com/",
            owner=self.user,
        )

    def test_create_lesson(self):
        """
        test lesson create
        :return:
        """
        data = {
            "title_lesson": "test",
            "description_lesson": "test",
            "url_lesson": "https://www.youtube.com/",
        }
        response = self.client.post("/lesson/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.all().exists())

    def test_list_lesson(self):
        """
        test lesson list
        :return:
        """
        response = self.client.get("/lesson/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.pk,
                        "title_lesson": "test_test",
                        "description_lesson": "test_test",
                        "owner": self.user.pk,
                        "url_lesson": "https://www.youtube.com/",
                    }
                ],
            },
        )

    def test_retrieve_lesson(self):
        """
        test detail lesson
        :return:
        """
        url = reverse("materials:view", args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": self.lesson.pk,
                "title_lesson": "test_test",
                "description_lesson": "test_test",
                "owner": self.user.pk,
                "url_lesson": "https://www.youtube.com/",
            },
        )

    def test_update_lesson(self):
        """
        test update lesson
        :return:
        """
        url = reverse("materials:update", args=(self.lesson.pk,))
        data = {
            "title_lesson": "test",
            "description_lesson": "test",
            "url_lesson": "https://www.youtube.com/",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": self.lesson.pk,
                "title_lesson": "test",
                "description_lesson": "test",
                "owner": self.user.pk,
                "url_lesson": "https://www.youtube.com/",
            },
        )

    def test_delete_lesson(self):
        """
        test delete lesson
        :return:
        """
        url = reverse("materials:delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="testoff@mail.ru", password="llleike11")
        self.client.force_authenticate(user=self.user)
        self.direction = Direction.objects.create(
            title_direction="it", description_direction="it", owner=self.user
        )
        self.url = reverse("materials:sub")
        self.data = {"user": self.user.id, "direction": self.direction.id}

    def test_sub_create(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "подписка добавлена"})

    def test_sub_delete(self):
        Subscription.objects.create(user=self.user, direction=self.direction)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "подписка удалена"})
