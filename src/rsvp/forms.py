from django import forms
from recaptcha.django import fields as r_fields
from django.utils.translation import ugettext_lazy as _

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = {'class': 'required'}
 
class EventRsvpForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("E-mail"))
    recaptcha = r_fields.ReCaptchaField(label=_("Anti-Spam"))