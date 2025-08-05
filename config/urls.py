from django.contrib import admin
from django.urls import path, include
from todo.views import (
    todo_list,
    todo_info,
    todo_create,
    todo_update,
    todo_delete
)
from todo.cb_views import (
    TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView,
    CommentDeleteView, CommentUpdateView, CommentCreateView
)
from users import views as user_views

urlpatterns = [
    # ======================
    # FBV URLs
    # ======================
    path('todo/', todo_list, name='todo_list'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),

    # ======================
    # CBV URLs
    # ======================
    path('cbv/todo/', TodoListView.as_view(), name='cbv_todo_list'),
    path('cbv/todo/create/', TodoCreateView.as_view(), name='cbv_todo_create'),
    path('cbv/todo/<int:pk>/', TodoDetailView.as_view(), name='cbv_todo_info'),
    path('cbv/todo/<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('cbv/todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),

    path('cbv/comment/<int:todo_id>/create/', CommentCreateView.as_view(), name='comment_create'),
    path('cbv/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('cbv/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),

    # ======================
    # Admin
    # ======================
    path('admin/', admin.site.urls),

    # ======================
    # Auth (Login / Logout)
    # ======================
    path('accounts/', include('django.contrib.auth.urls')),

    # 회원가입 및 사용자 정의 로그인
    path('accounts/login/', user_views.login, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]
