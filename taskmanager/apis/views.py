from rest_framework import generics
from emoticons.models import Topic
from .serializers import TopicSerializer



# Create your views here.
class TopicAPIView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer