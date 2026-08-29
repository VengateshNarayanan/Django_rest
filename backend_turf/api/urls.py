from . import views
from django.urls import path

urlpatterns = [

    path('Turf',views.TurfLC.as_view(),name='turf'),
    path('Turf/<int:pk>',views.TurfRUD.as_view(),name='turf'),

    
]


