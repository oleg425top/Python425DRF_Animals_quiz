from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from sections.models import Question, Section


class QuestionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'question')


class QuestionSectionSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'answer')
