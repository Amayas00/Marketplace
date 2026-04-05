from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Category

def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)

    return render(request, 'listing/detail.html', {
        'listing': listing,
    })
