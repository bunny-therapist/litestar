from typing import TYPE_CHECKING

from starlite.types import MiddlewareProtocol

if TYPE_CHECKING:
    from starlette.types import ASGIApp, Receive, Scope, Send

    from starlite.config import CompressionConfig


class CompressionMiddleware(MiddlewareProtocol):
    def __init__(self, app: "ASGIApp", config: "CompressionConfig") -> None:
        """
        Compression Middleware Wrapper

        This is a wrapper allowing for generic compression configuration / handler middleware

        Args:
            app: The 'next' ASGI app to call.
            config: An instance of [CompressionConfig][starlite.config.CompressionConfig]
        """
        self.handler = config.to_middleware(app=app)

    async def __call__(self, scope: "Scope", receive: "Receive", send: "Send") -> None:
        return await self.handler(scope, receive, send)
