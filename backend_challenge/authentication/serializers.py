# from rest_framework import serializers
# from .models import Choice, Question, Quiz, Course, Subject
# from E_learning_API.authentication.serializers import UserSerializer
# from django.shortcuts import get_object_or_404


# class CourseSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Course
#         fields = ('id', 'subject', 'title', 'slug', 'overview', 'created',)


# class SubjectSerializer(serializers.ModelSerializer):
#     courses = CourseSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Subject
#         fields = ('id', 'title', 'slug','courses')


# class ChoiceSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Choice
#         fields = ('choice','is_correct')


# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True)

#     class Meta:
#         model = Question
#         fields = ('quiz', 'question_text', 'hint', 'choices')
    
#     def create(self, validated_data):
#         # quiz = self.context['quiz']
#         # print(quiz)
#         choices_data = validated_data.pop('choices')
#         NewQuestion = Question.objects.create(**validated_data)
#         for choice_data in choices_data:
#             Choice.objects.create(question=NewQuestion, **choice_data)
#         return NewQuestion


# class QuizSerializer(serializers.ModelSerializer):
#     questions = QuestionSerializer(many=True, read_only=True)

#     class Meta:
#         model = Quiz
#         fields = ('level', 'pk', 'title','slug', 'single_attempt','pass_mark','success_text','fail_text','draft','duration','questions')
    
#     def create(self, validated_data):

#         newQuiz = Quiz.objects.create(**validated_data)
#         return newQuiz

 