from django import forms

from comments.models import Comment
from blog.models import Blog

class CommentForm(forms.ModelForm):
    #text = forms.TextInput(label = '댓글')

    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "댓글"
