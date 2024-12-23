import random

from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название отдела")

def get_default_avatar():
    DEFAULT_AVATARS = [
        'standard_avatars/1.svg',
        'standard_avatars/2.svg',
        'standard_avatars/3.svg',
        'standard_avatars/4.svg',
        'standard_avatars/5.svg',
        'standard_avatars/6.svg',
        'standard_avatars/7.svg',
        'standard_avatars/8.svg',
        'standard_avatars/9.svg',
        'standard_avatars/10.svg',
        'standard_avatars/11.svg',
        'standard_avatars/12.svg',
        'standard_avatars/13.svg',
        'standard_avatars/14.svg',
        'standard_avatars/15.svg',
        'standard_avatars/16.svg',
        'standard_avatars/17.svg',
        'standard_avatars/18.svg',
        'standard_avatars/19.svg',
        'standard_avatars/20.svg',
        'standard_avatars/21.svg',
        'standard_avatars/22.svg',
        'standard_avatars/23.svg',
        'standard_avatars/24.svg',
    ]
    return random.choice(DEFAULT_AVATARS)

class User(AbstractUser):
    GENDER_CHOICES = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
    )

    SHIFT_CHOICES = (
        ('Дневная смена', 'Дневная смена'),
        ('Вечерняя смена', 'Вечерняя смена'),
        ('Ночная смена', 'Ночная смена'),
        ('Сменный график', 'Сменный график'),
        ('Скользящий график', 'Скользящий график'),
        ('Половинная смена', 'Половинная смена'),
        ('Гибкий график', 'Гибкий график'),
        ('Ротационная смена', 'Ротационная смена'),
    )

    POSITION_CHOICES = (
        ('Руководитель отдела корпоративных финансов', 'Руководитель отдела корпоративных финансов'),
        ('Менеджер по слияниям и поглощениям', 'Менеджер по слияниям и поглощениям'),
        ('Финансовый аналитик', 'Финансовый аналитик'),
        ('Специалист по оценке бизнеса', 'Специалист по оценке бизнеса'),
        ('Специалист по структурированию сделок', 'Специалист по структурированию сделок'),
        ('Специалист по финансовому моделированию', 'Специалист по финансовому моделированию'),
        ('Руководитель отдела инвестиционного банкинга', 'Руководитель отдела инвестиционного банкинга'),
        ('Аналитик по инвестиционному банкингу', 'Аналитик по инвестиционному банкингу'),
        ('Менеджер по работе с клиентами', 'Менеджер по работе с клиентами'),
        ('Специалист по рынку капитала', 'Специалист по рынку капитала'),
        ('Специалист по IPO', 'Специалист по IPO'),
        ('Специалист по структурированным финансовым продуктам', 'Специалист по структурированным финансовым продуктам'),
        ('Руководитель отдела управления активами', 'Руководитель отдела управления активами'),
        ('Портфельный менеджер', 'Портфельный менеджер'),
        ('Аналитик по инвестициям', 'Аналитик по инвестициям'),
        ('Специалист по риск-менеджменту', 'Специалист по риск-менеджменту'),
        ('Специалист по финансовому планированию', 'Специалист по финансовому планированию'),
        ('Специалист по работе с клиентами', 'Специалист по работе с клиентами'),
        ('Руководитель отдела частного банкинга', 'Руководитель отдела частного банкинга'),
        ('Частный банкир', 'Частный банкир'),
        ('Специалист по финансовому планированию', 'Специалист по финансовому планированию'),
        ('Специалист по инвестициям', 'Специалист по инвестициям'),
        ('Специалист по кредитованию', 'Специалист по кредитованию'),
        ('Менеджер по работе с клиентами', 'Менеджер по работе с клиентами'),
        ('Руководитель отдела риск-менеджмента', 'Руководитель отдела риск-менеджмента'),
        ('Менеджер по управлению рисками', 'Менеджер по управлению рисками'),
        ('Специалист по кредитному риску', 'Специалист по кредитному риску'),
        ('Специалист по рыночному риску', 'Специалист по рыночному риску'),
        ('Специалист по операционному риску', 'Специалист по операционному риску'),
        ('Специалист по моделированию рисков', 'Специалист по моделированию рисков'),
        ('Руководитель отдела финансового контроля', 'Руководитель отдела финансового контроля'),
        ('Финансовый контролер', 'Финансовый контролер'),
        ('Бухгалтер', 'Бухгалтер'),
        ('Аналитик финансовой отчетности', 'Аналитик финансовой отчетности'),
        ('Специалист по налогам', 'Специалист по налогам'),
        ('Специалист по внутреннему аудиту', 'Специалист по внутреннему аудиту'),
        ('Руководитель отдела информационных технологий', 'Руководитель отдела информационных технологий'),
        ('Менеджер по информационным технологиям', 'Менеджер по информационным технологиям'),
        ('Разработчик программного обеспечения', 'Разработчик программного обеспечения'),
        ('Системный аналитик', 'Системный аналитик'),
        ('Специалист по информационной безопасности', 'Специалист по информационной безопасности'),
        ('Администратор баз данных', 'Администратор баз данных'),
        ('Руководитель отдела кадров', 'Руководитель отдела кадров'),
        ('Менеджер по персоналу', 'Менеджер по персоналу'),
        ('Специалист по подбору персонала', 'Специалист по подбору персонала'),
        ('Специалист по обучению и развитию', 'Специалист по обучению и развитию'),
        ('Специалист по компенсациям и льготам', 'Специалист по компенсациям и льготам'),
        ('Специалист по трудовым отношениям', 'Специалист по трудовым отношениям'),
        ('Руководитель отдела маркетинга и коммуникаций', 'Руководитель отдела маркетинга и коммуникаций'),
        ('Менеджер по маркетингу', 'Менеджер по маркетингу'),
        ('Специалист по брендингу', 'Специалист по брендингу'),
        ('Специалист по цифровому маркетингу', 'Специалист по цифровому маркетингу'),
        ('Специалист по PR', 'Специалист по PR'),
        ('Специалист по контенту', 'Специалист по контенту'),
        ('Руководитель отдела клиентского обслуживания', 'Руководитель отдела клиентского обслуживания'),
        ('Менеджер по работе с клиентами', 'Менеджер по работе с клиентами'),
        ('Специалист по клиентскому обслуживанию', 'Специалист по клиентскому обслуживанию'),
        ('Специалист по обработке заявок', 'Специалист по обработке заявок'),
        ('Специалист по технической поддержке', 'Специалист по технической поддержке'),
        ('Специалист по работе с жалобами', 'Специалист по работе с жалобами'),
    )

    # Пол
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name="Пол", null=True)

    # Отдел
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Отдел")

    # Должность
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, verbose_name="Должность", null=True)

    # Смена
    shift = models.CharField(max_length=100, choices=SHIFT_CHOICES, verbose_name="Смена", null=True)

    # Аватар
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар", default=get_default_avatar)



class Task(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новое'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
        ('cancelled', 'Отменено'),
    )

    title = models.CharField(max_length=120, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name="Назначено")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title


class FileComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', verbose_name="Задача", null=True)
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата комментария")

    def __str__(self):
        return f"Комментарий от {self.user.username} на задачу {self.task.title}"

class TaskAttachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments', verbose_name="Задача", null=True)
    file = models.FileField(upload_to='task_attachments/', verbose_name="Файл")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"Файл для задания {self.task.title} - {self.file.name}"
