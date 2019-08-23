from django.contrib.auth.models import Group
from django.test import Client
from django.test import TestCase
from users.models import User


class TestViewsAndGroupPermissionsTests(TestCase):

    def setUp(self):
        # create permissions group
        self.group_1 = Group.objects.create(name="View1 Viewers")
        self.group_2 = Group.objects.create(name="View2 Viewers")

        self.c = Client()

        self.user_1_test = User.objects.create_user(username="user_1_test", email="user_1_test@test.com", password="123456")
        self.user_2_test = User.objects.create_user(username="user_2_test", email="user_2_test@test.com", password="123456")
        self.user_3_test = User.objects.create_user(username="user_3_test", email="user_3_test@test.com", password="123456")

    def tearDown(self):
        self.group_1.delete()
        self.group_2.delete()

        self.user_1_test.delete()
        self.user_2_test.delete()
        self.user_3_test.delete()

    def test_user_1_cant_access_view_2(self):
        """user NOT in group should not have access """

        self.c.login(username='user_1_test', password='123456')
        response = self.c.get("/view-2/")
        self.assertEqual(response.status_code, 302, u'User not in group should not have access')

    def test_user_2_cant_access_view_1(self):
        """user NOT in group should not have access """

        self.c.login(username='user_2_test', password='123456')
        response = self.c.get("/view-1/")
        self.assertEqual(response.status_code, 302, u'User not in group should not have access')

    def test_user_1_can_access_view_1(self):
        """user in group should have access """

        self.user_1_test.groups.add(self.group_1)
        self.user_1_test.save()

        self.c.login(username='user_1_test', password='123456')
        response = self.c.get("/view-1/")
        self.assertEqual(response.status_code, 200, u'User in group should have access')

    def test_user_2_can_access_view_2(self):
        """user in group should have access """

        self.user_2_test.groups.add(self.group_2)
        self.user_2_test.save()

        self.c.login(username='user_2_test', password='123456')
        response = self.c.get("/view-2/")
        self.assertEqual(response.status_code, 200, u'User in group should have access')

    #