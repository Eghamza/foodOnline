from django.shortcuts import render

# Create your views here.


def listing(request):
    return render(request, 'marketplace/listing.html')

