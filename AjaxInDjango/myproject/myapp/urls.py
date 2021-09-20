from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.index ),
    path('save',views.save_data,name="save" ),
    path('delete',views.delete_data, name="delete" ),
    path('edit',views.edit_data, name="edit" ),
]
