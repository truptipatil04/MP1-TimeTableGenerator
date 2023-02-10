from django.forms import ModelForm
from .models import Subject, Room, Batch, Time

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = "__all__"

class TimeForm(ModelForm):
    class Meta:
        model = Time
        fields = "__all__"