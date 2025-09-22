# This is the response that we will return
from rest_framework.response import Response
# This is the model that we will use
from .models import Note
# This is the serializer that we will use
from .serializers import NoteSerializer

# ************************ Note API *****************************
# This is function will return the note list
def getNoteList(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# This will return the specifuc note details
def getNoteDetail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

# Function will create a notes
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# This function will update data
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data = data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# this function will delete note
def deleteNote(request, pk):
    data = request.data
    note = Note.objects.get(id = pk)
    note.delete()
    return Response('Note was deleted!')

