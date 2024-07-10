from django.db import models

# Create your models here.
# ORM
# Reference_books
# category | description

class Reference_book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} # {self.pk}"
    

class Book(models.Model):
        # pk # number # reference book #
    number = models.CharField(max_length=100)
    reference_book = models.ForeignKey(
        Reference_book,
        on_delete=models.PROTECT,
        related_name="books"
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"book # {self.pk}"
