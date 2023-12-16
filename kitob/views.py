from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from kitob.book_pagination import BookPagination
from kitob.custom_pagination import CustomPagination
from kitob.models import Author, Category, Book, BookAuthor, SelectedBooks, Reviews
from kitob.serializers import AuthorSerializer, CategorySerializer, BookSerializer, BookAuthorSerializer, \
    SelectedBooksSerializer, ReviewsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

#=======================================================================================================================
class AuthorListApiView(generics.ListAPIView):
   serializer_class = AuthorSerializer
   permission_classes = [AllowAny, ]
   pagination_class = CustomPagination

   filter_backends = (DjangoFilterBackend, SearchFilter)

   filter_fields = ('id', 'first_name', 'last_name')
   search_fields = ('id', 'first_name', 'last_name')

   def get_queryset(self):
      return Author.objects.all()





class AuthorDetailApiView(APIView):
   def get(self, request, pk):
      try:
         author = Author.objects.get(id=pk)
         serializer_data = AuthorSerializer(author).data
         data = {
            "status": "Successfully",
            "massage": serializer_data
         }
         return Response(data)
      except Exception:
         return Response(
            {
               "status": False,
               "massage": "Author is not found"
            }, status=status.HTTP_404_NOT_FOUND
         )


class AuthorCreateApiView(APIView):
   def post(self, request):
      data = request.data
      serializer = AuthorSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         data = {
            "status": "Author is created",
            "author": data
         }
         return Response(data)
      else:
         return Response(
            {
               "status": False,
               "massage": "Serializer is not valid"
            }, status=status.HTTP_400_BAD_REQUEST
         )


class AuthorUpdateApiView(APIView):

   def put(self, request, pk):
      author = get_object_or_404(Author.objects.all(), id=pk)
      data = request.data
      serializer = AuthorSerializer(instance=Author, data=data, partial=True)
      if serializer.is_valid(raise_exception=True):
         author_saved = serializer.save()
      return Response(
         {
            "status": True,
            "massage": f'Author {author_saved} successfuly updated'
         }
      )


class AuthorDeleteApiView(APIView):

   def delete(self, request, pk):
      try:
         author = Author.objects.get(id=pk)
         author.delete()

         return Response(
            {
               "status": True,
               "massage": "Author is successfuly deleted"
            }, status=status.HTTP_200_OK
         )
      except Exception:
         return Response(
            {
               "status": False,
               "massage": "Author is not deleted"
            }, status=status.HTTP_400_BAD_REQUEST
         )




class CategoryListApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]

    filter_backends = (DjangoFilterBackend, SearchFilter)

    filter_fields = ('id', 'name_category')
    search_fields = ('id', 'name_category')



    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailApiView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            serializer_data = CategorySerializer(category).data
            data = {
                "ststus": "Successfully",
                "massage": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Category is not found"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class CategoryCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Category are created",
                "massage": data
            }
            return Response(data)
        else:
            return Response(
                {
                    "status": False,
                    "massage": "Serializer is not valid"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class CategoryUpdateApiView(APIView):
    def put(self, request, pk):
        category = get_object_or_404(Category.objects.all(), id=pk)
        data = request.data
        serializer = CategorySerializer(instance=category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response(
            {
                "status": True,
                "massage": f'Category {category_saved} successfuly updated'
            }
        )


class CategoryDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
            category.delete()

            return Response(
                {
                    "status": True,
                    "massage": "Category is successfully deleted"
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Category is not deleted"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class BookListApiView(generics.ListAPIView):
   serializer_class = BookSerializer
   permission_classes = [AllowAny, ]
   pagination_class = BookPagination

   filter_backends = (DjangoFilterBackend, SearchFilter)

   filter_fields = ('id', 'book_title', )
   search_fields = ('id', 'book_title', )


   def get_queryset(self):
      return Book.objects.all()


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status": "Successfully",
                "massage": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Book is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )


class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Book are created",
                "books": data
            }
            return Response(data)
        else:
            return Response(
                {
                    "status": False,
                    "massage": "Serializer is not valid"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                "massage": f'Book {book_saved} successfuly updated'
            }
        )


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()

            return Response(
                {
                    "status": True,
                    "massage": "Book is successfuly deleted"
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Book is not deleted"
                }, status=status.HTTP_400_BAD_REQUEST
            )

#=======================================================================================================================

class BookAuthorListApiView(APIView):
    def get(self, request):
        bookauthor = BookAuthor.objects.all()
        serializer_data = BookAuthorSerializer(bookauthor, many=True).data
        data = {
            "status": f'Return {len(bookauthor)} bookauthors',
            "massage": serializer_data
        }
        return Response(data)


class BookAuthorDetailApiView(APIView):
    def get(self,request, pk):
        try:
            bookauthor = BookAuthor.objects.get(id=pk)
            serializer_data = BookAuthorSerializer(bookauthor).data
            data = {
                "status": "Successfuly",
                "massage": serializer_data
            },
            return Response(data)
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "BookAuthor is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )


class BookAuthorCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookAuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "BookAuthor are created",
                "books": data
            }
            return Response(data)
        else:
            return Response(
                {
                    "status": False,
                    "massage": "Serializer is not valid"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class BookAuthorUpdateApiView(APIView):
    def put(self, request, pk):
        bookauthor = get_object_or_404(BookAuthor.objects.all(), id=pk)
        data = request.data
        serializer = BookAuthorSerializer(instance=bookauthor, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            bookauthor_saved = serializer.save()
        return Response(
            {
                "status": True,
                "massage": f'BookAuthor {bookauthor_saved} successfuly updated'
            }
        )


class BookAuthorDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            bookauthor = BookAuthor.objects.get(id=pk)
            bookauthor.delete()

            return Response(
                {
                    "status": True,
                    "massage": "BookAuthor is successfuly deleted"
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "BookAuthor is not deleted"
                }, status=status.HTTP_400_BAD_REQUEST
            )



class SelectedBookListApiView(generics.ListAPIView):
    serializer_class = SelectedBooksSerializer
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return SelectedBooks.objects.all()


class SelectedBookDetailApiView(generics.RetrieveAPIView):
    serializer_class = SelectedBooksSerializer
    permission_classes = [AllowAny,]
    queryset = SelectedBooks.objects.all()


class SelectedBookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = SelectedBooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Selected Book are created",
                "books": data
            }
            return Response(data)
        else:
            return Response(
                {
                    "status": False,
                    "massage": "Serializer is not valid"
                }, status=status.HTTP_400_BAD_REQUEST
            )


class SelectedBookUpdateApiView(APIView):
    def put(self, request, pk):
        selected_books = get_object_or_404(SelectedBooks.objects.all(), id=pk)
        data = request.data
        serializer = SelectedBooksSerializer(instance=selected_books, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            selected_books_saved = serializer.save()
        return Response(
            {
                "status": True,
                "massage": f'Selected Book {selected_books_saved} successfuly updated'
            }
        )


class SelectedBookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            selected_books = SelectedBooks.objects.get(id=pk)
            selected_books.delete()

            return Response(
                {
                    "status": True,
                    "massage": "Selected Book is successfuly deleted"
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "massage": "Selected Book is not deleted"
                }, status=status.HTTP_400_BAD_REQUEST
            )



#=======================================================================================================================

