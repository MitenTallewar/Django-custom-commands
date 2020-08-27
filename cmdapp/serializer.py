from rest_framework import serializers
from cmdapp.models import Emp,Address

class EmpSerializer(serializers.ModelSerializer):
    adrs = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(),many=True) #whenever reequest to emp--all address for that
    class Meta:                                                                         #emp should be given
        model = Emp
        fields= '__all__'


class AddressSerializer(serializers.ModelSerializer):
    # emps =EmpSerializer(many = True) #whenerver request to address--makesure all address belongs to all emps -- should be given
    class Meta:
        model = Address
        fields= '__all__'