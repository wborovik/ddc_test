from django import forms

from projectmanager.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), label='Комментарий')
