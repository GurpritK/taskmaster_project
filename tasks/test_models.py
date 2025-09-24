from django.core.exceptions import ValidationError
from django.test import TestCase
from tasks.models import Task, Category


class TaskModelTest(TestCase):

    def setUp(self):
        # Setup code for creating test instances of Task and Category
        self.category = Category.objects.create(name="Test Category")
        self.task = Task.objects.create(
            title="Test Task",
            due_date="2024-10-10",
            completed=False,
            category=self.category
        )

    def test_task_creation(self):
        # Test for task creation
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.due_date, "2024-10-10")
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.category, self.category)

    def test_task_str(self):
        # Test for the __str__ method of Task
        self.assertEqual(str(self.task), "Test Task")

    def test_task_due_date(self):
        # Test for the due_date field of Task
        self.assertEqual(self.task.due_date, "2024-10-10")

    def test_task_completed_default(self):
        # Test for the default value of the completed field
        self.assertEqual(self.task.completed, False)

    def test_task_category_relationship(self):
        # Test the relationship between Task and Category
        self.assertEqual(self.category.tasks.first(), self.task)
        self.assertEqual(self.category.tasks.count(), 1)
    
    def test_task_title_length(self):
        # generate a unit test that checks for an error if the title is longer than 200 characters
        from django.core.exceptions import ValidationError
        long_title = "a" * 201  # max_length is 200
        task = Task(
            title=long_title,
            due_date="2025-01-01",
            completed=False,
            category=self.category
        )
        with self.assertRaises(ValidationError):
            task.full_clean()