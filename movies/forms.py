from django import forms
from django.forms import ModelForm
from .models import *


class ReviewForm(ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class RatingForm(ModelForm):
    """Форма для добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)
