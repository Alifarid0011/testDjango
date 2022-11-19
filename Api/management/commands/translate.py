import django.core.management
from bs4 import BeautifulSoup
import requests
from googletrans import Translator
from django.core.management import BaseCommand


class Command(BaseCommand):
    url = "https://torob.com/search/?query="

    def add_arguments(self, parser):
        parser.add_argument("text", help="text that you want to translate")
        parser.add_argument("--from", default="en", choices=["fa", "en", "ar"], help="from language")
        parser.add_argument("--to", default="fa", choices=["fa", "en", "ar"], help="to language")

    def handle(self, *args, **options):
        # url = f"{self.url}?hl={options['to']}&sl={options['from']}&tl={options['to']}&text={options['text']}&op=translate"
        url = f"{self.url}{options['text']}"
        search = BeautifulSoup(requests.get(url).text, "lxml")
        print(search.find_all("span"))
