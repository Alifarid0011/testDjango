import json

from django.core.management.base import BaseCommand, CommandError
import requests


class Command(BaseCommand):
    url = "https://v2.jokeapi.dev/joke/Any"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, default=1, help="It should be less than 100")
        parser.add_argument("-lang", type=str, default="fa", choices=["fa", "ar"], help="fa, ar")

    def say_jock(self, options):
        return json.loads(requests.get(f"{self.url}?type=single&amount={options['count']}").text)

    def handle(self, *args, **options):
        if options["count"] < 100:
            response = self.say_jock(options)
            with open("file.txt", "a+") as file:
                if "jokes" in response:
                    for i in response["jokes"]:
                        file.write(i["joke"] + "\n################################################################\n")
                else:
                    file.write(
                        response["joke"] + "\n################################################################\n")
                file.close
            self.stdout.write("it's ok")
        else:
            raise CommandError("ablah less than 100")


