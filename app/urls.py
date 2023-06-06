from django.urls import path
from .views import *

urlpatterns = [
	path('<int:pk>/', BookDetail.as_view(), name='post_detail'),
	path('', BookList.as_view(), name='post_list')
]