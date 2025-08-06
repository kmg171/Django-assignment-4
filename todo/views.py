from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.html import strip_tags  # Summernote 내용 검색 개선 시 사용

from todo.forms import TodoForm, TodoUpdateForm
from todo.models import Todo


@login_required
def todo_list(request):
    # 현재 로그인한 사용자의 Todo만 표시
    todo_list = Todo.objects.filter(user=request.user).order_by('-created_at')

    # 검색 기능
    q = request.GET.get('q')
    if q:
        # HTML 태그 제거 후 검색 정확도 높이기
        todo_list = todo_list.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q)
        )

    # 페이지네이션
    paginator = Paginator(todo_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'todo/todo_list.html', {'page_obj': page_obj})


@login_required
def todo_info(request, todo_id):
    # 해당 사용자의 Todo 가져오기
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo/todo_info.html', {'todo': todo})


@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)  # 이미지 업로드 가능
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    else:
        form = TodoForm()

    return render(request, 'todo/todo_create.html', {'form': form})


@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)

    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, request.FILES, instance=todo)  # 이미지 업로드 가능
        if form.is_valid():
            form.save()
            return redirect(reverse('todo_info', kwargs={'todo_id': todo.pk}))
    else:
        form = TodoUpdateForm(instance=todo)

    return render(request, 'todo/todo_update.html', {'form': form})


@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect(reverse('todo_list'))
