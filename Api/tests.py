import json
import os
from io import StringIO

import pytest
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase, Client
from unittest.mock import patch
from .serilizers import TopicSerializer
from django.urls import reverse

from .management.commands.sayjock import Command
from .models import Topic

client = Client()


# Create your tests here.
class TestCommand(TestCase):
    def setUp(self):
        self.valid_data = {"name": "alifarid1213"}

    @patch('Api.management.commands.sayjock.Command.say_jock')
    @pytest.mark.xfail(reason="grater than 100")
    def test_joke(self, get_jock):
        out = StringIO()
        module_dir = os.path.dirname(__file__)
        with open(f"{module_dir}/fixture/jokeResponse.json") as file:
            get_jock.return_value = json.loads(file.read())
        file.close()
        # get_jock.return_value=
        call_command('sayjock', 5, stdout=out, stderr=StringIO(), )
        say_joke = out.getvalue()
        print(say_joke)
        self.assertEqual(say_joke, "it's ok\n")

    def test_update_result(self):
        userobject = User.objects.create(username='testuser')
        User.objects.filter(username='testuser').update(username='test1user')
        # At this point userobject.val is still testuser, but the value in the database
        # was updated to test1user. The object's updated value needs to be reloaded
        # from the database.
        userobject.refresh_from_db()
        self.assertEqual(userobject.username, 'test1user')

    def test_create_topic(self):
        response = client.post(reverse('topic'),
                               data=json.dumps(self.valid_data),
                               content_type='application/json'
                               )
        topic = Topic.objects.create(name='testtopic')
        topics = Topic.objects.all()
        serilizers = TopicSerializer(topics, many=True)
        # print(serilizers.data)
        serilizer = TopicSerializer(data={"name": 'testtopic'})
        if serilizer.is_valid():
            serilizer.save()
        # print(response.data)
