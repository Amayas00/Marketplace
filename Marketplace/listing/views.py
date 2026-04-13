from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewListingForm, EditListingForm
from .models import Category, Listing


def listings(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    condition = request.GET.get('condition', '')
    categories = Category.objects.all()
    items = Listing.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if condition:
        items = items.filter(condition=condition)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query))

    return render(request, 'listing/listings.html', {
        'listings': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'condition': condition,
        'condition_choices': Listing.CONDITION_CHOICES,
    })


def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    related = Listing.objects.filter(category=listing.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'listing/detail.html', {
        'listing': listing,
        'related_listings': related,
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user
            listing.save()
            return redirect('listing:detail', pk=listing.id)
    else:
        form = NewListingForm()

    return render(request, 'listing/form.html', {
        'form': form,
        'title': 'New Listing',
    })


@login_required
def edit(request, pk):
    listing = get_object_or_404(Listing, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing:detail', pk=listing.id)
    else:
        form = EditListingForm(instance=listing)

    return render(request, 'listing/form.html', {
        'form': form,
        'title': 'Edit Listing',
    })


@login_required
def delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk, created_by=request.user)
    listing.delete()
    return redirect('dashboard:index')


@login_required
def mark_sold(request, pk):
    listing = get_object_or_404(Listing, pk=pk, created_by=request.user)
    listing.is_sold = True
    listing.save()
    return redirect('dashboard:index')
