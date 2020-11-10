from django import forms
range_attr = {
    'class': "border-0",
    'type': "range",
    'min': "0",
    'max': "5",
    'step': "0.25",
    'list': "tickmarks",
    'name': "rating",
    'id': "rangeInput",
    'oninput': "output.value = rangeInput.value",
}
class ShtoLiberForm(forms.Form):
    liber_id = forms.IntegerField(label='liber_id', required=True, widget=forms.HiddenInput())

class HiqLiberForm(forms.Form):
    lbr_id = forms.IntegerField(label='lbr_id', required=True, widget=forms.HiddenInput())

class RatingForm(forms.Form):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs=range_attr), required=False)