from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from todo.views import (
    todo_list,
    todo_info,
    todo_create,
    todo_update,
    todo_delete
)
from users import views as user_views

urlpatterns = [
    # Todo 앱 URL (기존 경로)
    path('todo/', todo_list, name='todo_list'),
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),

    # Todo 앱 URL (cbv 접두사 추가)
    path('cbv/todo/', todo_list, name='cbv_todo_list'),
    path('cbv/todo/create/', todo_create, name='cbv_todo_create'),
    path('cbv/todo/<int:todo_id>/', todo_info, name='cbv_todo_info'),
    path('cbv/todo/<int:todo_id>/update/', todo_update, name='cbv_todo_update'),
    path('cbv/todo/<int:todo_id>/delete/', todo_delete, name='cbv_todo_delete'),

    # 관리자 페이지
    path('admin/', admin.site.urls),

    # Summernote URL
    path('summernote/', include('django_summernote.urls')),

    # Django 기본 로그인/로그아웃 URL
    path('accounts/', include('django.contrib.auth.urls')),

    # 회원가입 (사용자 정의)
    path('accounts/signup/', user_views.sign_up, name='signup'),

    # 사용자 정의 로그인 (필요하면 경로 변경)
    path('accounts/custom-login/', user_views.login, name='custom_login'),
]

# 개발 환경에서 media 파일 접근 허용
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
