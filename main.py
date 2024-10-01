# Заранее заданный правильный пароль
correct_password = "PSPtop"

# Запрос пароля у пользователя
user_password = input("Введите пароль: ")

# Проверка пароля
if user_password == correct_password:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")