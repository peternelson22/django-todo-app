from django.urls import path
from .views import TaskDetail, TaskList, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterForm
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterForm.as_view(), name='register'),

]