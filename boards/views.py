
from rest_framework import viewsets

from .models import Board, Label, List
from .serializers.boards_serializers import BoardSerializer
from .serializers.labels_serializers import LabelSerializer
from .serializers.lists_serializers import ListSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint to create, retrieve, update, and delete Boards.
    """
    serializer_class = BoardSerializer

    def get_queryset(self):
        """"
        Optionally filter the returned boards.
        """
        return Board.objects.all()


class ListViewSet(viewsets.ModelViewSet):
    """
    ViewSet to provide CRUD functionality for List model
    """
    serializer_class = ListSerializer

    def get_queryset(self):
        """
    API endpoint to manage Lists within Boards.
    """
        return List.objects.all()


class LabelViewSet(viewsets.ModelViewSet):
    """
    API endpoint to manage Lists within Boards.
    """
    serializer_class = LabelSerializer

    def get_queryset(self):
        """
    API endpoint to manage Labels for tasks/cards.
       """
        return Label.objects.all()
