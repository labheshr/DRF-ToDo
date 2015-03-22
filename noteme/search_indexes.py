from haystack import indexes
from noteme.models import ToDo
 
class ToDoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    body = indexes.CharField(model_attr="body")
 
    def get_model(self):
        return ToDo