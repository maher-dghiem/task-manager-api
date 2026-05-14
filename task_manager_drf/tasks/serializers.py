# tasks/serializers.py

from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "priority",
            "status",
            "owner",
            "created_at",
            "updated_at",
        ]

    # Validate due_date
    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    # Validate priority + status choices (extra safety)
    def validate(self, attrs):
        priority = attrs.get("priority")
        status = attrs.get("status")

        valid_priorities = ["low", "medium", "high"]
        valid_statuses = ["pending", "in-progress", "done"]

        if priority and priority not in valid_priorities:
            raise serializers.ValidationError({"priority": "Invalid priority value."})

        if status and status not in valid_statuses:
            raise serializers.ValidationError({"status": "Invalid status value."})

        return attrs
