from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Listing
from listings.model_choices import state_choices, bedroom_choices, price_choices


# from .models import * #Bad Practise
# listing app

def listings_index(request):
    listing_ = Listing.objects.all()  # [:1]    # Suppose 6 listing
    # list_=Listing.objects.none()

    paginator = Paginator(listing_,
                          2)  # Per_Page 2, Page 3        Paginator is a Class & paginator is a object or reference
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
    # quires=request.GET.get
    # print(quires)
    # city=request.GET.get('city') #Don't do this
    get_method = request.GET.copy()         #get method theke anar jonno copy kora abar send korci jeikhana show korta chai
                                        #eijonno context er vitor dya pass kora dici
    keywords = get_method.get('keywords') or None
    city = get_method.get('city') or None
    # print(get_method.get('keywords'))
    listings_list = Listing.objects.filter(is_published=True).all()

    # keywords
    if keywords is not None:
        keyword = get_method.get('keywords')
        listings_list = listings_list.filter(desc__icontains=keyword)  # django=Django,dj,go
        # listings_list=listings_list.filter(description__iexact=keyword)  # Django==Django

    # city
    if city is not None:
        city = get_method.get('city')
        listings_list = listings_list.filter(city__icontains=city)
    # state
    if 'state' in get_method:
        st = get_method.get('state')
        listings_list = listings_list.filter(state__iexact=st)
    # bedrooms
    if 'bedrooms' in get_method:
        bedrooms = get_method.get('bedrooms')
        listings_list = listings_list.filter(bedrooms__lte=bedrooms)
    # price
    if 'price' in get_method:
        price = get_method.get('price')
        listings_list = listings_list.filter(price__lte=price)
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'get_method': get_method,
        'listing_list': listings_list,
    }
    return render(request, 'listings/search.html', context)
