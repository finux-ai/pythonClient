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


class LoginRequest:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def to_json(self):
        return {
            "email": self.email,
            "password": self.password
        }


class AlphaRegister:
    def __init__(self, email, password, repeat_password, alpha_key):
        self.email = email
        self.password = password
        self.repeat_password = repeat_password
        self.alpha_key = alpha_key

    def to_json(self):
        return {
            "email": self.email,
            "password": self.password,
            "repeatPassword": self.repeat_password,
            "alphakey": self.alpha_key
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


class AccessRefreshToken(object):
    def __init__(self, data):
        self.access_token = data.get("accessToken")
        self.refresh_token = data.get("refreshToken")


class ProfileRequest:
    def __init__(self, business_ID, company, first_name, last_name):
        self.business_ID = business_ID
        self.company = company
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        return {
            "businessID": self.business_ID,
            "company": self.company,
            "firstname": self.first_name,
            "surename": self.last_name
        }

class ChangePasswordRequest:
    def __init__(self, old_password, new_password, repeat_password):
        self.old_password = old_password
        self.new_password = new_password
        self.repeat_password = repeat_password

    def to_json(self):
        return {
            "oldPassword": self.old_password
            "newPassword": self.new_password
            "repeatPassword": self.repeat_password
        }

class FeedbackRequest:
    def __init__(self, message, reply):
        self.message = message
        self.reply = reply

    def to_json(self):
        return {
            "message": self.message,
            "reply": self.reply
        }

class BankAccountRequest:
    def __init__(self, bank_code, extra_secret, save_secret, secret, username):
        self.bank_code = bank_code
        self.extra_secret = extra_secret
        self.save_secret = save_secret
        self.secret = secret
        self.username = username

    def to_json(self):
        return {
            "bankCode": self.bank_code,
            "extraSecret": self.extra_secret,
            "saveSecret": self.save_secret,
            "secret": self.secret,
            "username": self.username
        }

class ChangeAccountRequest:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return {
            "data": json.dumps(self.data)
        }

    # finish up -- dumps?

class Account:
    def __init__(self, accountID, flag):
        self.accountID = accountID
        self.flag = flag
        # finish up