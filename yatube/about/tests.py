from django.test import TestCase, Client
from http import HTTPStatus


class TaskURLTests(TestCase):
    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()

    def test_about_author_url_exists_at_desired_location(self):
        """Страница об авторе
        "/about/author/"
        доступна любому пользователю.
        """
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_tech_url_exists_at_desired_location(self):
        """Страница о технологиях
        "/about/tech/"
        доступна любому пользователю.
        """
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
