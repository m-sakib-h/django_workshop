from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


# pages app views

def index(request):
    latest = Listing.objects.order_by('-list_date')[:3]  # 0,1,2 object
    # latest=Listing.objects.order_by('-list_date') ==>select * from Listing  order by list_date DESC

    context = {
        'latest': latest
    }
    return render(request, 'pages/index.html', context)


def about(request):
    team = Realtor.objects.order_by('-contact_date')[:3]
    # team = Realtor.objects.none()

    context = {
        'team': team
    }
    return render(request, 'pages/about.html', context)
