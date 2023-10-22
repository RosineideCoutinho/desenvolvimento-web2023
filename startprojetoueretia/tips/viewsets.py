from rest_framework import viewsets
from .serializers import SuggestionSerializer
from .models import Suggestion


class SuggestionViewSet(viewsets.ModelViewSet):
    model = Suggestion
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()
    filter_fields = ('article')