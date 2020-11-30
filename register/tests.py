from django.test import TestCase, Client
from register.views import remove_user
from django.contrib.auth.models import User
from django.urls import reverse

class TestRegisterViews(TestCase):

    def setup(self):
        self.user = User.objects.create_user('test', 'test@email.sc.edu')
        self.user.set_password('Erik')
        self.user.save

    def test_remove_user(self):
        user1 = User.objects.filter(username='test')
        post_response = self.client.post(reverse('remove_user'), follow=True)
        client = Client()
        logged = client.login(username='test', password='Erik')
        self.assertFalse(logged)
#        self.assertRedirects(post_response, reverse('/login/'), status_code=302)

if __name__ == '__main__':
    unittest.main()
