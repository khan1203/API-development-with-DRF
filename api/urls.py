from django.urls import path
from . import views

# Type-01: Manual Routing ------------------

urlpatterns = [
    path('students/', views.studentsView, name= 'studentsView'),
    path('students/<int:pk>/', views.studentDetailView, name='studentDetailView'),

    # path('employees/', views.EmployeesViewset.as_view(), name='employeesView'),
]

# Type-02: Default Routing -----------------

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employees')
router.register('blogs', views.BlogsViewset, basename='blogs')
router.register('comments', views.CommentViewset, basename='comments')
urlpatterns += router.urls