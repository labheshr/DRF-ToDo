from rest_framework import serializers
from noteme.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    id =  serializers.UUIDField(required=False)
    
    class Meta:
        model = ToDo
        fields = ('id','title','body', 'done')