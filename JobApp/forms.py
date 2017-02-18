import re
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Job
from django.utils.text import slugify
import itertools


class JobUploadForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'category', 'tags', 'details', 'street', 'city', 'state', 'end_date']

    def __init__(self, *args, **kwargs):
        super(JobUploadForm, self).__init__(*args, **kwargs)
        self.fields['end_date'].widget = forms.SelectDateWidget()

    # end_date = forms.DateField(widget=DateTimeWidget(usel10n = True, bootstrap_version=3))

    def save(self, commit=False):
        instance = super(JobUploadForm, self).save(commit=commit)

        max_length = Job._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.title)[:max_length]

        for x in itertools.count(1):
            if not Job.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.save()
        return instance
