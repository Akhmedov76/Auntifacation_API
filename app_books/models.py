from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['-id']
        db_table = 'author'


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-id']
        db_table = 'book'
