import pytest
import requests
import json


@pytest.fixture(scope='session')
# Предусловия, создание поользователя и сохранием АЙДИ
def setUp():
    print("Start testing")
    body = json.dumps({
        "data": {"color": 'white', "size": 'BUG'},
        "name": 'Test_object'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', data=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    # Удаляем сразу, чтобы не мусорить
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print("Testing completed")


# Тест на нахождение нужного пользователя
def test_one_post(setUp):
    print("before test")
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{setUp}')
    assert response.status_code == 200, 'Статус не верный'
    assert response.json()['id'] == setUp, 'ID объекта не совпадает'
    print("after test")

# Изменение данных
def test_put_posts(setUp):
    print("before test")
    body = json.dumps({
        "data": {"color": 'white', "size": 'BUG'},
        "name": 'Test_77'
    })
    headers = {'Content-Type': 'application/json'}
    response = (requests.put(
        f'http://objapi.course.qa-practice.com/object/{setUp}',
        data=body,
        headers=headers
    ))
    assert response.status_code == 200
    assert response.json()['name'] == "Test_77", 'Имя не изменен'
    print("after test")

# Изменение данных
def test_patch_posts(setUp):
    print("before test")
    body = json.dumps({
        "data": {"color": 'green', "size": 'BUG'}
    })
    headers = {'Content-Type': 'application/json'}
    response = (requests.patch(f'http://objapi.course.qa-practice.com/object/{setUp}',
                               data=body, headers=headers))
    assert response.status_code == 200
    assert response.json()['data']['color'] == 'green', 'Цвет не изменен'
    print("after test")

# Удаление пользователя
def test_delete_posts(setUp):
    response = (requests.delete(f'http://objapi.course.qa-practice.com/object/{setUp}'))
    assert response.status_code == 200, 'Объект не найден'


# Вывод всех пользоваетелей
def test_all_posts():
    print("before test")
    response = requests.get('http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200
    assert len(response.json()) == 1, 'Not all posts returned'
    print("after test")


# Добавление пользователей
def test_post_a_posts():
    print("before test")
    body = json.dumps({
        "data": {"color": 'white', "size": 'BUG'},
        "name": 'Test_77'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', data=body, headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == 'Test_77'
    post_id = response.json()['id']
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    print("after test")
