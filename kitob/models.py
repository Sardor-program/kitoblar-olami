from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from image_optimizer.fields import OptimizedImageField
from accounts.models import User


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    status_category = models.BooleanField('Avtive', default=False)

    def __str__(self):
        return self.name_category


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    image = OptimizedImageField(upload_to='images/author')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    book_title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    image = OptimizedImageField(upload_to='images/books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17)
    book_file = models.FileField(upload_to='files/book_file', null=True, blank=True)
    audio_book = models.FileField(upload_to='files/audio_book', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.book_title


class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.book_id


class Reviews(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='child',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'comment by {self.user_id}'


class SelectedBooks(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} {self.book_id}'


class UserSendMessage(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    massage = models.TextField()

    def __str__(self):
        return self.username




