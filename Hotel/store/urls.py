from django.urls import path,include
from .views import *

from rest_framework import routers

routers=routers.DefaultRouter()
routers.register(r'user',UserProfileViewSet, basename='user-list'),
routers.register(r'hotels',HotelListViewSet, basename='hotel-list'),
routers.register(r'hotels-detail',HotelDetailViewSet, basename='hotel-detail'),
routers.register(r'hotel_photos',HotelPhotosViewSet, basename='hotel_photos-list'),
routers.register(r'room',RoomListViewSet, basename='room-list'),
routers.register(r'room-detail',RoomDetailViewSet, basename='room-detail'),
routers.register(r'room_photos',RoomPhotosViewSet, basename='room_photos-list'),
routers.register(r'booking',BookingViewSet, basename='booking-list'),
routers.register(r'rating',RatingViewSet, basename='rating-list'),


urlpatterns = [
    path('',include(routers.urls))

]
