from django.shortcuts import render,redirect
from .models import Book
from reportlab.pdfgen import canvas
from django.shortcuts import redirect,render
from .forms import BookForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=BookForm()
    return render(request,'create_user_profile.html',{'form':form})

import csv
from django.http import HttpResponse
def generate_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="book_catalog.csv"'
    writer=csv.writer(response)
    writer.writerow(['Title','Author','Publication Year'])
    books = Book.objects.all()
    for book in books:
        writer.writerow([book.title,book.author,book.publication_year])
    return response
