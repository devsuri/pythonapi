from rest_framework import serializers
from .models import snappide

class snappideSerializer(serializers.ModelSerializer):

    class Meta:
        model = snappide
        fields = '__all__'
#        fields = 'paragraph', 'textfield'