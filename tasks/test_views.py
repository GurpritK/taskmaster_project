from django.test import TestCase
from django.urls import reverse
from .models import Task, Category

class HomeViewTest(TestCase):
    def setUp(self):
        # Set up any objects needed for the tests
        self.category = Category.objects.create(name="Work")
        self.task = Task.objects.create(
            title="Test Task",
            due_date="2025-01-01",
            completed=False,
            category=self.category
        )

    def test_home_view_status_code(self):
        # Test that the home view returns a 200 status code
        
        pass

    def test_home_view_uses_correct_template(self):
        # Test that the home view uses the correct template
        pass

    def test_home_view_context_data(self):
        # Test that the home view provides the correct context data
        pass

    def test_home_view_post_creates_task(self):
        # Test that posting valid data creates a new task
        pass
