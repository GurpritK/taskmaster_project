from django.test import TestCase
from .forms import TaskForm
from .models import Category, Task
from datetime import date

class TaskFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Personal")

    def test_valid_form(self):
        form_data = {
            'title': 'Buy groceries',
            'due_date': date.today(),
            'category': self.category.id
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_title(self):
        form_data = {
            'title': '',
            'due_date': date.today(),
            'category': self.category.id
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_missing_due_date(self):
        form_data = {
            'title': 'Buy groceries',
            'due_date': '',
            'category': self.category.id
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('due_date', form.errors)

    def test_missing_category(self):
        form_data = {
            'title': 'Buy groceries',
            'due_date': date.today(),
            'category': ''
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)
