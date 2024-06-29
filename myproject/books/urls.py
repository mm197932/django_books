from django.urls import path
from books.views import BooksListView

app_name = 'books'

urlpatterns = [
    path("", BooksListView.as_view(), name="list"),
]