import requests
import json

from models import RegisterRequest, ApiResponse, AccessRefreshToken, LoginRequest

host = "https://app.dev.finux.ai/"


def health_check():
    path = "api/ping"
    response = requests.get(host+path)
    return response


def register(name, password, repeat_password):
    path = "api/register"

    # create request body
    request = RegisterRequest(name, password, repeat_password)

    # send register credentials
    response = requests.post(host+path, data=request.to_json())

    # map to response model
    json_data = json.loads(response.text)
    api_response = ApiResponse.from_json(json_data)

    # create register data
    return AccessRefreshToken(api_response.data)


def login(name, password):
    path = "/api/login"

    # create request body
    request = LoginRequest(name, password)

    # send register credentials
    response = requests.post(host + path, data=request.to_json())

    # map to response model
    json_data = json.loads(response.text)
    api_response = ApiResponse.from_json(json_data)

    # create register data
    return AccessRefreshToken(api_response.data)

def alpha_register(email, password, repeat_password, alpha_key):
    path = "/api/alpharegister"
    response = requests.post(host+path)
    # something
    pass

def profile(business_ID, company, first_name, last_name):
    path = "/api/user/profile"
    response = requests.put(host+path)
    # something
    pass

def fetch_data():
    path = "/api/user/profile"
    response = requests.get(host+path)
    # something
    pass

def change_password(new_password, old_password, repeat_password):
    path = "/api/user/changepw"
    response = requests.put(host+path)
    # something
    pass

def feedback(message, reply):
    path = "/api/user/feedback"
    response = requests.post(host+path)
    # something
    pass

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

def get_forecast():
    path = "/api/user/intelligence/forecast"
    response = requests.get(host+path)
    # something
    pass

def get_partners():
    path = "/api/user/intelligence/procentpartner/{span}"
    response = requests.get(host+path)
    # something
    pass

def get_top_customers_suppliers():
    path = "/api/user/intelligence/toppartner/{request_type}/{span}"
    response = requests.get(host+path)
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
    register_data = register("bba1210@web.de", "Meinpasswort#12", "Meinpasswort#12")


