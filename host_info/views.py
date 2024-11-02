from django.http import HttpResponse
from django.template import loader

from host_info.models import AnsibleHostSummary


def ansible_host_summary(request):
    context = {
        'host_summary': AnsibleHostSummary.objects.order_by('hostname').all()
    }
    template = loader.get_template('AnsibleHostSummary.html')
    return HttpResponse(template.render(context, request))

