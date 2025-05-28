from rest_framework import status
from rest_framework.test import APITestCase

from sections.models import Section
from sections.tests.utils import get_admin_user, get_member_user


class SectionTestCase(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')  # ['access'] - либо такой вариант
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title='Test Section',
            description='Test Description'
        )

    def test_01_section_create(self):
        data = {
            'title': 'Test Section Create',
            'description': 'Test Description Create'
        }
        responce = self.client.post('/section/create/', data=data)
        # print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responce.json().get('title'), 'Test Section Create')

    def test_02_section_detail(self):
        responce = self.client.get(f'/section/{self.test_section.id}/')
        # print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json().get('title'), "Test Section")
        self.assertEqual(responce.json().get('description'), "Test Description")

    def test_03_section_update(self):
        data = {
            'title': 'Test Section Patch PUT',
            'description': 'Test Description Patch PUT'
        }
        responce = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json().get('title'), 'Test Section Patch PUT')
        self.assertEqual(responce.json().get('description'), 'Test Description Patch PUT')

    def test_04_section_delete(self):
        responce = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)
        responce = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)

    def test_05_section_list(self):
        responce = self.client.get('/section/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json()['results'][0]['title'], 'Test Section')

    def test_06_section_create_forbidden(self):
        self.user = get_member_user()
        responce = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = responce.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "title": "Test Section Create Member",
            "description": "Test Description Create Member",
        }
        responce = self.client.post('/section/create/', data=data)
        self.assertEqual(responce.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(responce.json().get('detail'), "У вас недостаточно прав для выполнения данного действия.")
