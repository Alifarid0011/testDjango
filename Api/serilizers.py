from rest_framework import serializers

from Api.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["name"]

