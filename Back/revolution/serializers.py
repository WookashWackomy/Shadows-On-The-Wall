from rest_framework import serializers
from revolution.models import Problem, AppUser, Tag, Comment
from datetime import datetime


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'user', 'title', 'description', 'date_time', 'comments', 'votes', 'tags', 'solutions']


class NewProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'user', 'title', 'description', 'tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['pk']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'text', 'date']
