from django.test import TestCase
from mixer.backend.django import mixer
from partners.models import Partner
from user.models import MyUser


class TestViews(TestCase):

    def setUp(self):
        self.username = 'user'
        self.password = 'user123456'
        MyUser.objects.create_user(self.username, 'user@user.com', self.password)

    def test_list_redirect_status_code(self):
        url = '/partners/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_list_status_code(self):
        self.client.login(username=self.username, password=self.password)
        url = '/partners/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        url = '/partners/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_list_context(self):
        partner = mixer.blend(Partner, name='My partner')
        self.client.login(username=self.username, password=self.password)
        url = '/partners/'
        response = self.client.get(url)
        self.assertIn('object_list', response.context)
        self.assertIn(partner, response.context['object_list'])

    def test_list_content(self):
        partner = mixer.blend(Partner, name='My partner')
        self.client.login(username=self.username, password=self.password)
        url = '/partners/'
        response = self.client.get(url)
        self.assertIn(b'My partner', response.content)
