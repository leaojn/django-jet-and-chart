from jet.dashboard.modules import DashboardModule, LinkListSettingsForm, LinkListItemForm
from core.models import Provider
from django import forms
from django.template.loader import render_to_string


class ProviderRecent(DashboardModule):
    title = 'Quantidade de coxinhas'
    template = 'dashboard_modules/provider.html'
    limit = 2
    column = 0
    ajax_load = False
    detelable = False
    draggable = False

    def init_with_context(self, context):
        self.children = Provider.objects.all()


class CardsModule(DashboardModule):
    # title = 'Quantidade de coxinhas'
    template = 'dashboard_modules/cards.html'
    limit = 20
    ajax_load = True
    column = 0

    detelable = False
    draggable = False
    style = "background-color: #ecf2f6; box-shadow:none;padding: 0px!important;margin: 0px!important;"

    class Media:
        css = ()
        js = ()

    def init_with_context(self, context):
        self.children = Provider.objects.all()

    def render(self):
        self.init_with_context(self.context)
        print(self.get_context_data())
        return render_to_string(self.template, self.get_context_data())

# class LinkList(DashboardModule):
#     title = 'Links'
#     template = 'jet.dashboard/modules/link_list.html'
#     layout = 'stacked'
#     children = []
#     settings_form = LinkListSettingsForm
#     child_form = LinkListItemForm
#     child_name = 'Link'
#     child_name_plural = 'Links'

#     def __init__(self, title=None, children=list(), **kwargs):
#         children = list(map(self.parse_link, children))
#         kwargs.update({'children': children})
#         super(LinkList, self).__init__(title, **kwargs)

#     def settings_dict(self):
#         return {
#             'layout': self.layout
#         }

#     def load_settings(self, settings):
#         self.layout = settings.get('layout', self.layout)

#     def store_children(self):
#         return True

#     def parse_link(self, link):
#         if isinstance(link, (tuple, list)):
#             link_dict = {'title': link[0], 'url': link[1]}
#             if len(link) >= 3:
#                 link_dict['external'] = link[2]
#             return link_dict
#         elif isinstance(link, (dict,)):
#             return link


# class LinkListSettingsForm(forms.Form):
#     layout = forms.ChoiceField(label='Layout', choices=(
#         ('stacked', 'Stacked'), ('inline', 'Inline')))


# class LinkListItemForm(forms.Form):
#     url = forms.CharField(label='URL')
#     title = forms.CharField(label='Title')
#     external = forms.BooleanField(label='External link', required=False)
