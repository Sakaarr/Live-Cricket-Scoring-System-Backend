import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import cricket.routing

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()  # Initialize Django

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        cricket.routing.websocket_urlpatterns
    ),
})