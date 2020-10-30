from django.test import TestCase
class Test_Social_Authentication(APITestCase):
    """Tests social authentication"""
    url = reverse('authentication:social_login')

    def setUp(self):
        self.provider = "twitter"
        self.data = {
            "access_token": config('TWITTER_ACCESS_TOKEN'),
            "access_token_secret": config('TWITTER_ACCESS_TOKEN_SECRET'),
            "provider": self.provider
        }
    @skip("Fails because of expired access keys")
    def test_user_successful_social_login(self):
        """Test for successful user login"""
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

         def test_wrong_credentials(self):
        """Test wrong credentials"""
        self.data = {
            "access_token": config('TWITTER_ACCESS_TOKEN_INVALID'),
            "access_token_secret": config('TWITTER_ACCESS_TOKEN_SECRET'),
            "provider": "twitter"
        }
        error_msg = 'Authentication process canceled'
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.data['error'], error_msg)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

         @skip("Fails because of expired access keys")
    def test_google_auth(self):
        """Test Google Oauth"""
        self.data = {
            "access_token": config('GOOGLE_ACCESS_TOKEN'),
            "access_token_secret": config('TWITTER_ACCESS_TOKEN_SECRET'),
            "provider": "google-oauth2"
        }

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')
class TestModels(TestCase):
    def test_model_str(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        self.assertEqual(str(book), "The man in the high castle")
        self.assertEqual(str(philip), "Philip K. Dick")

f

class CreateNewPuppyTest(TestCase):
    """ Test module for inserting a new puppy """
     def setUp(self):
        self.username = "eugine"
        self.email = "ochungeugine@gmail.com"
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')

user = User.objects.get(username='lauren')
client = APIClient()
client.force_authenticate(user=user)


# Create your tests here.
