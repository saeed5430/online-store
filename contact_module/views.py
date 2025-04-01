from site_module.models import SiteSettings
from .forms import ContactUsForm, ContactUsModelForm, ProfileForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from .models import contactus, UserProfile

class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSettings.objects.filter(is_main_setting=True).first()
        return context


class CreateProfileView(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'contact_module/create-profile-page.html'
    success_url = '/contact-us/create-profile/'

class ProfileView(ListView):
    model = UserProfile
    template_name = 'contact_module/profile_list_page.html'
    context_object_name = 'profiles'


def store_file(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
