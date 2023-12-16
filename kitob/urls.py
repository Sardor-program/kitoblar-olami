from kitob.views import (
                         AuthorListApiView,
                         AuthorDetailApiView,
                         AuthorCreateApiView,
                         AuthorUpdateApiView,
                         AuthorDeleteApiView,

                         CategoryListApiView,
                         CategoryDetailApiView,
                         CategoryCreateApiView,
                         CategoryUpdateApiView,
                         CategoryDeleteApiView,

                         BookListApiView,
                         BookDetailApiView,
                         BookCreateApiView,
                         BookUpdateApiView,
                         BookDeleteApiView,

                         BookAuthorListApiView,
                         BookAuthorDetailApiView,
                         BookAuthorCreateApiView,
                         BookAuthorUpdateApiView,
                         BookAuthorDeleteApiView,

                         SelectedBookListApiView,
                         SelectedBookDetailApiView,
                         SelectedBookCreateApiView,
                         SelectedBookUpdateApiView,
                         SelectedBookDeleteApiView,


                         )
from django.urls import path

urlpatterns = [
    path('author/list/', AuthorListApiView.as_view()),
    path('author/detail/<int:pk>/', AuthorDetailApiView.as_view()),
    path('author/create/', AuthorCreateApiView.as_view()),
    path('author/<int:pk>/update/', AuthorUpdateApiView.as_view()),
    path('author/<int:pk>/delete/', AuthorDeleteApiView.as_view()),

    path('category/list/', CategoryListApiView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailApiView.as_view()),
    path('category/create/', CategoryCreateApiView.as_view()),
    path('category/<int:pk>/update/', CategoryUpdateApiView.as_view()),
    path('category/<int:pk>/delete/', CategoryDeleteApiView.as_view()),

    path('book/list/', BookListApiView.as_view()),
    path('book/detail/<int:pk>/', BookDetailApiView.as_view()),
    path('book/create/', BookCreateApiView.as_view()),
    path('book/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('book/<int:pk>/delete/', BookDeleteApiView.as_view()),

    path('book-author/list/', BookAuthorListApiView.as_view()),
    path('book-author/detail/<int:pk>/', BookAuthorDetailApiView.as_view()),
    path('book-author/create/', BookAuthorCreateApiView.as_view()),
    path('book-author/<int:pk>/update/', BookAuthorUpdateApiView.as_view()),
    path('book-author/<int:pk>/delete/', BookAuthorDeleteApiView.as_view()),

    path('selected-book/list/', SelectedBookListApiView.as_view()),
    path('selected-book/detail/<int:pk>/', SelectedBookDetailApiView.as_view()),
    path('selected-book/create/', SelectedBookCreateApiView.as_view()),
    path('selected-book/<int:pk>/update/', SelectedBookUpdateApiView.as_view()),
    path('selected-book/<int:pk>/delete/', SelectedBookDeleteApiView.as_view()),


]

