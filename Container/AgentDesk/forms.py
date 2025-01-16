from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': ' w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all',
                'placeholder': 'Enter your name',
            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': ' w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all',
                'placeholder': 'Enter your password',
            }))
    
