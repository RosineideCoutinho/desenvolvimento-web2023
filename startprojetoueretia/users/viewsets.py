from rest_framework import viewsets
from .serializers import LoginSerializer
from .models import Login


class LoginViewSet(viewsets.ModelViewSet):
    model = Login
    serializer_class = LoginSerializer
    queryset = Login.objects.all()
    filter_fields = ('name', 'email', 'password')