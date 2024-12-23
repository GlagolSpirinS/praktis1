    // Простая валидация на клиенте
    document.querySelector('form').addEventListener('submit', function(event) {
        let valid = true;

        // Очистить ошибки
        document.querySelectorAll('.text-danger').forEach(function(element) {
            element.textContent = '';
        });

        // Валидация имени
        let firstName = document.getElementById('first_name');
        if (firstName.value.trim() === '') {
            document.getElementById('first-name-error').textContent = 'Это поле обязательно';
            valid = false;
        }

        // Валидация фамилии
        let lastName = document.getElementById('last_name');
        if (lastName.value.trim() === '') {
            document.getElementById('last-name-error').textContent = 'Это поле обязательно';
            valid = false;
        }

        // Валидация остальных полей (username, email, password и т.д.)
        // ...

        if (!valid) {
            event.preventDefault();
        }
    });