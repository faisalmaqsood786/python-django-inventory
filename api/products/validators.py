from invent.utils.helpers import validatorHelperMethod

Schema = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    },
    'description': {
        'type': 'string',
        'required': False,
        'empty': True,
    },
    'image': {
        'type': 'string',
        'required': False,
        'empty': True,
    },
    'qty': {
        'type': 'integer',
        'required':True,
        'empty': False,
    },
    'sku': {
        'type': 'string',
        'required': False,
        'empty': True,
    },
    'costPrice': {
        'type': 'string',
        'required': False,
        'empty': True,
    },
    'category': {
        'type': 'integer',
        'required': True,
        'empty': False,
    },
    'vendor': {
        'type': 'integer',
        'required': True,
        'empty': False,
    },
    'isActive': {
        'type': 'integer',
        'required': True,
        'empty': False,
    },

}

Errors = {
    'name': 'Category Name is required.',
    'description': 'description is required.',
    'image': 'image is required.',
    'qty': 'qty is required.',
    'sku': 'sku is required.',
    'costPrice': 'costPrice is required.',
    'category': 'category is required.',
    'vendor': 'vendor is required.',
}

def createProductValidator(data):
    return validatorHelperMethod(data, Schema, Errors)
