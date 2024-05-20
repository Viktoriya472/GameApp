from django.test import TestCase
from news.models import News, Category
from django.contrib.auth import get_user_model
from django.urls import reverse


class NewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Кино"
        )

        cls.user = cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.ru",
            password="secret"
        )

        cls.news = News.objects.create(
            header="Test header",
            text="Test text",
            image="test.png",
            user=cls.user
        )

        cls.news.category.set([cls.category,])

    def test_ad_model(self):
        self.assertEqual(self.news.header, "Test header")
        self.assertEqual(self.news.text, "Test text")
        self.assertEqual(self.news.image, "test.png")
        self.assertEqual(self.news.user.username, "testuser")
        list_category_names = self.news.category.values_list('name', flat=True)
        self.assertEqual(*(list_category_names), "Кино")

    def test_news_listview(self):
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test text")
        self.assertTemplateUsed(response, "news/news.html")

    def test_news_detailview(self):
        response = self.client.get(reverse("news_detail",
                                           kwargs={"pk": self.news.pk}))
        no_response = self.client.get("news/1000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test header")
        self.assertTemplateUsed(response, "news/news_detail.html")

    # def test_news_createview(self):
    #     self.client.login(username="testuser",
    #                       email="test@mail.ru",
    #                       password="secret")
    #     response = self.client.post(
    #         reverse("news_create"),
    #         {
    #             "header": "Test header_2",
    #             "text": "Test text_2",
    #             "image": "test_2.png",
    #             "user": self.user.id,
    #         }
    #     )

    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(News.objects.last().header, "Test header_2")
    #     self.assertEqual(News.objects.last().text, "Test text_2")
    #     self.assertEqual(News.objects.last().image, "test_2.png")

    # def test_news_updateview(self):
    #     response = self.client.post(
    #         reverse("news_update", args="1"),
    #         {
    #             "header": "Update header",
    #             "text": "Update text",
    #             "image": "update_img.png",
    #             "user": self.user.id,
    #         },
    #     )
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(News.objects.last().header, "Update header")
    #     self.assertEqual(News.objects.last().text, "Update text")
    #     self.assertEqual(News.objects.last().image, "update_img.png")

    # def test_news_deleteview(self):
    #     response = self.client.post(reverse("news_delete"), args="1")
    #     self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/news/1/")
        self.assertEqual(response.status_code, 200)
