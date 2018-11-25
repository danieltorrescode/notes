from django.contrib import admin
from django.urls import path
from . import views
from apps.notes.views import *
app_name = 'notes'

urlpatterns = [
	path('sign_up/', register.as_view(), name='sign_up'),
	#
	path('log_in/', log_in, name='log_in'),
	#
	path('log_out/', log_out, name='log_out'),
	#
	path('', views.index, name='index'),
	# ex: /polls/5/
	path('<int:id>/', views.detail, name='detail'),
	#
	path('category/create/',category_create.as_view(), name='category_create'),
	#
	path('category/list/',category_list.as_view(), name='category_list'),
	#
	path('category/update/<int:pk>/',category_update.as_view(), name='category_update'),
	#
	path('category/delete/<int:pk>/',category_delete.as_view(), name='category_delete'),
	#
	path('tag/create/',tag_create, name='tag_create'),
	#
	path('tag/list/',tag_list, name='tag_list'),
	#
	path('tag/update/<int:pk>/',tag_update, name='tag_update'),
	#
	path('tag/delete/<int:pk>/',tag_delete, name='tag_delete'),
	#
	path('note/create/',note_create.as_view(), name='note_create'),
	#
	path('note/list/',note_list.as_view(), name='note_list'),
	#
	path('note/update/<int:pk>/',note_update.as_view(), name='note_update'),
	#
	path('note/delete/<int:pk>/',note_delete.as_view(), name='note_delete'),
	#
	path('note/detail/<int:pk>/',note_detail.as_view(), name='note_detail'),
]
