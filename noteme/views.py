from noteme.models import ToDo
from noteme.serializers import ToDoSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
import logging
logger = logging.getLogger(__name__)
import os

from haystack.query import EmptySearchQuerySet,SearchQuerySet

class ToDoList(generics.ListCreateAPIView):
    '''
    http http://127.0.0.1:8000/todo/
    http --json POST http://127.0.0.1:8000/todo/ title="clean" body="clean home"
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    #def get_queryset(self):
    #    '''
    #    restrict using body of the title
    #    http http://127.0.0.1:8000/todo?body=clean%20home
    #    '''
    #    queryset = ToDo.objects.all()
    #    body = self.request.query_params.get('body', None)
    #    if body is not None:
    #        queryset = queryset.filter(body=body)
    #    return queryset

    def get_queryset(self, *args, **kwargs):
            request = self.request
            queryset = EmptySearchQuerySet()
            #if request.GET.get('q') is not None:
                #query = request.GET.get('q')
            body = self.request.query_params.get('body', None)
            title = self.request.query_params.get('title', None)
            if body:
                queryset = SearchQuerySet().filter(body=body)
                assert False, queryset
            elif title:
                queryset = SearchQuerySet().filter(title=title)
            else:
                queryset = ToDo.objects.all()

            return queryset

class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    http http://127.0.0.1:8000/todo/clean
    http PUT http://127.0.0.1:8000/todo/clean title="clean" body="clean home" done=True
    http DELETE http://127.0.0.1:8000/todo/post%20using%20json
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    lookup_field = 'title' #allows us to search by titles as opp. to weird object ids
    
    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        if request.data.get('done') == 'True' and response.status_code == 200:
            try:
                ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
                AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
                TO_PHONE = os.environ.get('TO_PHONE')
                FROM_PHONE = os.environ.get('FROM_PHONE')
                client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
                client.messages.create(to=TO_PHONE, from_=FROM_PHONE, body="task %s has been marked done"%title )
            except:
                logger.error('Twilio send SMS failed')
        return response

    
    
