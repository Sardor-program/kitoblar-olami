from rest_framework.exceptions import ValidationError
from accounts.serializers import UserSerializer
from kitob.models import Book, BookAuthor, SelectedBooks, Reviews, UserSendMessage, Author, Category
from rest_framework import serializers



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id',  'first_name', 'last_name', 'biography', 'image',)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id',  'name_category', 'status_category')


class BookSerializer(serializers.ModelSerializer):


    book_comments_count = serializers.SerializerMethodField('get_post_comments_count')

    class Meta:
        model = Book
        fields = ('id',
                  'book_title',
                  'author',
                  'description',

                  'image', 'category',
                  'isbn', 'book_comments_count', 'book_file', 'audio_book',
                  'created_time',)

    def get_post_comments_count(self, obj):
        return obj.comments.count()




class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ('id', 'book_id', 'author_id')


class SelectedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedBooks
        fields = ('id', 'user_id', 'book_id')


class ReviewsSerializer(serializers.ModelSerializer):

    user_id = UserSerializer(read_only=True)
    book_id = BookSerializer(read_only=True)
    replies = serializers.SerializerMethodField('get_replies')


    class Meta:
        model = Reviews
        fields = ('id',
                  'user_id',
                  'book_id',
                  'comment',
                  'replies',
                  'stars_given'
                  )

        def get_replies(self, obj):
            if obj.child.exists():
                serializers = self.__class__(obj.child.all(), many=True, context=self.context)
                return serializers.data
            else:
                return None



