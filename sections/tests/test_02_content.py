from rest_framework import status
from rest_framework.test import APITestCase

from sections.models import Section, Content
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
        self.test_content = Content.objects.create(
            section=self.test_section,
            title='Test Content Title',
            content='Test Content'
        )

    def test_07_content_create(self):
        data = {
            'section': self.test_section.id,
            'title': 'Test Title Content Create',
            'content': 'Test Content Create'
        }
        responce = self.client.post('/content/create/', data)
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responce.json().get('title'), 'Test Title Content Create'),
        self.assertEqual(responce.json().get('content'), 'Test Content Create'),

    def test_08_content_detail(self):
        responce = self.client.get(f'/content/{self.test_content.id}/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json().get('title'), 'Test Content Title')
        self.assertEqual(responce.json().get('content'), 'Test Content')

    def test_09_content_update(self):
        data = {
            'title': 'Test Title Content Update PATCH',
        }
        responce = self.client.patch(f'/content/{self.test_content.id}/update/', data=data)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json().get('title'), 'Test Title Content Update PATCH')

    def test_10_content_delete(self):
        responce = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)
        responce = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)

    def test_11_content_list(self):
        responce = self.client.get('/content/')
        # print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json()['results'][0]['id'], 6)

    def test_12_content_create_forbidden(self):
        self.user = get_member_user()
        responce = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = responce.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            'section': self.test_section.id,
            'title': 'Test Title Content Create',
            'content': 'Test Content Create Member',
        }
        responce = self.client.post('/content/create/', data=data)
        self.assertEqual(responce.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(responce.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')
