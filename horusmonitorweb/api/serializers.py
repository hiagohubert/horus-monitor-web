from rest_framework import serializers
from horusmonitorweb.dashboard.models import Machine,OS,CPU,Memory,Disc,Service

class MachineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Machine
		fields = ('id', 'name', 'token')

class OSSerializer(serializers.ModelSerializer):
	class Meta:
		model = OS
		fields = ('distributor_id', 'release', 'codename', 'description', 'machine' )

class CPUSerializer(serializers.ModelSerializer):
	class Meta:
		model = CPU
		fields = ('architecture', 'vendor_id', 'model_name', 'cpu_cores', 'percent_used','inserted_at', 'machine')
		
class MemorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Memory
		fields = ('free', 'percent_used', 'total', 'used', 'machine', 'inserted_at')

class DiscSerializer(serializers.ModelSerializer):
	class Meta:
		model = Disc
		fields = ('file_system', 'size', 'used', 'free', 'free_percent', 'mounted_in', 'machine')

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ('name','status', 'machine', 'inserted_at')