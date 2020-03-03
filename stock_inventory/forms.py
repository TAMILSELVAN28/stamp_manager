from django import forms


stamp_drop_down = (
    ('select', 'select'), 
    ('Rs10',10),
    ('Rs20',20),
    ('Rs50',50),
    ('Rs100',100),
    ('Rs500',500),
    ('Rs1000',1000),
    ('Rs5000',5000),
    ('Rs10000',10000),
    ('Rs15000',15000),
    ('Rs20000',20000),
    ('Rs25000',25000)
)

class Dropdown(forms.Form):  
    error_css_class = 'error'

    category = forms.ChoiceField(choices=stamp_drop_down, required=True)
