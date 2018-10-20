class Status(object):
    def __init__(self, message):
        self.message = message


class Data(object):
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


class CustomError(object):
    def __init__(self, status, data, code):
        self.status = status
        self.data = data
        self.code = code

    def from_json(self, json):
        return CustomError(
            Status(json.get("status").get("message")),
            Data(json.get("data").get("accessToken"), json.get("data").get("refreshToken")),
            json.get("code")
        )


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


class RegisterLoginResponse(object):
    def __init__(self, status_message, access_token, refresh_token, code):
        self.status = Status(status_message)
        self.data = Data(access_token, refresh_token)
        self.code = code

    def from_json(self, json):
        return RegisterLoginResponse(
            json.get("status").get("message"),
            json.get("data").get("access_token"),
            json.get("data").get("refresh_token"),
            json.get("code")
        )
