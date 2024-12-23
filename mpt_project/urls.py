from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf.urls.static import static
from users import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_menu/', views.admin, name='admin'),
    path('add-task/', views.add_task, name='add_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/edit/<int:task_id>/', views.add_task, name='edit_task'),
    path('staff', views.staff, name='staff'),
    path('task', views.task, name='tasks'),
    path('add-department', views.add_department, name='add_department'),
    path('department/update/<int:department_id>/', views.update_department, name='update_department'),
    path('api/update/<int:user_id>/', views.update_user, name='update_user'),
    path('api/users/<int:user_id>/', views.get_user_details, name='get_user_details'),
    path('departments/delete/<int:departments_id>/', views.delete_department, name='delete_department'),
    path('api/tasks/<int:task_id>/', views.get_task_details, name='get_task_details'),
    path('api/departmentId/<int:department_id>/', views.get_department_details, name='get_department_details'),
    path('api/tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('add_comment/<int:task_id>/', views.add_comment, name='add_comment'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('login', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration', views.registration, name='registration'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
