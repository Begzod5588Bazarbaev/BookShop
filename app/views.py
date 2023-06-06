from django.shortcuts import render
from .models import Books
from rest_framework import generics
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

class BookList(generics.ListCreateAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	queryset = Books.objects.all()
	serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	queryset = Books.objects.all()
	serializer_class = BookSerializer