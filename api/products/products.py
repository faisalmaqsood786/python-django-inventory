from api.models.categories import categories
from rest_framework.views import APIView
from api.products.serializer import ProductSerializer
from invent.messages import messages
from api.products.validators import createProductValidator
from invent.utils.helpers import sendResponse
from invent.exceptions.validationException import validationException
from api.models.items import items
from api.models.vendors import vendors

class Products(APIView):
    """
                @api {get} /products Get Items
                @apiVersion 1.0.0
                @apiName GetAllItems
                @apiGroup Products

                @apiSuccess {Integer} status  HTTP status code.
                @apiSuccess {Boolean} isError  shows the status of errors.
                @apiSuccess {String} message  API response message.
                @apiSuccess {Object} data  Object of Category.

                @apiSuccessExample Success-Response:
                   HTTP/1.1 200 OK
                  {
                    "isError": false,
                    "status": 200,
                    "data": [
                        {
                            "id": 1,
                            "name": "Mouse Logitech",
                            "description": "",
                            "image": null,
                            "qty": 39,
                            "sku": "fisd541",
                            "costPrice": "200.00",
                            "totalAmount": "3800.00",
                            "isActive": true,
                            "created_at": "2018-03-20T10:34:37.179204Z",
                            "updated_at": "2018-03-20T10:43:31.430563Z",
                            "category": 3,
                            "vendor": 1
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
            products = items.objects.filter(isActive=1)
            serializer = ProductSerializer(products, many=True)
            return sendResponse(messages['SUCCESSFUL'], serializer.data)

        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], str(ex))

    """
                     @api {post} /categories Create New Product
                     @apiVersion 1.0.0
                     @apiName CreateProduct
                     @apiGroup Products

                     @apiSuccess {Integer} status  HTTP status code.
                     @apiSuccess {Boolean} isError  shows the status of errors.
                     @apiSuccess {String} message  API response message.


                    @apiParamExample {json} API-Request:
                     {
                                "name":"Hello worls",
                                "description":"some desc",
                                "qty":10,
                                "sku":"85asd",
                                "costPrice":"5",
                                "category":2,
                                "vendor":1,
                                "isActive":1
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
            validationResult = createProductValidator(request.inputs)
            if not validationResult['isSuccess']:
                raise validationException(validationResult['errors'])

            getVendor = vendors.objects.get(id=request.inputs['vendor'])
            getCategory = categories.objects.get(id=request.inputs['category'])

            request.inputs['totalAmount'] = int(request.inputs['costPrice']) * int(request.inputs['qty'])

            serializer = ProductSerializer(data=request.inputs)
            if serializer.is_valid():
                serializer.save()
                return sendResponse(messages['SUCCESSFUL'], None)
            else:
                return sendResponse(messages['BAD_REQUEST'], serializer.errors)

        except categories.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)

        except vendors.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)

        except validationException as ex:
            return sendResponse(messages['BAD_REQUEST'], ex.errors)

        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], str(ex))

class ProductDetail(APIView):

    """
             @api {get} /products:id Product Details
             @apiVersion 1.0.0
             @apiName GetSingleProduct
             @apiGroup Products
             @apiParam (url Parameter) {Number} id Product Id  to get details of specific product.

             @apiSuccess {Integer} status  HTTP status code.
             @apiSuccess {Boolean} isError  shows the status of errors.
             @apiSuccess {String} message  API response message.
             @apiSuccess {Object} data  Object of Category.

             @apiSuccessExample Success-Response:
                HTTP/1.1 200 OK
               {
                    "isError": false,
                    "data": {
                        "id": 1,
                        "category": {
                            "name": "Mouse"
                        },
                        "vendor": {
                            "id": 1,
                            "image": null,
                            "isActive": true,
                            "created_at": "2018-03-20T10:32:26.682821Z",
                            "updated_at": "2018-03-20T10:32:26.683046Z"
                        },
                        "name": "Mouse Logitech",
                        "description": "",
                        "image": null,
                        "qty": 39,
                        "sku": "fisd541",
                        "costPrice": "200.00",
                        "totalAmount": "3800.00",
                        "isActive": true,
                        "created_at": "2018-03-20T10:34:37.179204Z",
                        "updated_at": "2018-03-20T10:43:31.430563Z"
                    },
                    "status": 200,
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

    def get(self, request, product_id):
        try:
            categoryQuerySet = items.objects.get(id=product_id)
            category = ProductSerializer(categoryQuerySet)
            return sendResponse(messages['SUCCESSFUL'], category.data)
        except categories.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)
        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], None)

    """
                 @api {put} /products:id Product Update 
                 @apiVersion 1.0.0
                 @apiName UpdateProduct
                 @apiGroup Categories
                 @apiParam (url Parameter) {Number} category_id Category Id  to update specific category.

                 @apiSuccess {Integer} status  HTTP status code.
                 @apiSuccess {Boolean} isError  shows the status of errors.
                 @apiSuccess {String} message  API response message.


                @apiParam (Body Parameter) {String} name Name of the category.
                @apiParam (Body Parameter) {Number} gender GenderID of the category.
                @apiParamExample {json} API-Request:

                 {
                "name":"Hello worls",
                "description":"some desc",
                "qty":10,
                "sku":"85asd",
                "costPrice":"5",
                "category":2,
                "vendor":1,
                "isActive":1
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

    def put(self, request, product_id):
        try:
            validationResult = createProductValidator(request.inputs)
            if not validationResult['isSuccess']:
                raise validationException(validationResult['errors'])

            getProduct = items.objects.get(id=product_id)
            getVendor = vendors.objects.get(id=request.inputs['vendor'])
            getCategory = categories.objects.get(id=request.inputs['category'])

            request.inputs['totalAmount'] = int(request.inputs['costPrice']) * int(request.inputs['qty'])

            prod_serializer = ProductSerializer(
                getProduct, data=request.inputs)
            if prod_serializer.is_valid():
                prod_serializer.save()
                return sendResponse(messages['SUCCESSFUL'], prod_serializer.data)
            else:
                return sendResponse(messages['BAD_REQUEST'], prod_serializer.errors)

        except items.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)
        except vendors.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)
        except categories.DoesNotExist:
            return sendResponse(messages['REQUIRED_DATA_NOT_FOUND'], None)

        except validationException as ex:
            return sendResponse(messages['BAD_REQUEST'], ex.errors)
        except Exception as ex:
            return sendResponse(messages['INTERNAL_SERVER_ERROR'], str(ex))
