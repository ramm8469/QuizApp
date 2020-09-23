from django.test import TestCase
from .models import CustomUserModel
# Create your tests here.

class TestCustomUser(TestCase):

    def test_user_create(self):
        user = CustomUserModel.objects.create_user(
            username='ram',
            email="ram@mohan.com",
            password="hrhk"
        )

        self.assertEqual(user.username, 'ram')
        self.assertEqual(user.email, 'ram@mohan.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    
    def test_superuser_create(self):
        super_user = CustomUserModel.objects.create_superuser(
             username="shyam",
             email="shyam@mohan.com",
             password='hrhk'
         )

        self.assertEqual(super_user.username, 'shyam')
        self.assertEqual(super_user.email, 'shyam@mohan.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
        

