from rest_framework import serializers
from .models import Task


# تعریف کلاس سریالایزر برای مدل Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # مدل مرتبط
        fields = "__all__"  # شامل تمام فیلدهای مدل
