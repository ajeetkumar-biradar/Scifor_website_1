# carrer/admin_urls.py
from django.urls import path
from . import views
from .views import (
    admin_dashboard,
    admin_job_list,
    admin_job_add,
    admin_job_edit,
    admin_job_delete,
    admin_application_list,
    admin_application_add,
    admin_application_edit,
    admin_application_delete,
    admin_login,
    admin_logout
)

urlpatterns = [
    path('login/', admin_login, name='admin_login'),
    path('logout/', admin_logout, name='admin_logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('jobs/', views.admin_job_list, name='admin_job_list'),
    path('jobs/add/', views.admin_job_add, name='admin_job_add'),
    path('jobs/edit/<int:pk>/', views.admin_job_edit, name='admin_job_edit'),
    path('jobs/delete/<int:pk>/', views.admin_job_delete, name='admin_job_delete'),
    path('applications/', views.admin_application_list, name='admin_application_list'),
    path('applications/add/', views.admin_application_add, name='admin_application_add'),
    path('applications/edit/<int:pk>/', views.admin_application_edit, name='admin_application_edit'),
    path('applications/delete/<int:pk>/', views.admin_application_delete, name='admin_application_delete'),
]


