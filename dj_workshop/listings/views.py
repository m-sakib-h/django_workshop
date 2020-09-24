from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Listing


# from .models import * #Bad Practise
# listing app

def listings_index(request):
    listing_ = Listing.objects.all()  # [:1]    # Suppose 6 listing
    # list_=Listing.objects.none()

    paginator = Paginator(listing_, 2)  # Per_Page 2, Page 3        Paginator is a Class & paginator is a object or reference
    page = request.GET.get('page', 1)  # By_Default kon page show korba
    # page = request.GET.get('p', 1)  # By_Default kon page show korba

    try:
        listing_ = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        listing_ = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        listing_ = paginator.page(paginator.num_pages)

    context = {
        'listing_list': listing_
    }

    return render(request, 'listings/listings.html', context)
    # return render(request,'listings/listings.html', {'listing_list': listing_list})


def listing(request, listing_id):
    listing_ = Listing.objects.get(id=listing_id)  # 1 ti id show korar jonno .get
    return render(request, 'listings/listing.html', {'listing': listing_})


def search(request):
    return render(request, 'listings/search.html')
