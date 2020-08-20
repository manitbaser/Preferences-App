from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.test import force_authenticate
from user import views, serializers
from user.models import User

class UserTestCase(APITestCase):
    def setUp(self):
        self.factory = factory = APIRequestFactory()
        self.register_view = views.RegisterUserView.as_view()
        self.token_view = views.GetTokenView.as_view()
        self.user_info_view = views.UserInfoView.as_view()
        self.deactivate_view = views.UserDeactivateView.as_view()
        self.preferences_view = views.UserPreferencesView.as_view()
        self.data = {"username":"testing1", "password":"password1234", "email":"testing1@gmail.com", "first_name":"For", "last_name":"Testing"}
        self.request = self.factory.post('/user/', self.data)
        response = self.register_view(self.request)
        # self.token = response.data["token"]
        # print(self.token.decode("utf-8") )

    def register_user(self):
        data = {"username":"testing2", "password":"password1234", "email":"testing2@gmail.com", "first_name":"For", "last_name":"Testing"}
        request = self.factory.post('/user/', data)
        response = self.register_view(request)
        self.assertEqual(response.status_code, 201)
    
    def get_token(self):
        data = {"email":"testing1@gmail.com", "password":"password1234"}
        request = self.factory.post('/user/', data)
        response = self.token_view(request)
        self.assertEqual(response.status_code, 200)
        
    def user_info(self):
        user = User.objects.get(email='testing1@gmail.com')
        request = self.factory.get('/user/')
        force_authenticate(request, user=user)
        response =self.user_info_view(request)
        self.assertEqual(response.status_code, 200)
        
        data = {"first_name":"Changed", "last_name":"Testing"}
        request = self.factory.put('/user/', data)
        force_authenticate(request, user=user)
        response =self.user_info_view(request)
        self.assertEqual(response.status_code, 200)

    def deactivate_user(self):
        user = User.objects.get(email='testing1@gmail.com')        
        data = {}
        request = self.factory.post('/user/', data)
        force_authenticate(request, user=user)
        response =self.deactivate_view(request)
        self.assertEqual(response.status_code, 200)

####
    def preferences(self):
        user = User.objects.get(email='testing1@gmail.com')        
        data = {"preferences:":[1,2]}
        request = self.factory.put('/user/')
        force_authenticate(request, user=user)
        response =self.preferences_view(request)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        

