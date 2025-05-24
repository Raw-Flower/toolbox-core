from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='setValidationClass')
def setValidationClass(input):
    bootstrap_class = ''
    if input.help_text == 'filter_option':
        if input.errors:
            #CSS Class for only filters forms
            bootstrap_class = 'is-invalid'
    else:
        #CSS Class for others forms
        #print(input.widget_type) #Get the widget from the field
        if (input.data != None) and (input.data != []) :
            if input.errors:
                bootstrap_class = 'is-invalid'
            else:
                bootstrap_class = 'is-valid'   
    return input.as_widget(attrs={'class':'form-control '+ bootstrap_class})

@register.simple_tag(takes_context=True)
def querystring_without_page(context):
    request = context['request']
    querydict = request.GET.copy()
    querydict.pop('page',None)
    
    #Delete keys empty or duplicated
    clean_querydict = {k: v for k, v in querydict.items() if v.strip() != ''}
    
    return '&'.join([f'{k}={v}' for k,v in clean_querydict.items()])

@register.filter(name='is_image')
def is_image(filename):
    print(filename)
    if filename:
        img_ext = tuple(settings.CUSTOM_FILE_EXTENSIONS) 
        return filename.lower().endswith(img_ext)
    return False

