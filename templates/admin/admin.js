function deleteTask(taskId) {
    if (confirm("Are you sure you want to delete this task?")) {
        fetch(`/task/${taskId}/delete/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken() // Убедитесь, что CSRF-токен включён
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Task successfully deleted!');
                // Удаляем строку из таблицы
                document.getElementById(`task-row-${taskId}`).remove();
            } else {
                alert('Failed to delete task: ' + (data.error || 'Unknown error'));
            }
        });
    }
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function editTaskModal(taskId) {
    // Fetch task details via API
    fetch(`/api/tasks/${taskId}/`)
        .then(response => response.json())
        .then(data => {
            // Populate the modal fields
            document.getElementById('editTaskTitle').value = data.title;
            document.getElementById('editTaskDescription').value = data.description;
            document.getElementById('editTaskStatus').value = data.status;
            document.getElementById('editTaskAssignedTo').value = data.assigned_to;

            // Update form action to point to the update endpoint
            const form = document.getElementById('editTaskForm');
            form.action = `/api/tasks/update/${taskId}/`;
        })
        .catch(error => console.error('Error fetching task details:', error));
}

function editDepartmentModal(departmentId) {
    fetch(`/api/departmentId/${departmentId}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('editDepartmentName').value = data.name;
            const form = document.getElementById('editDepartmentForm');
            form.onsubmit = function(event) {
                event.preventDefault();

                const newName = document.getElementById('editDepartmentName').value;
                const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                fetch(`/department/update/${departmentId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrfToken,
                    },
                    body: `name=${encodeURIComponent(newName)}`
                })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        alert(data.message);
                        location.reload();
                    } else {
                        alert(data.error);
                    }
                })
                .catch(error => console.error('Error updating department:', error));
            };
        })
        .catch(error => console.error('Error fetching department details:', error));
}

function deleteDepartment(id) {
    if (confirm("Вы уверены, что хотите удалить этот отдел?")) {
        fetch(`/departments/delete/${id}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCSRFToken(),
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            if (response.ok) {
                alert("Отдел успешно удален.");
                document.getElementById(`department-row-${id}`).remove(); // Remove the row from the table
            } else {
                alert("Ошибка при удалении отдела.");
            }
        })
    }
}

function editUserModal(userId) {
    // Fetch task details via API
    fetch(`/api/users/${userId}/`)
        .then(response => response.json())
        .then(data => {
            // Populate the modal fields
            document.getElementById('editUsername').value = data.username;
            document.getElementById('editFirstName').value = data.first_name;
            document.getElementById('editLastName').value = data.last_name;
            document.getElementById('editEmail').value = data.email;
            document.getElementById('editGender').value = data.gender;
            document.getElementById('editDepartment').value = data.department;
            document.getElementById('editPosition').value = data.position;

            // Update form action to point to the update endpoint
            const form = document.getElementById('editUserForm');
            form.action = `/api/update/${userId}/`;
        })
        .catch(error => console.error('Error fetching task details:', error));
}
