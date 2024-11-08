from django.test import TestCase
from app.services import EmailService
from django.core.mail import outbox
from unittest.mock import patch
from django.urls import reverse
from app.models import Project, Tag
from datetime import datetime, date
from django.contrib.messages import get_messages
from django.utils import timezone

# EmailService test
class EmailServiceTest(TestCase):
    # Avoid actually sending emails during the test
    @patch('app.services.send_mail')
    def test_send_project_created_email(self, mock_send_mail):
        recipient_email = 'recipient@example.com'
        EmailService.send_project_created_email(recipient_email)

        # Ensure the email was sent with the correct details
        mock_send_mail.assert_called_with(
            'Project created',
            'You have created a new project.',
            'test@example.com',
            [recipient_email]
        )

###################################################################
# Add project test
class AddProjectViewTest(TestCase):
    def test_app_project_valid(self):
        url = reverse('create_project')
        data = {
            'title': 'Test Project',
            'description': 'Test description',
            'image': '',
            'completed': False,
            'due_date': '2024-12-31',
            'tags': 'tag1, tag2',
        }
        
        # POST request
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 302)
        
        self.assertRedirects(response, reverse('home'))
        
        expected_due_date = timezone.make_aware(
            datetime.strptime('2024-12-31', '%Y-%m-%d')
        )
        
        # Check if project was created successfully in the database
        project = Project.objects.get(title='Test Project')
        self.assertEqual(project.title, 'Test Project')
        self.assertEqual(project.description, 'Test description')
        self.assertEqual(project.due_date, expected_due_date)
        
        # Check if tags was correctly associated
        tags = project.tags.all()
        self.assertEqual(tags.count(), 2)
        
        # Check if tag1 and tag2 exist in the database
        self.assertTrue(Tag.objects.filter(title='tag1').exists())
        self.assertTrue(Tag.objects.filter(title='tag2').exists())
        
        # Check if tags are associated with the project
        tag1 = Tag.objects.get(title='tag1')
        tag2 = Tag.objects.get(title='tag2')
        self.assertIn(tag1, project.tags.all())
        self.assertIn(tag2, project.tags.all())
        
        # Check if success message is displayer
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Project create correctly !")
        
###################################################################

# Update project test
class UpdateProjectViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test project',
            description='Test description',
            image='',
            completed=False,
            due_date="2024-12-31",
        )
        
        self.tag1 = Tag.objects.create(title='tag1')
        self.tag2 = Tag.objects.create(title='tag2')
        self.project.tags.add(self.tag1)
        self.project.tags.add(self.tag2)
        
    def test_update_project_valid(self):
        url = reverse('update_project', kwargs={'pk': self.project.pk})
        data = {
            'title': 'Updated project',
            'description': 'Updated description',
            'image': '',
            'completed': True,
            'due_date': '2025-01-01',
            'tags': 'tag1, tag2, tag3',
        }
        
        response = self.client.post(url, data)
        expected_due_date = timezone.make_aware(
            datetime.strptime('2025-01-01', '%Y-%m-%d'),
            timezone.utc
        )
        
        self.assertRedirects(response, reverse('home'))
        
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Updated project')
        self.assertEqual(self.project.description, 'Updated description')
        self.assertEqual(self.project.completed, True)
        self.assertEqual(self.project.due_date, expected_due_date)
        
        self.assertEqual(self.project.tags.count(), 5)
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[0]), "Project update correctly!")
        self.assertEqual(str(messages[1]), "Your project has been modified correctly.")
        
        
    def test_update_project_invalid(self):
        url = reverse('update_project', kwargs={'pk': self.project.pk})
        data = {
            'title': '',
            'description': 'Invalid description',
            'image': '',
            'completed': True,
            'due_date': 'invalid date',
            'tags': 'tag1',
        }
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 200)
        
        expected_due_date = timezone.make_aware(
            datetime.strptime('2024-12-31', '%Y-%m-%d'),
            timezone.utc
        )
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your project cannot be update...")
        
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Test project')
        self.assertEqual(self.project.description, 'Test description')
        self.assertEqual(self.project.completed, False)
        self.assertEqual(self.project.due_date, expected_due_date)

###################################################################

# Delete project test
class DeleteProjectViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test project",
            description="Test description",
            image="",
            completed=False,
            due_date=date(2024, 12, 31)
        )
    def test_delete_project_valid(self):
        url = reverse('delete_project', kwargs={'pk': self.project.pk})
        
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 302)
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your project has been deleted correctly.")
        
        with self.assertRaises(Project.DoesNotExist):
            self.project.refresh_from_db()

###################################################################

# Project model test
class ProjectModelTest(TestCase):
    def test_project_model(self):
        project = Project.objects.create(
            title='Test project',
            description='Test description',
            image='',
            completed=False,
            due_date=date(2024, 12, 31)
        )
        self.assertEqual(str(project), 'Test project')

###################################################################

# Tag model test
class TagModelTest(TestCase):
    def test_tag_model(self):
        tag = Tag.objects.create(title='Test tag')
        self.assertEqual(str(tag), 'Test tag')