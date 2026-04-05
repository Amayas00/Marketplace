from django.shortcuts import render
from listing.models import Category, Listing


def index(request):
    featured = Listing.objects.filter(is_sold=False, is_featured=True)[0:3]
    recent = Listing.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'featured_listings': featured,
        'recent_listings': recent,
    })

def contact(request):
    return render(request, 'core/contact.html')