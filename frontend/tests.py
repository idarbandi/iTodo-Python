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


class FrontendTests(TestCase):
    def test_list_view(self):
        url = reverse("list")  # Assumes the URL pattern name is 'list'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "frontend/list.html")
