from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from dashboard_modules import ProviderRecent, CardsModule


class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.children.append(CardsModule(column=1))
        self.children.append(CardsModule(column=0))
        self.children.append(ProviderRecent())
