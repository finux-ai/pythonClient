import json

import requests

from helpers import auth_header, api_response
from models import RegisterRequest, AccessRefreshToken, LoginRequest, ProfileRequest, AccessToken, \
    ChangePasswordRequest, FeedbackRequest, FetchData

host = "https://app.dev.finux.ai"
def get_selected_account():
    path = "/api/user/connector/bank/account/{accountid}"


def handle_expired_access_token(request, tokens, path):
    access_token = access_for_refresh_token(tokens.refresh_token)
    headers = auth_header(access_token)
    data = None
    if request is not None:
        data = request.to_json()
    return requests.put(host + path, headers=headers, data=data)


def access_for_refresh_token(token):
    path = "/api/refreshtoken"
    request = {
        "refreshToken": token
    }

    response = requests.post(host + path, data=request)
    data = json.loads(response.text)

    return AccessToken.from_json(data)

def health_check():
    path = "/api/ping"
    response = requests.get(host+path)
    return response


def register(name, password, repeat_password):
    path = "/api/register"

    request = RegisterRequest(name, password, repeat_password)

    # send register credentials
    response = requests.post(host+path, data=request.to_json())

    # create register data
    result = api_response(response)
    return AccessRefreshToken(result.data)


def login(name, password):
    path = "/api/login"

    request = LoginRequest(name, password)

    # send register credentials
    response = requests.post(host + path, data=request.to_json())

    # create register data
    result = api_response(response)
    return AccessRefreshToken(result.data)


def profile(business_ID, company, first_name, last_name, tokens):
    path = "/api/user/profile"

    # create request
    request = ProfileRequest(
        business_ID=business_ID,
        company=company,
        first_name=first_name,
        last_name=last_name
    )

    # first we try the access token
    headers = auth_header(tokens.access_token)
    response = requests.put(host+path, headers=headers, data=request.to_json())

    # if access token is expired, we send the request token to fetch another access token
    if response.status_code == 401:
        response = handle_expired_access_token(request=request, tokens=tokens, path=path)

    # map to response model
    result = api_response(response)
    return result.status


def fetch_data(tokens):
    path = "/api/user/profile"

    # first we try the access token
    headers = auth_header(tokens.access_token)
    response = requests.get(host+path, headers=headers)

    # if access token is expired, we send the request token to fetch another access token
    if response.status_code == 401:
        response = handle_expired_access_token(request=None, tokens=tokens, path=path)

    # map to response model
    result = api_response(response)
    return FetchData(result.data)


def change_password(new_password, repeat_password, old_password, tokens):
    path = "/api/user/changepw"

    # create request
    request = ChangePasswordRequest(
        new_password=new_password,
        old_password=old_password,
        repeat_password=repeat_password
    )

    # first we try the access token
    headers = auth_header(tokens.access_token)
    response = requests.put(host + path, headers=headers, data=request.to_json())

    # if access token is expired, we send the request token to fetch another access token
    if response.status_code == 401:
        response = handle_expired_access_token(request=request, tokens=tokens, path=path)

    # map to response model
    result = api_response(response)
    return result.status


def feedback(message, reply, tokens):
    path = "/api/user/feedback"

    # create request
    request = FeedbackRequest(
        message=message,
        reply=reply
    )

    # first we try the access token
    headers = auth_header(tokens.access_token)
    response = requests.put(host + path, headers=headers, data=request.to_json())

    # if access token is expired, we send the request token to fetch another access token
    if response.status_code == 401:
        response = handle_expired_access_token(request=request, tokens=tokens, path=path)

    # map to response model
    result = api_response(response)
    return result.status


def connect_bank_account(bank_code, extra_secret, save_secret, secret, username):
    path = "/api/user/connector/bank/account"
    response = requests.post(host+path)
    # something
    pass


def get_all_bank_accounts():
    path = "/api/user/connector/bank/account"
    response = requests.get(host+path)
    # something
    pass

def get_selected_account():
    path = "/api/user/connector/bank/account/{accountid}"
    response = requests.get(host + path)
    pass

def disconnect_selected_account():
    path = "/api/user/connector/bank/account/{bankloginid}"
    response = requests.delete(host + path)
    pass

def get_all_account_IDs():
    path = "/api/user/connector/bank/ids"
    response = requests.get(host + path)
    pass

def get_selected_account_IDs():
    path = "/api/user/connector/bank/accountids"
    response = requests.get(host + path)
    pass

def change_account_selection():
    path = "/api/user/connector/bank/accountids"
    response = requests.patch(host + path)
    pass

def add_GMI_account():
    path = "/api/user/connector/gmi/account"
    response = requests.post(host + path)
    pass

def get_all_invoices():
    path = "/api/user/connector/gmi/invoices"
    response = requests.get(host + path)
    pass

def get_forecast():
    path = "/api/user/intelligence/forecast"
    response = requests.get(host+path)
    # something
    pass

def get_top_customers_supplier_percent():
    path = "/api/user/intelligence/procentpartner/{span}"
    response = requests.get(host+path)
    # something
    pass

def get_top_customers_suppliers_currency():
    path = "/api/user/intelligence/toppartner/{request_type}/{span}"
    response = requests.get(host + path)
    # something
    pass

def get_smartalerts():
    path = "api/user/intelligence/smartalerts"
    response = requests.get(host+path)
    # something
    pass

def branches():
    path = "api/ressources/branches"
    response = requests.get(host+path)
    # something
    pass


if __name__ == "__main__":
    # test register function

    tokens = login("bba3@web.de", "Meinpasswort#14")
    profile("Business123", "My Co", "Roger", "Smith", tokens)
    print(data.firstname, data.surename, data.business_ID)



