from rest_framework import serializers

from emoticons.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title', 'keywords', 'mode', 'pics')