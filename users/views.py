from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from users.models import User, Department, Task, TaskAttachment, FileComment
import json
from django.http import JsonResponse, Http404
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='login')
def task(request):
    user = request.user
    tasks = Task.objects.filter(assigned_to=user)

    # Создайте пустой список для задач с их комментариями
    tasks_with_comments = []

    for task in tasks:
        # Получите комментарии для каждой задачи
        task_comments = FileComment.objects.filter(task=task)
        # Добавьте комментарии в задачу (не через присваивание, а как отдельное поле)
        tasks_with_comments.append({
            'task': task,
            'comments': task_comments
        })

    return render(request, 'tasks/task.html', {'tasks_with_comments': tasks_with_comments})

def profile(request, user_id):
    from django.shortcuts import get_object_or_404
    profile_user = get_object_or_404(User, id=user_id)
    return render(request, 'profile/profile.html', {'profile_user': profile_user})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid login or password")
    return render(request, 'login/login.html')

def registration(request):
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        first_name = request.POST.get('first_name')  # Имя
        last_name = request.POST.get('last_name')  # Фамилия
        gender = request.POST.get('gender')  # Пол
        avatar = request.FILES.get('avatar')

        # Проверка на уникальность username и email
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Имя пользователя уже занято.')
            return render(request, 'registration/registration.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email уже используется.')
            return render(request, 'registration/registration.html')

        # Валидация пароля
        if password != password_confirmation:
            messages.error(request, 'Пароли не совпадают.')
            return render(request, 'registration/registration.html')

        if len(password) < 6:
            messages.error(request, 'Пароль должен быть не менее 6 символов.')
            return render(request, 'registration/registration.html')

        # Проверка на выбор пола
        if not gender:
            messages.error(request, 'Пол обязателен для выбора.')
            return render(request, 'registration/registration.html')

        # Создание пользователя
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # Создание пользователя на основе модели CustomUser с добавлением пола
        фbstractгser = AbstractUser.objects.create(
            user=user,
            gender=gender,  # Добавляем поле gender
            avatar=avatar,  # Устанавливаем аватар, если был загружен
        )

        login(request, user)
        return redirect('home')

    return render(request, 'home/home.html')


def admin(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    departments = Department.objects.all()
    return render(request, 'admin/admin.html', {'users': users, 'tasks': tasks, 'departments': departments})

def staff(request):
    departments = Department.objects.all()
    return render(request, 'staff/staff.html', {'departments': departments})

def get_department_details(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return JsonResponse({
        'id': department.id,
        'name': department.name,
    })

def add_department(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if not name:
            return JsonResponse({'success': False, 'error': 'Name is required'}, status=400)

        # Create and save the department
        department = Department(name=name)
        department.save()
        return redirect('admin')

    return render(request, 'admin/admin.html')

def update_department(request, department_id):
    if request.method == 'POST':
        # Получаем объект отдела по ID
        department = get_object_or_404(Department, id=department_id)

        # Получаем новое имя отдела из запроса
        new_name = request.POST.get('name')

        if new_name:
            department.name = new_name  # Обновляем имя
            department.save()  # Сохраняем изменения в базе данных

            # Возвращаем успешный ответ
            return JsonResponse({'message': 'Department updated successfully!'}, status=200)
        else:
            # Если имя не передано, возвращаем ошибку
            return JsonResponse({'error': 'Name is required'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def delete_department(request, departments_id):
    if request.method == "DELETE":
        department = get_object_or_404(Department, id=departments_id)
        department.delete()
        return redirect('admin')

    return render(request, 'admin/admin.html')
def add_task(request):
    if request.method == "POST":
        task = Task()
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')

        user_id = request.POST.get('assigned_to')
        task.assigned_to = get_object_or_404(User, id=user_id)

        task.save()

        # Добавление сообщения об успехе
        messages.success(request, "Задание добавлено")

        # Редирект на страницу задач
        return redirect('tasks')

    return render(request, 'tasks/task.html')

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)

        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_status = request.POST.get('status')

        if new_title:
            task.title = new_title
            task.save()

        if new_description:
            task.description = new_description
            task.save()

        if new_status:
            task.status = new_status
            task.save()

        return redirect('tasks')
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
@login_required
def get_task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    return JsonResponse({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'status': task.status,
        'assigned_to': task.assigned_to.id if task.assigned_to else None,
    })

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')  # Возвращаем пользователя на страницу задач

@login_required
def add_comment(request, task_id):
    # Получаем задачу по ID
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        try:
            # Десериализуем JSON данные
            data = json.loads(request.body)

            # Получаем комментарий из данных
            comment_text = data.get('comment', '').strip()

            if not comment_text:
                return JsonResponse({'success': False, 'message': 'Комментарий не может быть пустым.'})

            # Создаем новый комментарий
            comment = FileComment.objects.create(
                user=request.user,
                task=task,
                comment=comment_text
            )

            # Возвращаем успешный ответ с данными нового комментария
            return JsonResponse({
                'success': True,
                'user_first_name': comment.user.first_name,
                'user_last_name': comment.user.last_name,
                'comment': comment.comment,
            })

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Ошибка при обработке данных.'})

    return JsonResponse({'success': False, 'message': 'Неверный метод запроса.'})

@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file') and request.POST.get('task_id'):
        task_id = request.POST['task_id']
        task = Task.objects.get(id=task_id)

        if not task:
            return JsonResponse({'error': 'Task not found'}, status=404)

        # Check if the user is assigned to the task or an admin
        if task.assigned_to != request.user:
            raise PermissionDenied

        uploaded_file = request.FILES['file']
        attachment = TaskAttachment.objects.create(task=task, file=uploaded_file)

        return JsonResponse({'message': 'File uploaded successfully', 'file_url': attachment.file.url})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.status = 'completed'
        task.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def get_user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Safely check if the user has a department
    department_name = user.department.name if user.department else None

    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'gender': user.gender,
        'department': department_name,  # This will be None if no department
        'position': user.position
    })


def update_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)

        # Get the data from the request
        new_username = request.POST.get('username')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_email = request.POST.get('email')
        new_gender = request.POST.get('gender')
        new_department_id = request.POST.get('department')
        new_position = request.POST.get('position')

        # Update username if provided
        if new_username:
            user.username = new_username
            user.save()

        # Update first name if provided
        if new_first_name:
            user.first_name = new_first_name
            user.save()

        # Update last name if provided
        if new_last_name:
            user.last_name = new_last_name
            user.save()

        # Update email if provided
        if new_email:
            user.email = new_email
            user.save()

        # Update gender if provided
        if new_gender:
            user.gender = new_gender
            user.save()

        # Update department if provided
        if new_department_id:
            department = Department.objects.get(id=new_department_id)
            user.department = department
            user.save()

        # Update position if provided
        if new_position:
            user.position = new_position
            user.save()

    return redirect('admin')

