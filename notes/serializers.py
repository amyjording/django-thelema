from rest_framework import serializers
from .models import Author, Note

class CreateNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['entry']

    
    def save(self, **kwargs):
        author = Author.objects.get(
                user_id=self.context['user_id'])
        
        entry = self.validated_data['entry']
        
        note = Note.objects.create(entry=entry, author=author)

        return note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['entry', 'created', 'updated', 'author']