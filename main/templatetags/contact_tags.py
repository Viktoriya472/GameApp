from django import template
from main.forms import ContactForm

register = template.Library()


@register.inclusion_tag('main/contact/tags/form.html')
def contact_form():
    form = ContactForm
    return {'contact_form': form}
