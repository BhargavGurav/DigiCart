from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('profile/<str:name>', views.profile, name='profile'),
    path('delete/<int:id>', views.delete_item, name='delete'),
    path('buy/', views.buy, name='buy'),
    path('history/', views.history, name='history'),
    path('history_page/', views.history_page, name='history_page'),
    path('delete_history/', views.delete_history, name='delete_history'),
    path('save_cart_items/', views.save_cart_items, name='save_cart_items'),
    # path('add_cart/<str:item_cat><str:item>', views.add_cart, name='add_cart'),
]
