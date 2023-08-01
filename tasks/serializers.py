from rest_framework import serializers
from .models import Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description", "category", "created_at")
        read_only_fields = ("created_at",)
