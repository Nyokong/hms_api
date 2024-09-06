from rest_framework import serializers

from .models import FeedbackMessage


# feedback serializer goes here
class FeedbackMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackMessage
        fields = ['message']