from invent.utils.helpers import validatorHelperMethod

updateCategorySchema = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    }
}

categoriesErrors = {
    'name': 'Category Name is required.',
}

def updateCategoryValidator(data):
    return validatorHelperMethod(data, updateCategorySchema, categoriesErrors)
