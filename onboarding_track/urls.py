from django.urls import path
from . import views

urlpatterns = [
    

    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('Employee_list/',views.EmployeeListView.as_view(),name='Employee_list'),
    
    path('add_record/',views.add_record,name='add_record'),
    path('record/<int:pk>',views.Employee_record,name='record'),
    path('showrecords/',views.show_reocrd,name='allrecords'),
   path('mark_onboarded/<int:pk>/', views.mark_onboarded, name='maonboarded'),
   path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
]