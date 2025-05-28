from rest_framework import status
from rest_framework.test import APITestCase

from sections.models import Section, Content, Question
from sections.tests.utils import get_member_user


class SectionTestCase(APITestCase):
    def setUp(self):
        self.user = get_member_user()
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

        self.test_question = Question.objects.create(
            section=self.test_section,
            description='Test Question Description',
            question='Test Question',
            answer='Test Answer'
        )

    def test_13_question_list(self):
        responce = self.client.get('/question/')
        # print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json()['results'][0]['answer'], "Test Answer")

    def test_14_question_is_correct(self):
        responce = self.client.get(f'/question/{self.test_question.id}/')
        # print(responce.json())
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json()['question'], 'Test Question')

        responce = self.client.post(f'/question/{self.test_question.id - 1}/', {'member_answer': 'Test Answer'})
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.json().get('is_correct'), True)
