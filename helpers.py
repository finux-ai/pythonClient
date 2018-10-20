import json

from models import ApiResponse


def auth_header(token):
    return {"Authorization": "Bearer "+token}


def api_response(response):
    # map to response model
    json_data = json.loads(response.text)
    return ApiResponse.from_json(json_data)
