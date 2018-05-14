define({ "api": [
  {
    "type": "delete",
    "url": "/categories:category_id",
    "title": "Category Delete",
    "version": "1.0.0",
    "name": "DeleteCategory",
    "group": "Categories",
    "parameter": {
      "fields": {
        "url Parameter": [
          {
            "group": "url Parameter",
            "type": "Number",
            "optional": false,
            "field": "category_id",
            "description": "<p>Category Id  to update specific category.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>HTTP status code.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "isError",
            "description": "<p>shows the status of errors.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>API response message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n \"status\": 200,\n \"isError\": false,\n \"message\": \"Successful\",\n }",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>Internal Server Error.</p>"
          }
        ],
        "404 Resource not found": [
          {
            "group": "404 Resource not found",
            "optional": false,
            "field": "ResourceNotFound",
            "description": "<p>Requested data/resource not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "\n\nHTTP/1.1 500 Internal Server Error\n{\n     \"status\": 500,\n     \"isError\": True,\n     \"message\": \"Internal Server Error\",\n}\n\n HTTP/1.1 404 Resource not found\n{\n     \"status\": 404,\n     \"isError\": true,\n     \"message\": \"Requested data/resource not found\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/getCategories/category_api.py",
    "groupTitle": "Categories"
  },
  {
    "type": "post",
    "url": "/categories",
    "title": "Create New Categore",
    "version": "1.0.0",
    "name": "CreateCategory",
    "group": "CategoriesNew",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>HTTP status code.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "isError",
            "description": "<p>shows the status of errors.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>API response message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n \"status\": 200,\n \"isError\": false,\n \"message\": \"Successful\",\n }",
          "type": "json"
        }
      ]
    },
    "parameter": {
      "fields": {
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of the category.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "API-Request:",
          "content": "\n{\n    \"name\": \"HP Laptops\",\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>Internal Server Error.</p>"
          }
        ],
        "404 Resource not found": [
          {
            "group": "404 Resource not found",
            "optional": false,
            "field": "ResourceNotFound",
            "description": "<p>Requested data/resource not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "\n\nHTTP/1.1 500 Internal Server Error\n{\n     \"status\": 500,\n     \"isError\": True,\n     \"message\": \"Internal Server Error\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/getCategories/category_api.py",
    "groupTitle": "CategoriesNew"
  },
  {
    "type": "get",
    "url": "/categories",
    "title": "Get Categories",
    "version": "1.0.0",
    "name": "GetCategories",
    "group": "CategoriesNew",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>HTTP status code.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "isError",
            "description": "<p>shows the status of errors.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>API response message.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>Object of Category.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "   HTTP/1.1 200 OK\n  {\n    \"status\": 200,\n    \"isError\": false,\n    \"data\": [\n        {\n            \"id\": 2,\n            \"name\": \"HP Laptops\",\n            \"image\": null,\n            \"created_at\": \"2018-03-20T07:12:20.678392Z\",\n            \"updated_at\": \"2018-03-20T07:12:20.678640Z\"\n        },\n        {\n            \"id\": 3,\n            \"name\": \"Mouse\",\n            \"image\": null,\n            \"created_at\": \"2018-03-20T10:33:59.366142Z\",\n            \"updated_at\": \"2018-03-20T10:33:59.366195Z\"\n        },\n        {\n            \"id\": 4,\n            \"name\": \"Mousee\",\n            \"image\": null,\n            \"created_at\": \"2018-03-22T06:06:02.805953Z\",\n            \"updated_at\": \"2018-03-22T06:06:02.805991Z\"\n        }\n    ],\n    \"arabicMessage\": \"تم بنجاح\",\n    \"message\": \"Successful\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>Internal Server Error.</p>"
          }
        ],
        "404 Resource not found": [
          {
            "group": "404 Resource not found",
            "optional": false,
            "field": "ResourceNotFound",
            "description": "<p>Requested data/resource not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "\n\nHTTP/1.1 500 Internal Server Error\n{\n     \"status\": 500,\n     \"isError\": True,\n     \"message\": \"Internal Server Error\",\n}\n\n HTTP/1.1 404 Resource not found\n{\n     \"status\": 404,\n     \"isError\": true,\n     \"message\": \"Requested data/resource not found\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/getCategories/category_api.py",
    "groupTitle": "CategoriesNew"
  },
  {
    "type": "get",
    "url": "/categories:category_id",
    "title": "Category Details",
    "version": "1.0.0",
    "name": "SpecificCategoryDetails",
    "group": "Categories",
    "parameter": {
      "fields": {
        "url Parameter": [
          {
            "group": "url Parameter",
            "type": "Number",
            "optional": false,
            "field": "category_id",
            "description": "<p>Category Id  to get details of specific category.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>HTTP status code.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "isError",
            "description": "<p>shows the status of errors.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>API response message.</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>Object of Category.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n \"status\": 200,\n \"isError\": false,\n \"message\": \"Successful\",\n \"data\": {\n         \"id\": 1,\n         \"name\": \"Home Service\",\n         \"created_at\": \"2017-08-15T05:56:55.232406Z\",\n         \"updated_at\": \"2017-08-15T05:56:55.232406Z\",\n }",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>Internal Server Error.</p>"
          }
        ],
        "404 Resource not found": [
          {
            "group": "404 Resource not found",
            "optional": false,
            "field": "ResourceNotFound",
            "description": "<p>Requested data/resource not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "\n\nHTTP/1.1 500 Internal Server Error\n{\n     \"status\": 500,\n     \"isError\": True,\n     \"message\": \"Internal Server Error\",\n}\n\n HTTP/1.1 404 Resource not found\n{\n     \"status\": 404,\n     \"isError\": true,\n     \"message\": \"Requested data/resource not found\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/getCategories/category_api.py",
    "groupTitle": "Categories"
  },
  {
    "type": "put",
    "url": "/categories:category_id",
    "title": "Category Update",
    "version": "1.0.0",
    "name": "SpecificCategoryUpdate",
    "group": "Categories",
    "parameter": {
      "fields": {
        "url Parameter": [
          {
            "group": "url Parameter",
            "type": "Number",
            "optional": false,
            "field": "category_id",
            "description": "<p>Category Id  to update specific category.</p>"
          }
        ],
        "Body Parameter": [
          {
            "group": "Body Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>Name of the category.</p>"
          },
          {
            "group": "Body Parameter",
            "type": "Number",
            "optional": false,
            "field": "gender",
            "description": "<p>GenderID of the category.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "API-Request:",
          "content": "\n{\n    \"name\": \"Mouse\",\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Integer",
            "optional": false,
            "field": "status",
            "description": "<p>HTTP status code.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "isError",
            "description": "<p>shows the status of errors.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>API response message.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": " HTTP/1.1 200 OK\n{\n \"status\": 200,\n \"isError\": false,\n \"message\": \"Successful\",\n }",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "500 Internal Server Error": [
          {
            "group": "500 Internal Server Error",
            "optional": false,
            "field": "InternalServerError",
            "description": "<p>Internal Server Error.</p>"
          }
        ],
        "404 Resource not found": [
          {
            "group": "404 Resource not found",
            "optional": false,
            "field": "ResourceNotFound",
            "description": "<p>Requested data/resource not found.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Error-Response:",
          "content": "\n\nHTTP/1.1 500 Internal Server Error\n{\n     \"status\": 500,\n     \"isError\": True,\n     \"message\": \"Internal Server Error\",\n}\n\n HTTP/1.1 404 Resource not found\n{\n     \"status\": 404,\n     \"isError\": true,\n     \"message\": \"Requested data/resource not found\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/getCategories/category_api.py",
    "groupTitle": "Categories"
  }
] });
