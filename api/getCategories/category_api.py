from api.models.categories import categories
from rest_framework.views import APIView
from api.getCategories.serializer import CategorySerializer
from invent.messages import messages
from api.getCategories.category_validators import updateCategoryValidator
from invent.utils.helpers import sendResponse
from invent.exceptions.validationException import validationException

class CategoryData(APIView):
    """
                @api {get} /categories Get Categories
                @apiVersion 1.0.0
                @apiName GetCategories
                @apiGroup CategoriesNew

                @apiSuccess {Integer} status  HTTP status code.
                @apiSuccess {Boolean} isError  shows the status of errors.
                @apiSuccess {String} message  API response message.
                @apiSuccess {Object} data  Object of Category.

                @apiSuccessExample Success-Response:
                   HTTP/1.1 200 OK
                  {
                    "status": 200,
                    "isError": false,
                    "data": [
                        {
                            "id": 2,
                            "name": "HP Laptops",
                            "image": null,
                            "created_at": "2018-03-20T07:12:20.678392Z",
                            "updated_at": "2018-03-20T07:12:20.678640Z"
                        },
                        {
                            "id": 3,
                            "name": "Mouse",
                            "image": null,
                            "created_at": "2018-03-20T10:33:59.366142Z",
                            "updated_at": "2018-03-20T10:33:59.366195Z"
                        },
                        {
                            "id": 4,
                            "name": "Mousee",
                            "image": null,
                            "created_at": "2018-03-22T06:06:02.805953Z",
                            "updated_at": "2018-03-22T06:06:02.805991Z"
                        }
                    ],
                    "arabicMessage": "تم بنجاح",
                    "message": "Successful"
                }

                @apiError (500 Internal Server Error) InternalServerError Internal Server Error.
                @apiError (404 Resource not found) ResourceNotFound Requested data/resource not found.

                @apiErrorExample {json} Error-Response:


                HTTP/1.1 500 Internal Server Error
                {
                     "status": 500,
                     "isError": True,
                     "message": "Internal Server Error",
                }

                 HTTP/1.1 404 Resource not found
                {
                     "status": 404,
                     "isError": true,
                     "message": "Requested data/resource not found",
                }

             """

    def get(self, request, format=None):
        try:
            category_data = categories.objects.all()
            serializer = CategorySerializer(category_data, many=True)
            return sendResponse(messages['SUCCESSFUL'], serializer.data)

        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], str(ex))

    """
                     @api {post} /categories Create New Categore
                     @apiVersion 1.0.0
                     @apiName CreateCategory
                     @apiGroup CategoriesNew

                     @apiSuccess {Integer} status  HTTP status code.
                     @apiSuccess {Boolean} isError  shows the status of errors.
                     @apiSuccess {String} message  API response message.


                    @apiParam (Body Parameter) {String} name Name of the category.
                    @apiParamExample {json} API-Request:

                    {
                        "name": "HP Laptops",
                    }

                     @apiSuccessExample Success-Response:
                        HTTP/1.1 200 OK
                       {
                        "status": 200,
                        "isError": false,
                        "message": "Successful",
                        }

                     @apiError (500 Internal Server Error) InternalServerError Internal Server Error.
                     @apiError (404 Resource not found) ResourceNotFound Requested data/resource not found.

                     @apiErrorExample {json} Error-Response:


                     HTTP/1.1 500 Internal Server Error
                     {
                          "status": 500,
                          "isError": True,
                          "message": "Internal Server Error",
                     }
                  """

    def post(self, request, format=None):
        try:
            validationResult = updateCategoryValidator(request.inputs)
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

class CategoryDetail(APIView):

    """
             @api {get} /categories:category_id Category Details
             @apiVersion 1.0.0
             @apiName SpecificCategoryDetails
             @apiGroup Categories
             @apiParam (url Parameter) {Number} category_id Category Id  to get details of specific category.

             @apiSuccess {Integer} status  HTTP status code.
             @apiSuccess {Boolean} isError  shows the status of errors.
             @apiSuccess {String} message  API response message.
             @apiSuccess {Object} data  Object of Category.

             @apiSuccessExample Success-Response:
                HTTP/1.1 200 OK
               {
                "status": 200,
                "isError": false,
                "message": "Successful",
                "data": {
                        "id": 1,
                        "name": "Home Service",
                        "created_at": "2017-08-15T05:56:55.232406Z",
                        "updated_at": "2017-08-15T05:56:55.232406Z",
                }

             @apiError (500 Internal Server Error) InternalServerError Internal Server Error.
             @apiError (404 Resource not found) ResourceNotFound Requested data/resource not found.

             @apiErrorExample {json} Error-Response:


             HTTP/1.1 500 Internal Server Error
             {
                  "status": 500,
                  "isError": True,
                  "message": "Internal Server Error",
             }

              HTTP/1.1 404 Resource not found
             {
                  "status": 404,
                  "isError": true,
                  "message": "Requested data/resource not found",
             }

          """

    def get(self, request, category_id):
        try:
            categoryQuerySet = categories.objects.get(id=category_id)
            category = CategorySerializer(categoryQuerySet)
            return sendResponse(messages['SUCCESSFUL'], category.data)
        except categories.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)
        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], None)

    """
                 @api {put} /categories:category_id Category Update 
                 @apiVersion 1.0.0
                 @apiName SpecificCategoryUpdate
                 @apiGroup Categories
                 @apiParam (url Parameter) {Number} category_id Category Id  to update specific category.

                 @apiSuccess {Integer} status  HTTP status code.
                 @apiSuccess {Boolean} isError  shows the status of errors.
                 @apiSuccess {String} message  API response message.


                @apiParam (Body Parameter) {String} name Name of the category.
                @apiParam (Body Parameter) {Number} gender GenderID of the category.
                @apiParamExample {json} API-Request:

                {
                    "name": "Mouse",
                }

                 @apiSuccessExample Success-Response:
                    HTTP/1.1 200 OK
                   {
                    "status": 200,
                    "isError": false,
                    "message": "Successful",
                    }

                 @apiError (500 Internal Server Error) InternalServerError Internal Server Error.
                 @apiError (404 Resource not found) ResourceNotFound Requested data/resource not found.

                 @apiErrorExample {json} Error-Response:


                 HTTP/1.1 500 Internal Server Error
                 {
                      "status": 500,
                      "isError": True,
                      "message": "Internal Server Error",
                 }

                  HTTP/1.1 404 Resource not found
                 {
                      "status": 404,
                      "isError": true,
                      "message": "Requested data/resource not found",
                 }

              """

    def put(self, request, category_id):
        try:
            validationResult = updateCategoryValidator(request.inputs)
            if not validationResult['isSuccess']:
                raise validationException(validationResult['errors'])
            categoryQuerySet = categories.objects.get(id=category_id)
            serializer = CategorySerializer(
                categoryQuerySet, data=request.inputs)
            if serializer.is_valid():
                serializer.save()
                return sendResponse(messages['SUCCESSFUL'], None)
        except categories.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)
        except validationException as ex:
            return sendResponse(messages['BAD_REQUEST'], ex.errors)
        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], None)

    """
                     @api {delete} /categories:category_id Category Delete
                     @apiVersion 1.0.0
                     @apiName DeleteCategory
                     @apiGroup Categories
                     @apiParam (url Parameter) {Number} category_id Category Id  to update specific category.

                     @apiSuccess {Integer} status  HTTP status code.
                     @apiSuccess {Boolean} isError  shows the status of errors.
                     @apiSuccess {String} message  API response message.



                     @apiSuccessExample Success-Response:
                        HTTP/1.1 200 OK
                       {
                        "status": 200,
                        "isError": false,
                        "message": "Successful",
                        }

                     @apiError (500 Internal Server Error) InternalServerError Internal Server Error.
                     @apiError (404 Resource not found) ResourceNotFound Requested data/resource not found.

                     @apiErrorExample {json} Error-Response:


                     HTTP/1.1 500 Internal Server Error
                     {
                          "status": 500,
                          "isError": True,
                          "message": "Internal Server Error",
                     }

                      HTTP/1.1 404 Resource not found
                     {
                          "status": 404,
                          "isError": true,
                          "message": "Requested data/resource not found",
                     }

                  """

    def delete(self, request, category_id, format=None):
        try:
            categoryQuerySet = categories.objects.get(id=category_id)
            categoryQuerySet.delete()
            return sendResponse(messages['SUCCESSFUL'], None)
        except categories.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)
        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], None)
