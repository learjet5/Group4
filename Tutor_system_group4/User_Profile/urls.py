# 引入path
from django.urls import path, include
from . import views

app_name = 'User_Profile'
urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('register/', views.register, name='register'),
	path('student_profile_update/<int:id>/', views.student_profile_update, name='student_profile_update'),
	path('teacher_profile_update/<int:id>/', views.teacher_profile_update, name='teacher_profile_update'),
]
