from noteme.models import ToDo
from noteme.serializers import ToDoSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
import logging
logger = logging.getLogger(__name__)

class ToDoList(generics.ListCreateAPIView):
    '''
    http http://127.0.0.1:8000/todo/
    http --json POST http://127.0.0.1:8000/todo/ title="clean" body="clean home"
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        '''
        restrict using body of the title
        http http://127.0.0.1:8000/todo?body=clean%20home
        '''
        queryset = ToDo.objects.all()
        body = self.request.query_params.get('body', None)
        if body is not None:
            queryset = queryset.filter(body=body)
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
                ACCOUNT_SID = "AC59345910d470c6a4c0452f358ab15846"
                AUTH_TOKEN = "57b9507fe53a091da19bc30ebe85ee18"
                client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
                client.messages.create(to="9173708927", from_="+13476907785", body="task %s has been marked done"%title )
            except:
                logger.error('Twilio send SMS failed')
        return response
        

#from noteme.models import ToDo
#from noteme.serializers import ToDoSerializer
#from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#
##twilio's free sms service for trial..
#from twilio.rest import TwilioRestClient
#
#class ToDoList(APIView):
#    """
#    List all todos, or create a new todo.
#    """
#    def get(self, request, format=None):
#        '''
#        http http://127.0.0.1:8000/todo/
#        '''
#        todos = ToDo.objects.all()
#        serializer = ToDoSerializer(todos, many=True)
#        return Response(serializer.data)
#
#    def post(self, request, format=None):
#        '''
#        http --json POST http://127.0.0.1:8000/todo/ title="clean" body="clean home"
#        '''
#        serializer = ToDoSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#class ToDoDetail(APIView):
#    """
#    Retrieve, update or delete a snippet instance.
#    """
#    def get_object(self, title):
#        #this defines what we are searching the mongodb for
#        try:
#            return ToDo.objects.filter(title=title)[0]
#        except: #ToDo.DoesNotExist
#            raise Http404
#
#    def get(self, request, title, format=None):
#        '''
#        http http://127.0.0.1:8000/todo/clean
#        where clean is the title of todo item
#        '''
#        todo = self.get_object(title)
#        serializer = ToDoSerializer(todo)
#        return Response(serializer.data)
#
#    def put(self, request, title, format=None):
#        '''
#        http PUT http://127.0.0.1:8000/todo/clean title="clean" body="clean home" done=True
#        '''
#        todo = self.get_object(title)
#        serializer = ToDoSerializer(todo, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            if request.data.get('done') == 'True':
#                #use twilio's sms service to send a test message to yourself
#                #TODO: how to hide this: example from github?
#                ACCOUNT_SID = "AC59345910d470c6a4c0452f358ab15846"
#                AUTH_TOKEN = "57b9507fe53a091da19bc30ebe85ee18"
#                client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
#                client.messages.create(to="9173708927", from_="+13476907785", body="task %s has been marked done"%title )
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, title, format=None):
#        '''
#        http DELETE http://127.0.0.1:8000/todo/post%20using%20json
#        '''
#        todo = self.get_object(title)
#        todo.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
#from pymongo import Connection
#
#def getDbHandle():
#    '''
#    gets handle to the mongodb's collection
#    '''
#    databaseName = 'notes_db'
#    connection = Connection()
#    db = connection[databaseName]
#    notemeCollection = db['noteme_todo']
#    
#    return notemeCollection
#
#
#
#class ToDoList(APIView):
#    """
#    List all todos, or create a new todo.
#    """
#    def get(self, request, format=None):
#        #get our collection
#        todos = []
#        noteMeCollection = getDbHandle()
#        for r in noteMeCollection.find():
#            todo = ToDo(r["title"],r["body"],r["done"])
#            todos.append(todo)
#        serializedList = ToDoSerializer(todo, many=True)
#        return Response(serializedList.data)
#
#    def post(self, request, format=None):
#        #get data from the request and insert the record
#        name = request.POST["title"]
#        body = request.POST["body"]
#        done = request.POST["done"]
#        try:
#            noteMeCollection = getDbHandle()
#            noteMeCollection.insert({"title" : name, "body": body, "done":done})
#        except:
#            return Response({ "ok": "false" })
#        return Response({ "ok": "true" })
#
#
#class ToDoDetail(APIView):
#    """
#    Retrieve, update or delete a snippet instance.
#    """
#    lookup_field = 'title' #allows us to search by titles as opp. to weird object ids
#    def get_object(self, title):
#        #this defines what we are searching the mongodb for
#        try:
#            return ToDo.objects.find_one( { lookup_field:title } )
#        except ToDo.DoesNotExist:
#            raise Http404
#
#    def get(self, request, title, format=None):
#        todo = self.get_object(title)
#        serializer = ToDoSerializer(todo)
#        return Response(serializer.data)
#
#    def put(self, request, title, format=None):
#        todo = self.get_object(title)
#        serializer = ToDoSerializer(todo, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, title, format=None):
#        todo = self.get_object(title)
#        todo.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)