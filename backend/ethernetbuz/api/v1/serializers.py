from rest_framework import serializers
from ethernetbuz.models import Ethernetbuz


class EthernetbuzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethernetbuz
        fields = "__all__"
