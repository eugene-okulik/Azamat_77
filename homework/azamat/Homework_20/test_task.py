import requests
import json
import unittest

from homework.eugene_okulik.Lesson_18.api_requests import clear


class TestPostApi(unittest.TestCase):

    # Предусловия, создание поользователя и сохранием АЙДИ
    def setUp(self) -> None:
        print('Start testing')
        body = json.dumps({
            "data": {"color": 'white', "size": 'BUG'},
            "name": 'Test_object'
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://objapi.course.qa-practice.com/object', data=body, headers=headers)
        self.post_id = response.json()['id']

    # Постусловие, очищаем все за собой
    def tearDown(self) -> None:
        print('Testing completed')
        requests.delete(f'http://objapi.course.qa-practice.com/object/{self.post_id}')

    # Тест на нахождение нужного пользователя
    def test_one_post(self):
        print('before test')
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id, 'Айди не совпадают')
        print('after test')


    def test_put_posts(self):
        body = json.dumps({
            "data": {"color": 'white', "size": 'BUG'},
            "name": 'Test_77'
        })
        headers = {'Content-Type': 'application/json'}
        response = (requests.put(
            f'http://objapi.course.qa-practice.com/object/{self.post_id}',
            data=body,
            headers=headers
        ).json())
        self.assertEqual(response['name'], 'Test_77', 'Имя не изменен')


    def test_patch_posts(self):
        body = json.dumps({
            "data": {"color": 'green', "size": 'BUG'}
        })
        headers = {'Content-Type': 'application/json'}
        response = (requests.patch(f'http://objapi.course.qa-practice.com/object/{self.post_id}',
                                   data=body, headers=headers).json())
        self.assertEqual(response['data']['color'], 'green', 'Цвет не изменен')


    def delete_posts(self):
        response = (requests.delete(f'http://objapi.course.qa-practice.com/object/{self.post_id}')).json()
        self.assertEqual(response.status_code, 200, 'Объект не удалён')


class TestNotSetUP(unittest.TestCase):

    def tearDown(self) -> None:
        print('Testing completed')
        requests.delete(f'http://objapi.course.qa-practice.com/object/{self.test_post_a_posts()}')

    # Вывод всех пользоваетелей
    def test_all_posts(self):
        response = requests.get('http://objapi.course.qa-practice.com/object').json()
        self.assertEqual(len(response), 1, 'Not all posts returned')


    def test_post_a_posts(self):
        body = json.dumps({
            "data": {"color": 'white', "size": 'BUG'},
            "name": 'Test_77'
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://objapi.course.qa-practice.com/object', data=body, headers=headers)
        self.assertEqual(response.status_code, 200, 'Статус не верный')
        self.assertEqual(response.json()['name'], 'Test_77')
        return response.json()['id']
