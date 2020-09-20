from django.shortcuts import render
from .models import Listing
#from .models import * #Bad Practise
#listing app

def listings_index(request):
    listing_list=Listing.objects.all() [:1]
    #list_=Listing.objects.none()

    context={
        'listing_list': listing_list,
        #'list':list_,
    }

    return render(request,'listings/listings.html', context)
    # return render(request,'listings/listings.html', {'listing_list': listing_list})

def listing(request, listing_id):
    listing_=Listing.objects.get(id=listing_id)     # 1 ti id show korar jonno .get
    return render(request, 'listings/listing.html', {'listing': listing_} )

def search(request):
    return render(request,'listings/search.html')