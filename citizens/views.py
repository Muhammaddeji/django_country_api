# Relative path: citizens/views.py

from rest_framework.viewsets import ModelViewSet
from .models import Citizen
from .serializers import CitizenSerializer


class CitizenViewSet(ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
