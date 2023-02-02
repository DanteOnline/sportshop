from rest_framework.test import APITestCase
from partners.models import Partner
from mixer.backend.django import mixer

from user.models import MyUser


class PartnerApiTestCase(APITestCase):

    def setUp(self):
        self.username = 'user'
        self.password = 'user123456'
        self.user = MyUser.objects.create_user(self.username, 'user@user.com', self.password)

    def test_status_code(self):
        url = '/partners/api/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_data(self):
        mixer.blend(Partner, name='My partner')
        url = '/partners/api/'
        response = self.client.get(url)
        self.assertEqual(response.json(), [{'name': 'My partner'}])

        mixer.blend(Partner, name='My partner two')
        url = '/partners/api/'
        response = self.client.get(url)
        self.assertEqual(response.json(), [{'name': 'My partner'}, {'name': 'My partner two'}])

    def test_post(self):
        self.client.force_authenticate(user=self.user)

        data = {'name': 'My partner'}
        url = '/partners/api/'
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Partner.objects.filter(name='My partner').exists())

    def test_put(self):
        self.client.force_authenticate(user=self.user)

        old_partner = mixer.blend(Partner, name='Start partner')
        data = {'name': 'My partner'}
        url = f'/partners/api/{old_partner.id}/'
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, 200)
        new_partner = Partner.objects.get(name='My partner')
        self.assertTrue(old_partner.id == new_partner.id)

