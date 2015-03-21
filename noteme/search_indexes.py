from haystack import indexes
from noteme.models import ToDo
 
class ToDoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
 
    def get_model(self):
        return ToDo