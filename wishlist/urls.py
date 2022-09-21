from django.urls import path
from wishlist.views import show_wishlist 
from wishlist.views import show_json
from wishlist.views import show_xml # Customize to the name of the function created
from wishlist.views import show_json_by_id  # Customize the name of the function created
app_name = 'wishlist'
app_name = 'show_xml'
app_name = 'show_json'
app_name = 'show_json_by_id'
urlpatterns = [
    
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), # Customize the name of the function created
    path('json/123', show_json_by_id, name='show_json_by_id'),
]