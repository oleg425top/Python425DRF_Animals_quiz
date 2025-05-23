from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from sections.models import Question, Section

class QuestionSerializer(ModelSerializer):
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'question_section', 'question')

class QuestionSectionSerializer(ModelSerializer):
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        fields = ('id', 'question_section')