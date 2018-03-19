import jwt
import pytz
import copy
import random
import hmac
import hashlib
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.response import Response
from cerberus import Validator
from letsbookr.utils.contants import FIELD_IS_NOT_ALLOWED
from django.conf import settings

epoch = datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def sendResponse(message, payload):
    messageToSend = copy.deepcopy(message)
    data = payload
    if message['isError']:
        return sendErrorResponse(messageToSend, data)
    else:
        return sendSuccessResponse(messageToSend, data)


def sendResponseMessage(message):
    return Response(message, status=message['status'])


def sendSuccessResponse(message, data):
    if data is not None:
        message['data'] = data
    return Response(message, status=message['status'])


def sendErrorResponse(message, errors):
    if errors is not None:
        message['errors'] = errors
    return Response(message, status=message['status'])



def validatorHelperMethod(data, schema, errorDictionary):
    v = Validator()
    validatorObject = {}
    errors = {}
    validatorObject['isSuccess'] = v.validate(data, schema)
    validatorObject['validatorObject'] = v
    try:
        for key, value in v.errors.items():
            errorString = errorDictionary[key] if (
                key in errorDictionary and key in schema) else key + FIELD_IS_NOT_ALLOWED
            errors[key] = errorString
        validatorObject['errors'] = errors
    except Exception as ex:
        b = 1
    return validatorObject


def make_password(password, salt):
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    return hashlib.sha256(password + salt).hexdigest()

def make_passwordEncrpty(password, salt):
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    return hashlib.sha256(password + salt).hexdigest()


def check_password(hash, password, salt):
    """Generates the hash for a password and compares it."""
    generated_hash = make_password(password, salt)

    return hash == generated_hash

def check_passwordEncrypt(hash, password):
    """Generates the hash for a password and compares it."""
    return hash == password


def saltGenrator(len = 30):
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(len):
        chars.append(random.choice(ALPHABET))
    salt = "".join(chars)
    return salt


def boolify(s):
    if s == 'True':
        return True
    if s == 'False':
        return False
    raise ValueError("huh?")


def autoconvert(s):
    for fn in (boolify, int, float):
        try:
            return fn(s)
        except ValueError:
            pass
    return s


def tempMethod(data):
    tempData = {}
    for group in data:
        tempData[group['name']] = group['services']
    return tempData


def sendServiceResponse(success, data):
    response = {
        'isSuccess': success,
        'payload': data
    }
    return response


def convertFromJSDateTime(dateString):
    try:
        return datetime.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
    except Exception as ex:
        return False


def JsToMysqlDatetime(dateString):
    try:
        dateObject = convertFromJSDateTime(dateString)
        return dateObject.strftime('%Y-%m-%d %H:%M:%S')
    except BaseException:
        return False

def convertStrDatetimeInPython(dateTimeString,company_timezone):
    return datetime.strptime(dateTimeString,'%Y-%m-%d %I:%M%p')
    # return utc.astimezone(timezone.get_current_timezone())
def JsToMysqlDate(dateString):
    try:
        dateObject = convertFromJSDateTime(dateString)
        return dateObject.strftime('%Y-%m-%d')
    except BaseException:
        return False


def PythonToMysqlDate(dateTimeObj):
    try:
        return dateTimeObj.strftime('%Y-%m-%d')
    except BaseException:
        return False


def MysqlToPythonDate(dateString):
    try:
        return datetime.strptime(str(dateString), "%Y-%m-%d")
    except Exception as ex:
        return False


def stripEmptyObjFromArray(array):
    resultArray = []
    for value in array:
        if len(value) > 0:
            resultArray.append(value)
    return resultArray


def serviceToGroupsMapper(data):
    groups = []
    groupIds = []
    for service in data[:]:
        if service['service'] is None:
            continue
        if not service['service']['group']['id'] in groupIds:
            groupIds.append(service['service']['group']['id'])
            groupObject = {
                'name': service['service']['group']['name'],
                'id': service['service']['group']['id'],
                'services': []
            }
            if service['service']['isActive']==True or service['service']['isActive']== 1:
                tempServiceObject = {
                    'name': service['service']['name'],
                    'id': service['service']['id'],
                    'price': service['service']['price'],
                    'bufferTime': service['service']['bufferTime'],
                    'duration': service['service']['duration'],
                    # 'specialPrice': service['service']['specialPrice'],
                }
                groupObject['services'].append(tempServiceObject)
            groups.append(groupObject)
        else:
            for group in groups[:]:
                if group['id'] is service['service']['group']['id']:
                    if service['service']['isActive']==True or service['service']['isActive']== 1:

                        tempServiceObject = {
                            'name': service['service']['name'],
                            'id': service['service']['id'],
                            'price': service['service']['price'],
                            'bufferTime': service['service']['bufferTime'],
                            'duration': service['service']['duration'],
                            # 'specialPrice': service['service']['specialPrice'],
                        }
                        group['services'].append(tempServiceObject)
    return groups


def returnDayOftheWeek(dateTime):
    return datetime.weekday(dateTime)


def PythonWeekToMysqlWeek(dayNumber):
    if dayNumber == 0:  # Monday
        return 2
    if dayNumber == 1:
        return 3
    if dayNumber == 2:
        return 4
    if dayNumber == 3:
        return 5
    if dayNumber == 4:
        return 6
    if dayNumber == 5:
        return 7
    if dayNumber == 6:
        return 1


def MysqlDatesIsEqual(date1, date2):
    return (MysqlToPythonDate(date1) == MysqlToPythonDate(date2))


def createJWT(payload):
    payloadToSend = copy.deepcopy(payload)
    payloadToSend['expiry'] = unix_time_millis(
        datetime.today() + timedelta(days=7))
    payloadToSend['created_at'] = unix_time_millis(datetime.today())
    return jwt.encode(
        payloadToSend,
        settings.LETBOOKR_JWT_SECRET_KEY,
        algorithm='HS256')


def decodeJwt(token):
    return jwt.decode(
        token,
        settings.LETBOOKR_JWT_SECRET_KEY,
        algorithms=['HS256'])


def generateUniqueId(len):

    digits = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    all_chars = digits + letters
    length = len

    while True:

        val = ''.join(random.choice(all_chars) for i in range(length))

        # The following line might be faster if you only want hex digits.
        # It makes a long int with 24 random bits, converts it to hex,
        # drops '0x' from the start and 'L' from the end, then pads
        # with zeros up to six places if needed
        # val = hex(random.getrandbits(4*length))[2:-1].zfill(length)

        # test whether it contains at least one letter
        if not val.isdigit():
            break

    return val


def validateTapPayment(merchantDetails, payload):

    try:
        MerchantID = str(merchantDetails.MerchantID)
        APIKey = merchantDetails.APIKey
        RefNumber = str(payload['ref'])
        TxnResult = str(payload['result'])
        OrderID = str(payload['trackid'])
        strHash = 'x_account_id' + MerchantID + 'x_ref' + RefNumber + \
            'x_result' + TxnResult + 'x_referenceid' + OrderID + ''
        MyHashString = hmac.new(
            bytearray(
                APIKey, 'ASCII'), bytearray(
                strHash, 'ASCII'), hashlib.sha256).hexdigest()
        if MyHashString == payload['hash']:
            return True
        else:
            return False
    except Exception as ex:
        return False


def filter_unique(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output




def iequal(a, b):
    try:
       return a.upper() == b.upper()
    except AttributeError:
       return a == b


def generateServiceDurations(step):
    if step <= 60:
        step = step
    else:
        step = 60
    hourNumber = 0
    minutes = 0
    string = ''
    array = ['0min']

    while (hourNumber < 12):
        minutes += step
        if (minutes == 60):
            hourNumber += 1
            minutes = 0
        if (hourNumber):
            string += str(hourNumber) + 'h '

        if (minutes):
            string += str(minutes) + 'min'

        array.append(string.strip())
        string = ''
    return array