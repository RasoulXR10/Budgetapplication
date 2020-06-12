from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

    # def ready(self):
    # """
    # Override this method in subclasses to run code when Django starts.
    # """
