from django.shortcuts import render,get_object_or_404
from vendor.models import Vendor
from menu.models import Categry,FoodItem
from django.db.models import Prefetch

# Create your views here.


def listing(request):

    vendor = Vendor.objects.all()
    vendrList = vendor.count()

    context = {
        "vendors": vendor,
        "vendrList": vendrList
    }

    return render(request, 'marketplace/listing.html',context)


def vendordetail(request,slug):
    vendor =  get_object_or_404(Vendor, slug=slug)
    categry = Categry.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_available=True)
            ))
    
    context ={
        "vendors": vendor,
        'categories': categry
    }
    return render(request, 'marketplace/vendordetail.html',context)