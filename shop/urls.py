
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/',views.about, name="About"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('tracker/',views.tracker,name="tracker"),
    path('productView/',views.productview,name="search"),
    path('checkout/',views.checkout,name="search")

]