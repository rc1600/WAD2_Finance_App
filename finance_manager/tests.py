from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile, FinancialAccount, Budget, Expense

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.account = FinancialAccount.objects.create(username=self.user_profile, financial_account_name='Test Account')
        self.budget = Budget.objects.create(date='2024-01-01', category='Test Category', amount=100.0)
        self.expense = Expense.objects.create(category='Test Category', price=50.0)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_analysis_view(self):
        response = self.client.get(reverse('analysis'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'analysis.html')

    def test_contactUs_view(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contactUs.html')

    def test_newSpending_view(self):
        response = self.client.get(reverse('newSpending'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newSpending.html')

    def test_incomeOutcome_view(self):
        response = self.client.get(reverse('incomeOutcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incomeOutcome.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutUs.html')

    def test_userAccountPage_view(self):
        response = self.client.get(reverse('userAccountPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userAccountPage.html')

    def test_financialAccount_view(self):
        response = self.client.get(reverse('financial_account', args=[self.account.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'financialAccount.html')

    def test_newAccount_view(self):
        response = self.client.get(reverse('newAccount'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newAccount.html')

    def test_budget_view(self):
        response = self.client.get(reverse('budget'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget.html')

    def test_contact_form_submit_view(self):
        response = self.client.post(reverse('contact_form_submit'), {'name': 'Test Name', 'email': 'test@example.com', 'message': 'Test Message'})
        self.assertEqual(response.status_code, 302)  

    def test_deleteBudget_view(self):
        response = self.client.get(reverse('delete_budget', args=[self.budget.id]))
        self.assertEqual(response.status_code, 302)  

    def test_deleteFinancialAccount_view(self):
        response = self.client.get(reverse('delete_financial_account', args=[self.account.slug, self.account.pk]))
        self.assertEqual(response.status_code, 302)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Finance Manager")

    def test_about_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, "Welcome to Finance Manager!")
        self.assertContains(response, "User-Centric Approach")

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.slug, 'test_user')

class FinancialAccountTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='password123')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.financial_account = FinancialAccount.objects.create(username=self.user_profile, financial_account_name='Savings', savings_balance=1000, current_balance=1000)

    def test_financial_account_creation(self):
        self.assertEqual(self.financial_account.financial_account_name, 'Savings')
        self.assertEqual(self.financial_account.username, self.user_profile)
        self.assertEqual(self.financial_account.savings_balance, 1000)
        self.assertEqual(self.financial_account.current_balance, 1000)
