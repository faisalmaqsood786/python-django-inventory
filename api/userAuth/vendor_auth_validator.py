from letsbookr.utils.helpers import validatorHelperMethod
vendorLoginSchema = {
    'username': {
        'type': 'string',
        'required': True,
        'maxlength': 30,
        'empty': False
    },
    'password': {
        'type': 'string',
        'required': True,
        'maxlength': 13,
        'empty': False
    },

}

vendorErrors = {
    'username': 'username is required.',
    'password': 'Password is required. Must be between 6 to 13 characters and alphanumerics'
}


def vendorLoginValidator(data):
    return validatorHelperMethod(data, vendorLoginSchema, vendorErrors)
