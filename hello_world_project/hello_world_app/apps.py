from django.apps import AppConfig


class ApiHelloWorldAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello_world_app'

    def ready(self):
        import hello_world_app.signals
