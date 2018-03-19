messages = {

    'SUCCESSFUL': {
        'status': 200,
        'isError': False,
        'message': 'Successful',
        'arabicMessage': 'تم بنجاح'
    },
    'BAD_REQUEST': {
        'status': 400,
        'isError': True,
        'message': 'Bad request. Please try again with proper parameters.',
        'arabicMessage': 'اقتراح غير موفق. يرجى إعادة المحاولة باستخدام ال؟ المناسبة.'
    },
    'FORBIDDEN': {
        'status': 403,
        'isError': True,
        'message': 'Not Allowed.',
        'arabicMessage': 'غير مسموح.'
    },
    'REQUIRED_DATA_NOT_FOUND': {
        'status': 404,
        'isError': True,
        'message': 'Requested data/resource not found.',
        'arabicMessage': 'لم يتم إيجاد المعلومات والمصادر المطلوبة.'
    },
    'INTERNAL_SERVER_ERROR': {
        'status': 500,
        'isError': True,
        'message': 'Internal Server Error.',
        'arabicMessage': 'Internal Server Error.'
    },
    'LOGIN_SUCCESSFUL': {
        'status': 200,
        'isError': False,
        'message': 'Login Successful.',
        'arabicMessage': 'تم تسجيل الدخول بنجاح.'
    },
    'LOGIN_FAILED': {
        'status': 200,
        'isError': True,
        'message': 'Provided email/password is incorrect.',
        'arabicMessage': 'البريد الإلكتروني/كلمة المرور التي تم إدخالها غير صحيحة.'
    }
}
