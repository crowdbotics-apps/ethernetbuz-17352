from rest_framework import authentication
from ethernetbuz.models import Ethernetbuz
from .serializers import EthernetbuzSerializer
from rest_framework import viewsets


class EthernetbuzViewSet(viewsets.ModelViewSet):
    serializer_class = EthernetbuzSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ethernetbuz.objects.all()
