from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Genre, Comment
from .serializers import BookSerializer, GenreSerializer, CommentSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]




# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly
# from .models import Book, Genre, Comment
# from .serializers import (BookSerializer, BookSerializerForAdmin,
#                           GenreSerializer, CommentSerializer)
# from .permissions import IsAuthorOrReadOnly
#
#
# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
# class GenreViewSet(ModelViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
# class GenreAPIView(ListCreateAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#
#
# class GenreRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer
#     lookup_field = "pk"
#     lookup_url_kwarg = "genre_id"
#
#
# class BookAPIView(ListCreateAPIView):
#     serializer_class = BookSerializer
#
#     def get_queryset(self):
#         genre_id = self.kwargs.get("genre_id")
#
#         if genre_id:
#             books = Book.objects.filter(genre_id=genre_id)
#         else:
#             books = Book.objects.all()
#         return books
#
#     def get_serializer_class(self):
#         if self.request.user.is_staff:
#             return BookSerializerForAdmin
#         return BookSerializer
#
#
# class BookRetrieveAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "pk"
#     lookup_url_kwarg = "book_id"
#
#     def get_serializer_class(self):
#         if self.request.user.is_staff:
#             return BookSerializerForAdmin
#         return BookSerializer
#
#
# class CommentAPIView(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [DjangoModelPermissions, IsAuthorOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
