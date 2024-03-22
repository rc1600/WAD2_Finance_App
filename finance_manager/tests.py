from django.test import TestCase
from django.urls import reverse
from finance_manager.models import FinancialAccount, UserProfile
from django.contrib.auth.models import User

class SignUpTestCase(TestCase):
    def test_signup(self):
        signup_data = {
            'username': 'testuser123',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }

        response = self.client.post(reverse('signup'), signup_data, follow=True)

        self.assertEqual(response.status_code, 200)

        if response.context.get('form'):
            print(response.context['form'].errors)

        print(response.content.decode('utf-8'))

        self.assertTrue(User.objects.filter(username='testuser123').exists())

        self.assertRedirects(response, reverse('userAccountPage'))

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.login_url = reverse('login')
        self.login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }

    def test_login_valid(self):
        response = self.client.post(self.login_url, self.login_data)
        self.assertEqual(response.status_code, 302) 

    def test_login_invalid(self):
        invalid_data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, invalid_data)
        self.assertEqual(response.status_code, 200)

class FinancialAccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.financial_account = FinancialAccount.objects.create(
            username=self.user_profile,
            financial_account_name='Test Account',
            balance=500,
            slug='test-account'
        )

    def test_delete_financial_account(self):
        url = reverse('delete_financial_account', kwargs={'account_slug': self.financial_account.slug, 'financial_account_id': self.financial_account.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(FinancialAccount.objects.filter(pk=self.financial_account.pk).exists())

def test_new_spending_view(self):
    response = self.client.get(reverse('newSpending'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'newSpending.html')

    form_data = {
        'description': 'Test spending',
        'amount': 100,
        'date': '2024-03-21',
    }
    response = self.client.post(reverse('newSpending'), data=form_data)
    self.assertEqual(response.status_code, 302)  

    invalid_form_data = {
        'description': '',
        'amount': -100,  
        'date': '2024-03-21',
    }
    response = self.client.post(reverse('newSpending'), data=invalid_form_data)
    self.assertEqual(response.status_code, 200)  
    self.assertFormError(response, 'form', 'description', 'This field is required.')
    self.assertFormError(response, 'form', 'amount', 'Ensure this value is greater than or equal to 0.')


def test_budget_view(self):
    response = self.client.get(reverse('budget'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'budget.html')

    form_data = {
        'category': 'Test Category',
        'amount': 500,
    }
    response = self.client.post(reverse('budget'), data=form_data)
    self.assertEqual(response.status_code, 302)  

    invalid_form_data = {
        'category': '', 
        'amount': -500,  
    }
    response = self.client.post(reverse('budget'), data=invalid_form_data)
    self.assertEqual(response.status_code, 200)  
    self.assertFormError(response, 'form', 'category', 'This field is required.')
    self.assertFormError(response, 'form', 'amount', 'Ensure this value is greater than or equal to 0.')