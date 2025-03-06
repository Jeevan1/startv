from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        exclude = [ "created_at", "updated_at"] 
        read_only_fields = ["idx", "created_at", "updated_at"]