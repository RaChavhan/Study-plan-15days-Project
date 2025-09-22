from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, NoteSerializer
from .models import Note
from rest_framework.decorators import api_view
from .utils import getNoteList, getNoteDetail, createNote, updateNote , deleteNote


# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello word view")

class RegisterAPI(APIView):
    def post(shelf, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "role": user.role
        })
    

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/myapp/notes/'},
        {'GET': '/myapp/notes/:id'},
        {'POST': '/myapp/notes/'},
        {'PUT': '/myapp/notes/:id'},
        {'DELETE': '/myapp/notes/:id'},
    ]
    return Response(routes)

# -------- Notes Views --------

@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        return getNoteList(request)
    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    if request.method == 'GET':
        return getNoteDetail(request, pk)
    elif request.method == 'PUT':
        return updateNote(request, pk)
    elif request.method == 'DELETE':
        return deleteNote(request, pk)