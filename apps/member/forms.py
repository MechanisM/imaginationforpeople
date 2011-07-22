import re

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm

from apps.i4p_base.utils import remove_accents

class I4PSignupForm(SignupForm):
    """
    Form to signup with first and last names
    """
    first_name = forms.CharField(_(u'first name'))
    last_name = forms.CharField(_(u'last name'))

    def __init__(self, *args, **kwargs):
        super(I4PSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        self.fields.keyOrder = ['first_name',
                                 'last_name',
                                 'email',
                                 'password1',
                                 'password2']


    def save(self):
        firstname = self.cleaned_data['first_name'].title()
        lastname = self.cleaned_data['last_name'].title()
        fullname = "%s%s" % (firstname, lastname)
        username = re.sub("[^a-zA-Z]", "", remove_accents(fullname))

        users = User.objects.filter(username__istartswith=username)
        if users.count() > 0:
            username = "%s%s" % (username, users.count())

        self.cleaned_data['username'] = username

        new_user = super(I4PSignupForm, self).save()
        new_user.first_name = firstname
        new_user.last_name = lastname

        new_user.save()
        return new_user
