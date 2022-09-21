from django.shortcuts import render
from wishlist.models import ItemWishlist
from django.http import HttpResponse
from django.core import serializers
data_wishlist_item = ItemWishlist.objects.all()
data1 = ItemWishlist.objects.all()
data2 = ItemWishlist.objects.all()
data = ItemWishlist.objects.filter(pk=id)
context = {
    'list_item' : data,
    'list_item': data_wishlist_item,
    'list_item': data1,
    'list_item': data2,
    'name': 'Julian Justin Orvino'
    
}

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)
def show_xml(request):
   
    
    return HttpResponse(serializers.serialize("xml", data1), content_type="application/xml")
    
def show_json(request):
    
    return HttpResponse(serializers.serialize("json", data2), content_type="application/json")
def show_json_by_id(request):
    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
