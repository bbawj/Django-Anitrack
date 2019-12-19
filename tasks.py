from main.script import get_anime_info
from main.models import AnimeInfo
import logging
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")



@register_job(scheduler, "interval", minutes=10, id="new_job", replace_existing=True, max_instances = 1, coalesce=True)
def update_database():

    real_title = []
    data_title = AnimeInfo.objects.values_list("title", flat=True)
    anime_list = get_anime_info()

    for anime in anime_list:
        real_title.append(anime["title"])

    if len(data_title) == 0: #if database is currently empty, save all data from api, for initialization
        for t in real_title:
            missing = next(item for item in anime_list if item["title"] == t)
            a = AnimeInfo(title=missing["title"], latest_ep_num=missing["latest_ep_num"],ld=missing["ld"],sd=missing["sd"],hd=missing["hd"],fhd=missing["fhd"])
            a.save()


    else: #test if api fails
        for t in real_title:
            #testing if the titles in the database and from the api match, update if match

            b = next(item for item in anime_list if item["title"] == t)
            a1 = AnimeInfo(title=t, latest_ep_num=b["latest_ep_num"], ld=b["ld"], sd=b["sd"],hd=b["hd"],fhd=b["fhd"])
            a1.save()
            print(anime_list)

        for t in data_title:   #testing if there are any old titles to delete
            if t not in real_title:
                a = AnimeInfo.objects.get(title=t)
                a.delete()
            else:
                pass

scheduler.start()
print("Scheduler started!")
