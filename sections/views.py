from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sections.models import Section, Content, Question
from sections.paginators import SectionPaginator, ContentPaginator, QuestionPaginator
from sections.permissions import IsModerator, IsSuperUser
from sections.serializers.content_serializer import ContentSerializer, ContentListSerializer
from sections.serializers.question_serializer import QuestionSerializer, QuestionSectionSerializer
from sections.serializers.section_serializer import SectionSerializer, SectionListSerializer


# from sections.urls import question


class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = ContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsSuperUser)


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSectionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator


class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].strip().lower()
        member_answer = request.data.get('member_answer').strip().lower()
        is_correct = member_answer == answer
        return Response({'is_correct': is_correct})
