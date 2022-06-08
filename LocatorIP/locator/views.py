from django.views.generic import TemplateView
from .forms import IPForm
from django.shortcuts import render
from .rapidapi import result


def check_data(i_string):
    ip_list = i_string.split('.')
    if len(ip_list) == 4:
        good = True
        for i_num in ip_list:
            if not i_num.isdigit() or 255 < int(i_num) or int(i_num) < 0:
                good = False
        if good:
            return i_string


class LocatorIPView(TemplateView):
    template_name = 'locator/locator.html'
    ip_form = IPForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['ip_form'] = self.ip_form
        return context

    def post(self, request, *args, **kwargs):
        ip_form = IPForm(request.POST)
        if ip_form.is_valid() and check_data(ip_form.cleaned_data['IP']):
            ip = ip_form.cleaned_data['IP']
            i_result = result(ip)
            try:
                continent = i_result['continent']['name']
                country = i_result['country']['name']
                city = i_result['city']
                latitude = i_result['latitude']
                longitude = i_result['longitude']
                is_good = True
                return render(request, self.template_name, {'ip_form': ip_form, 'is_good': is_good,
                                                            'continent': continent, 'country': country, 'city': city,
                                                            'latitude': latitude, 'longitude': longitude})
            except TypeError:
                return render(request, self.template_name,
                              {'ip_form': ip_form, 'message': 'Результаты не найдены, '
                                                              'либо введенные данные не корректны'})
        else:
            return render(request, self.template_name, {'ip_form': ip_form, 'message': 'Введенные данные не корректны, '
                                                                                       'пожалуйста, повторите ввод:'})
