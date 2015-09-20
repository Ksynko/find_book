from haystack import indexes
from .models import Page


class PageIndex(indexes.ModelSearchIndex, indexes.Indexable):

    class Meta:
        model = Page
        fields = ['text', 'number', 'chapter']

    def get_model(self):
        return Page

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter()
