from django.shortcuts import render
from django.http import HttpResponse


# listings apps

def listings_index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
