from rest_framework import serializers
from noteme.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    id =  serializers.UUIDField(required=False)
    
    class Meta:
        model = ToDo
        fields = ('id','title','body', 'done')

#class ToDoSerializer(serializers.Serializer):
#    title = serializers.CharField(required=True, max_length=120)
#    body = serializers.CharField()
#    done = serializers.BooleanField()
#
#    def restore_object(self, attrs, instance=None):
#        if instance:
#            instance.title = attrs.get('title', instance.title)
#            instance.name = attrs.get('body', instance.body)
#            instance.done = attrs.get('done', instance.done)
#            return instance
#
#        return ToDo(**attrs)