"""
*********************************************************************
*                                                                   *
*                           🗒️ iTodo                                *
*                                                                   *
*        یک برنامه لیست کارهای ساده و موثر که با جنگو و              *
*            جاوااسکریپت خالص ساخته شده است 📋🚀                    *
*                                                                   *
*     تولید کننده: idarbandi                                        *
*     ایمیل: darbandidr99@gmail.com                                 *
*     گیت‌هاب: https://github.com/idarbandi/iTweet                  *
*                                                                   *
*********************************************************************
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task


class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(title="Test Task", completed=False)

    def test_task_list(self):
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_create(self):
        url = reverse("task-create")
        data = {"title": "New Task"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update(self):
        url = reverse("task-update", kwargs={"pk": self.task.id})
        data = {"title": "Updated Task", "completed": True}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task")
        self.assertEqual(self.task.completed, True)

    def test_task_delete(self):
        url = reverse("task-delete", kwargs={"pk": self.task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
