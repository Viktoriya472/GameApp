from django.views.generic import DetailView, UpdateView, CreateView
from main.models import Profile, Contact
from main.forms import ProfileForm, ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import newsletter_subscription, newsletter_subscription_error


class ProfileView(DetailView):
    model = Profile
    template_name = 'main/profile.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'main/profile_update.html'
    queryset = Profile.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        user = self.request.user
        context['profile_form'] = ProfileForm(
            instance=self.request.user.profile,
            initial={'first_name': user.first_name,
                     'last_name': user.last_name})
        return context

    def form_valid(self, form):
        profile = form.save(commit=False)
        user = profile.user
        user.last_name = form.cleaned_data['last_name']
        user.first_name = form.cleaned_data['first_name']
        user.save()
        profile.save()
        return HttpResponseRedirect(reverse('profile',
                                            kwargs={'pk': self.get_object().pk}))


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm

    def form_valid(self, form):
        contact = form.save(commit=False)
        if contact.email not in Contact.objects.values_list("email",flat=True):
            contact.save()
            newsletter_subscription(contact.email)
        else:
            newsletter_subscription_error(contact.email)
        return HttpResponseRedirect(reverse('news'))
