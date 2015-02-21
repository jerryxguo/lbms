import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from books.models import Collection
# Create your views here.
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'books/result.html'
    context_object_name = 'latest_book_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Collection.objects.order_by('title')

def index(request):
    return HttpResponse("Hello, world. You're at the books index.")