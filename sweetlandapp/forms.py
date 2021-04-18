from django import forms


CHOICES = (
    ('chocolate', 'chocolate'),
    ('candy', 'candy'),
    ('cake', 'cake'),
    ('marshmallow', 'marshmallow'),
    ('cookies', 'cookies'),
    ('marmalade', 'marmalade'),
    ('gingerbread', 'gingerbread'),
    ('hazelnut_cocoa_spread', 'hazelnut_cocoa_spread'),
    ('caramel', 'caramel'),
)


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=10)
    file = forms.FileField()
    description = forms.CharField(max_length=30)
    full_description = forms.CharField(max_length=255)
    product_type = forms.ChoiceField(choices=CHOICES)
    price = forms.FloatField()


class OrderForm(forms.Form):
    firstname = forms.CharField(max_length=50, required=True, label='Enter your firstname')
    lastname = forms.CharField(max_length=50, required=True, label='Enter your lastname')
    email = forms.EmailField(required=True, label='Enter your email')
    phone_number = forms.CharField(max_length=50, required=True, label='Enter your phone_number')
    delivery_time = forms.TimeField(required=True, label='Enter delivery time')
    address = forms.CharField(required=True, label='Enter your address')
    comment = forms.CharField(required=False, label='Comment')
