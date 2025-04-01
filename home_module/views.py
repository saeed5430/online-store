from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from site_module.models import SiteSettings, FooterLinkBox,FooterLink,Slider


# Create your views here.

#class HomeView(View):
 #   def get(self,request):
  #      return render(request, 'home_module/index_page.html')
class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders']=Slider.objects.filter(is_active=True)
        return context

def contact_page(request):
    return render(request,'home_module/contact_page.html')
def site_header_component(request):
    setting = SiteSettings.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html',context)
def site_footer_component(request):
    setting = SiteSettings.objects.filter(is_main_setting=True).first()
    footer_link_box = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        'footer_link_box': footer_link_box,
    }
    return render(request, 'shared/site_footer_component.html',context)

class AboutUs(TemplateView):
    template_name = 'AboutUs.html'
    def get_context_data(self, **kwargs):
        site_settings = SiteSettings.objects.filter(is_main_setting=True).first()
        context = super(AboutUs,self).get_context_data(**kwargs)
        context['site_setting'] = site_settings
        return context