import requests
host = "https://app.dev.finux.ai/"


def health_check():
    path = "api/ping"
    response = requests.get(host+path)
    return response


def register(name, password, repeat_password):
    pass


if __name__ == "__main__":
    print(health_check())