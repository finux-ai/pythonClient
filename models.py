class Status:
    def __init__(self, message):
        self.message = message


class Data(object):
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


class RegisterRequest(object):
    def __init__(self, email, password, repeat_password):
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

    def to_json(self):
        return {
            "email": self.email,
            "password": self.password,
            "repeatPassword": self.repeat_password
        }


class ApiResponse(object):
    def __init__(self, status, data, code):
        self.status = status
        self.data = data
        self.code = code

    @staticmethod
    def from_json(json):
        return ApiResponse(
            json.get("status").get("message"),
            json.get("data"),
            json.get("code")
        )
