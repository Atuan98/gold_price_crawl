from fastapi import Request, Response
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse

from typing import Callable
from uuid import uuid4

import time
from loguru import logger


from utils.constants import ERROR_CODE
from utils.exceptions import ServiceException


class BaseRoute(APIRoute):
    async def _format_request(self, req: Request, request_id: str) -> str:
        content_type: str = req.headers.get("content-type", "")
        if "multipart" in content_type:
            body = f", body: (content-type:{content_type})"
        elif content_type:
            body = f", (content-type:{content_type}) - body: " + (await req.body()).decode('utf-8')
        else:
            body = ""

        return f">> [Receive request] - {request_id} {req.method} {req.url} {body}"

    async def _format_response(self, res: Response, request_id: str, duration: float) -> str:
        return f"<< [Return response] - {request_id} (duration: {duration}), body: {res.body.decode('utf-8')}"

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request_id = str(uuid4())
            before = time.time()
            logger.info(await self._format_request(request, request_id))

            try:
                response: Response = await original_route_handler(request)
            except ServiceException as err:
                response = JSONResponse(status_code=200,
                                        content={"code": err.code, "message": err.detail})
            except Exception as ex:
                logger.exception(ex)
                response = JSONResponse(status_code=200,
                                        content={"code": ERROR_CODE.SERVER_ERROR, "message": "Server Error"})

            duration = time.time() - before
            logger.info(await self._format_response(response, request_id, duration))

            response.headers["X-Request-ID"] = request_id
            return response

        return custom_route_handler
