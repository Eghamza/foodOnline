from vendor import models


def get_vendor(request):
    try:
     vendor = models.Vendor.objects.get(user=request.user)
    except:
       vendor = None


    return dict(vendor=vendor)
