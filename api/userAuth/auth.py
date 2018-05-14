from api.models.categories import categories
from rest_framework.views import APIView
from api.getCategories.serializer import CategorySerializer
from invent.messages import messages
from api.getCategories.category_validators import updateCategoryValidator
from invent.utils.helpers import sendResponse
from invent.exceptions.validationException import validationException

class RegisterUser(APIView):

    def post(self, request, format=None):
        try:
            validationResult = CreateNewUser(request.inputs)
            if not validationResult['isSuccess']:
                raise validationException(validationResult['errors'])

            serializer = CategorySerializer(data=request.inputs)
            if serializer.is_valid():
                serializer.save()
                return sendResponse(messages['SUCCESSFUL'], None)
            else:
                return sendResponse(messages['BAD_REQUEST'], serializer.errors)

        except validationException as ex:
            return sendResponse(messages['BAD_REQUEST'], ex.errors)

        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], str(ex))
