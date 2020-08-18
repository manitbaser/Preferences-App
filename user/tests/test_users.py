from django.test import TestCase
from user.models import User
from user.views import RegisterUserView
import json
import requests

class UserTestCase(TestCase):
    def setUp(self):
        pass
    
    def register_user(self):
        y=json.dumps({"username":"testing", "password":"password1234", "email":"testing@gmail.com", "first_name":"For", "last_name":"Testing"})
        # y = json.dumps(x)
        # response = requests.post('http://httpbin.org/post', files=dict(foo='bar'))
        response = RegisterUserView.post(self,y)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

