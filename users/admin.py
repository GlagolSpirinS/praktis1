from django.contrib import admin

from users.models import User, Task, Department, FileComment, TaskAttachment

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Department)
admin.site.register(FileComment)
admin.site.register(TaskAttachment)