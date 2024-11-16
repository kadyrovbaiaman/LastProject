from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'ownerUser':
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.status == 'ownerUser'


class CheckOwnerHotel(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'занят' or 'забронирован':
            return False
        return True


class BookingPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'ownerUser':
            return False
        return True


class CheckRating(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_name:
            return True
        return False


class CheckOwnerRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.hotel_room.owner == request.user:
            return True
        return False


class CheckOwnBooking(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user_book == request.user:
            return True
        return False


class CheckImage(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True



