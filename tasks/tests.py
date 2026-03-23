from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskPageTests(TestCase):
    def test_home_page_displays_existing_tasks(self):
        task = Task.objects.create(title='Write tests', description='Cover the homepage flow')

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task.title)
        self.assertContains(response, task.description)

    def test_create_task_from_home_page(self):
        response = self.client.post(
            reverse('create-task'),
            {'title': 'New task', 'description': 'Created from form'},
        )

        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Task.objects.filter(title='New task', description='Created from form').exists())

    def test_complete_task_from_home_page(self):
        task = Task.objects.create(title='Finish setup', description='Task to complete')

        response = self.client.post(reverse('complete-task', args=[task.pk]))

        self.assertRedirects(response, reverse('home'))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_delete_task_from_home_page(self):
        task = Task.objects.create(title='Remove me', description='Task to delete')

        response = self.client.post(reverse('delete-task', args=[task.pk]))

        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
