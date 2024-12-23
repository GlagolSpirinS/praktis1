/**
 * Получение CSRF токена из cookies
 */
function getCSRFToken() {
    const csrfToken = document.cookie
        .split(';')
        .find(cookie => cookie.trim().startsWith('csrftoken='));
    return csrfToken ? csrfToken.split('=')[1] : '';
}

/**
 * Добавление комментария к задаче
 * @param {number} taskId - ID задачи
 */
function addComment(taskId) {
    const commentInput = document.getElementById(`comment-input-${taskId}`);
    const commentText = commentInput.value.trim();

    if (!commentText) {
        alert("Комментарий не может быть пустым.");
        return;
    }

    fetch(`/add_comment/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({ comment: commentText })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Очистим поле ввода
                commentInput.value = '';

                // Добавляем новый комментарий в список комментариев
                const commentList = document.getElementById(`comments-list-${taskId}`);
                const newComment = document.createElement("div");
                newComment.className = "mb-2";
                newComment.innerHTML = `
                    <img src="${data.user_avatar}" class="rounded-circle me-3" width="30" alt="Аватар">
                    ${data.user_first_name} ${data.user_last_name}: ${data.comment}
                `;
                commentList.appendChild(newComment);
            } else {
                alert(data.message || "Не удалось добавить комментарий. Попробуйте снова.");
            }
        })
        .catch(() => alert("Ошибка при добавлении комментария. Проверьте соединение."));
}

/**
 * Загрузка файла для задачи
 * @param {number} taskId - ID задачи
 */
function uploadFile(taskId) {
    const fileInput = document.getElementById(`file-input-${taskId}`);
    const file = fileInput.files[0];

    if (!file) {
        alert("Пожалуйста, выберите файл для загрузки.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('task_id', taskId);

    fetch('/upload-file/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken()
        },
        body: formData
    })
        .then(response => {
            if (response.ok) {
                alert("Файл успешно загружен.");
                location.reload(); // Обновляем страницу для отображения нового файла
            } else {
                alert("Ошибка загрузки файла. Попробуйте снова.");
            }
        })
        .catch(() => alert("Ошибка при загрузке файла. Проверьте соединение."));
}

/**
 * Завершение задачи
 * @param {number} taskId - ID задачи
 */
function completeTask(taskId) {
    fetch(`/tasks/complete/${taskId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    })
        .then(response => {
            if (response.ok) {
                alert("Задача завершена!");
                location.reload(); // Перезагрузка страницы для обновления статуса
            } else {
                alert("Не удалось завершить задачу. Попробуйте снова.");
            }
        })
        .catch(() => alert("Ошибка при завершении задачи. Проверьте соединение."));
}
