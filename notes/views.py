from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Author, Note
from .serializers import CreateNoteSerializer, NoteSerializer
# Create your views here.

class NoteViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['entry']
    ordering_fields = ['created', 'updated']

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Note.objects.all()

        author_id = Author.objects.only(
            'id').get(user_id=user.id)
        return Note.objects.filter(author_id=author_id)

    def create(self, request, *args, **kwargs):
        serializer = CreateNoteSerializer(
            data=request.data,
            context={'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        note = serializer.save()
        serializer = NoteSerializer(note)
        return Response(serializer.data)
