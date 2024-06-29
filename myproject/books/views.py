from django.views.generic import ListView
from .models import Books
from .forms import BooksForm

class BooksListView(ListView):
  model = Books
  form_class = BooksForm
  template_name = 'books/index.html'