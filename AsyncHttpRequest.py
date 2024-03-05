import aiohttp
import json as j

class Request:
    session = None

    class Response:
        def __init__(self, status_code, msg="succeed", data=None, content=None):
            self.status_code = status_code
            self.msg = msg
            self.data = data
            self.content = content

        def json(self):
            return j.loads(self.data)

    @staticmethod
    async def post(url, headers: dict = {}, data: dict = {}):
        if not Request.session:
            Request.session = aiohttp.ClientSession()

        try:
            res = await Request.session.post(url, headers=headers, json=data)

            data = None
            content = None

            if "Content-Type" in headers and ('text' in headers["Content-Type"] or 'json' in headers["Content-Type"]):
                data = await res.text()
            else:
                content = await res.read()
            return Request.Response(
                status_code=res.status,
                data=data,
                content=content
            )
        except aiohttp.ClientError as e:
            return Request.Response(
                status_code=400,
                msg=str(e)
            )
        except Exception as e:
            return Request.Response(
                status_code=500,
                msg=str(e)
            )

    @staticmethod
    async def get(url, headers: dict = {}, data: dict = {}):
        if not Request.session:
            Request.session = aiohttp.ClientSession()

        try:
            res = await Request.session.get(url, headers=headers, json=data)
            data = None
            content = None

            if "Content-Type" in headers and ('text' in headers["Content-Type"] or 'json' in headers["Content-Type"]):
                data = await res.text()
            else:
                content = await res.read()
            return Request.Response(
                status_code=res.status,
                data=data,
                content=content
            )
        except aiohttp.ClientError as e:
            return Request.Response(
                status_code=400,
                msg=str(e)
            )
        except Exception as e:
            return Request.Response(
                status_code=500,
                msg=str(e)
            )