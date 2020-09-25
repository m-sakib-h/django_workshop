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
    seller_of_month= Realtor.objects.filter(is_mvp=True).first()
    # Realtor.objects.filter(is_mvp=True) ==>select * from Realtor where is_mvp=True

    # seller_of_month= Realtor.objects.filter(is_mvp=True)

    # if len(seller_of_month)>1:
    #     seller_of_month=seller_of_month[0]
    # print(seller_of_month)

    # team = Realtor.objects.none()

    context = {
        'team': team,
        'seller_of_month': seller_of_month
    }
    return render(request, 'pages/about.html', context)
