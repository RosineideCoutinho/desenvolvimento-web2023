from rest_framework import serializers
from .models import suggestion


class suggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = suggestion
        fields = ['article']




    # article- artigo