define({ "api": [
  {
    "type": "get",
    "url": "/categories:category_id",
    "title": "Category Details (Disable)",
    "version": "1.0.0",
    "name": "Specific_Category_Details",
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
          "content": " HTTP/1.1 200 OK\n{\n \"status\": 200,\n \"isError\": false,\n \"message\": \"Successful\",\n \"data\": {\n         \"id\": 1,\n         \"name\": \"Home Service\",\n         \"image\": \"http://res.cloudinary.com/bookr/image/upload/v1502870268/Home_Service_xjfix9.png\",\n         \"created_at\": \"2017-08-15T05:56:55.232406Z\",\n         \"updated_at\": \"2017-08-15T05:56:55.232406Z\",\n         \"gender\": {\n             \"id\": 3,\n             \"gender\": \"B\",\n             \"created_at\": \"2017-08-15T05:55:56.599978Z\",\n             \"updated_at\": \"2017-08-15T05:55:56.599978Z\"\n         }\n     }\n }",
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
    "title": "Category Update (Disable)",
    "version": "1.0.0",
    "name": "Specific_Category_Update",
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
          "content": "\n{\n    \"name\": \"Home Service\",\n    \"gender\"  :1\n}",
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
