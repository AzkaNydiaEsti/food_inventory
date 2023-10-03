from django.urls import path
from main.views import show_main, add_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, inc_amount, dec_amount, delete_item, edit_item 
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item/', add_item, name='add_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dec_amount/<int:id>/', views.dec_amount, name='dec_amount'),
    path('inc_amount/<int:id>/', views.inc_amount, name='inc_amount'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
]