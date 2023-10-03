from django.urls import path
from main.views import show_main
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import add_item, subtract_item, delete_item, edit_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('create-item', create_item, name='create_item'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-item/<int:id>/', add_item, name='add_item'),
    path('subtract-item/<int:id>/', subtract_item, name='subtract_item'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
]