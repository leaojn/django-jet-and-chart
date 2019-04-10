from django.conf.urls import url
from django.contrib import messages
from django.shortcuts import redirect
from jet.dashboard import dashboard
from core.utils.utils import DatabaseManager


def update_database(request):
    database_manager = DatabaseManager()
    database_manager.update_database()

    messages.success(request, 'Database was successfully updated')

    return redirect(request.META.get('HTTP_REFERER'))


# This method registers view's url
dashboard.urls.register_urls([
    path(
        '^update_database/',
        update_database,
        name='update-database'
    ),
])
