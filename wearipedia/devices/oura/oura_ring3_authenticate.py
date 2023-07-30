import base64
import hashlib
import os

import requests

__all__ = ["login", "Oura_token"]


def login(email, password):
    if len(email) == 0:  # fake the login
        token = ""
        user_id = ""
    else:
        login = requests.post(
            "https://accounts.fitbit.com/login",
            json={
                "grant_type": "password",
                "issueRefresh": False,
                "password": password,
                "username": email,
            },
        )


def Oura_token():
    """gives us access token given the login info
    Returns access token"""

    print(
        "fill the login info in this url then generate the token: ",
        "https://cloud.ouraring.com/personal-access-tokens",
        "\n",
    )
    access_token = input("Enter the resulting token: ")

    return access_token
