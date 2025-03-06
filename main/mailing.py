from main.models import Contact
from django.template import loader
from news.models import News
import datetime


date_today = datetime.datetime.today()
today_min = datetime.datetime.combine(date_today.date(), date_today.time().min)
today_max = datetime.datetime.combine(date_today.date(), date_today.time().max)
list_news_for_mailings = News.objects.filter(datetime__range=(today_min, today_max))
message_list_news = loader.render_to_string('news/newsletter/news_send.html',
                                            {'all_news': list_news_for_mailings})
contact_list = list(Contact.objects.values_list('email', flat=True))
