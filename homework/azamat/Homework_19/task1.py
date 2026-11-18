import requests
import json


def all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) == 3, 'Not all posts returned'


def post_posts():
    body = json.dumps({
        "data": {"color": 'white', "size": 'BUG'},
        "name": 'Test_object'
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', data=body, headers=headers)
    assert response.status_code == 200, 'Статус не верный'
    return response.json()['id']


def one_posts(post_id):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    assert response['id'] == post_id, 'Айди не совпадают'


def put_posts(post_id):
    body = json.dumps({
        "data": {"color": 'white', "size": 'BUG'},
        "name": 'Test_77'
    })
    headers = {'Content-Type': 'application/json'}
    response = (requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        data=body,
        headers=headers
    ).json())
    assert response['name'] == u'Test_77', 'Имя не изменен'


def patch_posts(post_id):
    body = json.dumps({
        "data": {"color": 'green', "size": 'BUG'}
    })
    headers = {'Content-Type': 'application/json'}
    response = (requests.patch(f'http://objapi.course.qa-practice.com/object/{post_id}',
                               data=body, headers=headers).json())
    assert response['data']['color'] == u'green', 'Цвет изменен на зеленый'


def delete_posts(post_id):
    response = (requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}'))
    assert response.status_code == 200, 'Объект не удалён'


post_id = post_posts()
put_posts(post_id)
patch_posts(post_id)
