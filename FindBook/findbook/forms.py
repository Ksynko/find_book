from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(label='What we will search in books?',
                                  max_length=200)
    email = forms.EmailField(label="Your email for search results")
