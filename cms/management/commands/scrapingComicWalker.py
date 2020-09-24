from django.core.management.base import BaseCommand

import datetime
import requests
from bs4 import BeautifulSoup

from cms.models import Comic

class Command(BaseCommand):
    def handle(self, *args, **options):
      load_url = "https://comic-walker.com"
      html = requests.get(load_url)
      soup = BeautifulSoup(html.content, "html.parser")

      # HTML全体を表示する
      tileListWrap = soup.find('dl', class_='tileListWrap')
      elements = tileListWrap.select('a')
      for ele in elements:
        link = load_url + ele.get('href')
        if 'https://comic-walker.com/contents/detail/' in link:
          sub_html = requests.get(link)
          sub_soup = BeautifulSoup(sub_html.content, "html.parser")
          comic = Comic.objects.filter(home_link=link)
          if comic.first() is None:
            comic = Comic()
            comic.home_link = link
            comic.main_title = sub_soup.find('title').text
          rightBox = sub_soup.find('div', class_='comicIndex-rightBox')
          if rightBox is not None:
            sub_links = rightBox.select('a')
            sub_link = sub_links[0].get('href')
            sub_links = rightBox.select('a')
            sub_link = sub_links[0].get('href')
            comic.link = load_url + sub_link
            comic_html = requests.get(comic.link)
            comic_soup = BeautifulSoup(comic_html.content, "html.parser")
            comic.title = comic_soup.find('title').text
            comic.update_time = datetime.datetime.now()
            comic.save()
