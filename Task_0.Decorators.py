from datetime import datetime
import requests


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        res = func(*args, **kwargs)
        t_stop = datetime.now()
        execution_time = t_stop - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in {execution_time.seconds}s {milliseconds}ms")
        return res
    return wrapper


@measure_execution_time
def request():
    response = requests.get('https://yandex.ru/pogoda/moscow?ysclid=m8lotb8g6f775200345')
    if response.status_code == 200:
        return 'Запрос выполнен успешно', response.headers
    else:
        return 'Произошла ошибка:', response.status_code


print(*request())


def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user['role'] == 'admin':
            print('Доступ разрешен')
            res = func(user, *args, **kwargs)
            return res
        else:
            raise PermissionError('Доступ запрещен: требуется роль администратора.')
    return wrapper


@requires_admin
def delete_user(user, username_to_delete):
    return f"User {username_to_delete} has been deleted by {user['username']}."


admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}


print(delete_user(admin_user, 'Charlie'))
print(delete_user(regular_user, 'Charlie'))
