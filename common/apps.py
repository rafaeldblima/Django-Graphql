from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CommonConfig(AppConfig):
    name = 'common'

    def ready(self):
        from . import receivers  # NOQA
        post_migrate.connect(receivers.create_admin_user, sender=self)
