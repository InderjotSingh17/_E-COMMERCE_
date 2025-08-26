from django.urls import path
from . import views

urlpatterns = [
	path('', views.index,name="home"),
	path('about/', views.about,name="about"),
	path('contact/', views.contact,name="contact"),
	path('checkout/', views.checkout,name="checkout"),
	path('handlerequest/', views.handlerequest,name="handlerequest"),
	path('profile/', views.profile,name="profile"),
    path('rate/<int:product_id>/', views.rate_product, name='rate_product'),
]