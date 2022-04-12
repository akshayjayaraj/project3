from django.urls import path
from apps import views

urlpatterns = [
path('',views.index),
path('1/',views.about),
path('2/',views.services),
path('3/',views.contact),
path('contact1/',views.contact1),
path('viewdata/',views.viewdata),
path('login/',views.login),
path('logout/',views.logout),
path('myprofile/',views.myprofile),
path('delete/',views.delete),
path('update/',views.update),
path('updateform/',views.updateform),
path('imageget/',views.imageget),
path('imageupload/',views.imageupload),
path('downloadtc/',views.downloadtc),
path('favactor/',views.favactor),
path('luckyno/',views.luckyno),









]