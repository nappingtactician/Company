from rest_framework import serializers
from .models import asset,work,worker,allocatework

class assetSerializer(serializers.ModelSerializer):

    class Meta:
        model = asset
        fields = '__all__'

class workSerializer(serializers.ModelSerializer):
    class Meta:
        model = work
        fields = '__all__'

class workerSerializer(serializers.ModelSerializer):
    class Meta:
        model = worker
        fields = '__all__'

class allocateworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = allocatework
        fields = '__all__'
