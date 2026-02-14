from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book_now", views.book_now, name="book_now"),
    path("turf_details", views.turf_details, name="turf_details"),
    path("turf1_details", views.turf1_details, name="turf1_details"),
    path("turf2_details", views.turf2_details, name="turf2_details"),
    path("turf3_details", views.turf3_details, name="turf3_details"),
    path("turf4_details", views.turf4_details, name="turf4_details"),
    path("turf5_details", views.turf5_details, name="turf5_details"),
    path("turf6_details", views.turf6_details, name="turf6_details"),
    path("turf7_details", views.turf7_details, name="turf7_details"),
    path("turf8_details", views.turf8_details, name="turf8_details"),
    path("slot_details", views.slot_details, name="slot_details"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path('turfBilling', views.turfBilling, name='turfBilling'),
    path('orderHistory', views.orderHistory, name="orderHistory"),
    path('allBookings', views.allBookings, name="allBookings"),
    path('delete_booking/<int:id>', views.delete_booking, name="delete_booking"),
    path('success', views.success, name='success'),
    
    # Owner URLs
    path('owner/signup', views.owner_signup, name='owner_signup'),
    path('owner/login', views.owner_login, name='owner_login'),
    path('owner/dashboard', views.owner_dashboard, name='owner_dashboard'),
    path('owner/add-turf', views.add_turf, name='add_turf'),
    path('owner/edit-turf/<int:turf_id>', views.edit_turf, name='edit_turf'),
    path('owner/delete-turf/<int:turf_id>', views.delete_turf, name='delete_turf'),
    
    # Explore section
    path('explore', views.explore_turfs, name='explore_turfs'),
    path('turf/<int:turf_id>', views.dynamic_turf_details, name='dynamic_turf_details'),
    
    # Dynamic turf booking URLs
    path('turf/<int:turf_id>/book', views.dynamic_turf_booking, name='dynamic_turf_booking'),
    path('dynamic-turf-slots', views.dynamic_turf_slots, name='dynamic_turf_slots'),
    path('dynamic-turf-billing', views.dynamic_turf_billing, name='dynamic_turf_billing'),
]
