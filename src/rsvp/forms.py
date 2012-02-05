from django import forms
from recaptcha.django import fields as r_fields
 
class EventRsvpForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_("E-mail"))
    recaptcha = r_fields.ReCaptchaField()