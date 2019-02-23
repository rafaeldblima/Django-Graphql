from django.contrib.auth.models import User


def create_admin_user(sender, **kwargs):
    if not User.objects.filter(username='admin').first():
        User.objects.create_superuser('admin', 'admin@admin.mail', '123qweasd')
