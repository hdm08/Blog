from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'id':'contact_name','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'id':'contact_email','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))
    to = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'id':'contact_email','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))
    comments = forms.CharField(required=False, widget=forms.TextInput(attrs={'id':'contact_message','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))


class CommentForm(forms.ModelForm):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'id':'contact_name','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'id':'contact_email','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))
    body = forms.CharField(required=False, widget=forms.TextInput(attrs={'id':'contact_message','class':'form-control rounded-0 border-top-0 border-right-0 border-left-0'}))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
