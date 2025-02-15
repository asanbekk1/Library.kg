import json
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'forms from JSON file'

    def handle(self, *args, **kwargs):
        with open('books.json', 'r') as file:
            books = json.load(file)
            for book_data in books:
                Book.objects.create(
                    title=book_data['title'],
                    author=book_data['author'],
                    price=book_data['price']
                )
        self.stdout.write(self.style.SUCCESS('Books loaded successfully'))