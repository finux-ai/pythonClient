import requests

from models import RegisterRequest

host = "https://app.dev.finux.ai/"
register_path = "api/ping"


def health_check():
    response = requests.get(host+register_path)
    return response


def register(name, password, repeat_password):
    # create request body
    body = RegisterRequest(name, password, repeat_password)

    # send register credentials
    response = requests.post(host+register_path)


    pass


if __name__ == "__main__":
    print(health_check())