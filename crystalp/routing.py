from django.urls import path
# from django.conf.urls import url

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from frontend.consumers import FrontendConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("frontend/stream/", FrontendConsumer),
        ]),
    ),

})
