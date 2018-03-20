import json
from invent.utils.helpers import autoconvert

class getRequestInputsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        inputs = {}
        for key, value in request.GET.items():
            inputs[key] = autoconvert(value)
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            for key, value in body.items():
                inputs[key] = value
            request.inputs = inputs
        except ValueError:
            request.inputs = inputs

            # Important Line
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response
