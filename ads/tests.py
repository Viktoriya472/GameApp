from django.test import TestCase
from ads.models import Game, Ad
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.game = Game.objects.create(
            name="It Takes Two",
        )

        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.ru",
            password="secret"
        )

        cls.ad = Ad.objects.create(
            title="Какие впечатления",
            content_upload="Какие у вас впечатления от игры",
            user=cls.user,
            game=cls.game,
        )

    def test_ad_model(self):
        self.assertEqual(self.ad.title, "Какие впечатления")
        self.assertEqual(self.ad.content_upload,
                         "Какие у вас впечатления от игры")
        self.assertEqual(self.ad.user.username, "testuser")
        self.assertEqual(self.ad.game.name, "It Takes Two")
        self.assertEqual(str(self.ad), "Какие впечатления")

    def test_ad_listview(self):
        response = self.client.get(reverse("ads"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Какие у вас впечатления от игры")
        self.assertTemplateUsed(response, "ads/ads.html")

    def test_ad_detailview(self):
        response = self.client.get(reverse("ad_detail",
                                           kwargs={"pk": self.ad.pk}))
        no_response = self.client.get("ads/70/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Какие впечатления")
        self.assertTemplateUsed(response, "ads/ad.html")

    def test_ad_createview(self):
        self.client.login(username="testuser",
                          email="test@mail.ru",
                          password="secret")
        response = self.client.post(
            reverse("ad_create"),
            {
                "title": "Новый заголовок",
                "content_upload": "Новый текст",
                "user": self.user.id,
                "game": self.game.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ad.objects.last().title, "Новый заголовок")
        self.assertEqual(Ad.objects.last().content_upload, "Новый текст")

    def test_ad_updateview(self):
        response = self.client.post(
            reverse("ad_update", args="1"),
            {
                "title": "Изменить заголовок",
                "content_upload": "Изменить текст",
                "user": self.user.id,
                "game": self.game.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ad.objects.last().title, "Изменить заголовок")
        self.assertEqual(Ad.objects.last().content_upload, "Изменить текст")

    def test_ad_deleteview(self):
        response = self.client.post(reverse("ad_delete", args="1"))
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/ads/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/ads/1/")
        self.assertEqual(response.status_code, 200)
