from rest_framework import serializers

from ..models import Board
from .lists_serializers import ListSerializer


class BoardSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['created_by', 'modified_at', 'modified_by', 'archived']
