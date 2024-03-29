"""
ASGI config for svelte project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from app_svelte_van_itten.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svelte.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter([
      path("ws/uzenetek/", ChatConsumer.as_asgi())
    ])
})
