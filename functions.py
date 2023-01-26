import requests


def get_token_password(cr_url, username, password):
    endpoint = "/v1/authentication"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "username": username,
        "password": password
    }

    r = requests.post(url=url, headers=headers, json=payload, verify=False)
    r.raise_for_status()
    return r.json()['token']


def get_token_apikey(cr_url, username, api_key):
    endpoint = "/v1/authentication"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "username": username,
        "apiKey": api_key
    }

    r = requests.post(url=url, headers=headers, json=payload, verify=False)
    r.raise_for_status()
    return r.json()['token']


def create_gv(cr_url, token, global_value):
    endpoint = "/v1/globalvalues/values"
    url = cr_url + endpoint
    headers = {
        "Content-Type": "application/json",
        "X-Authorization": token
    }

    payload = {
        "key": global_value["name"],
        "name": global_value["name"],
        "description": global_value["description"],
        "type": global_value["type"],
        "isOverridable": str(global_value["isOverridable"]),
        "isPublic": True,
        "value": {
            "type": global_value["type"],
            str(global_value["type"]).lower(): global_value["value"]
        },
        "userId": "0"
    }
    # print(payload)
    r = requests.put(url=url, headers=headers, json=payload,
                     verify=False)  # POST method fails if gv has been already created, use PUT
    r.raise_for_status()
    return r.json()
