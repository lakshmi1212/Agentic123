#!/usr/bin/env python3
"""
Pytest login automation script using requests.
Parameters are read from environment variables for secure credential handling.
"""
import os
import requests
import pytest
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.fixture(scope="module")
def credentials():
    assert LOGIN_URL, "LOGIN_URL must be set in environment variables."
    assert LOGIN_EMAIL, "LOGIN_EMAIL must be set in environment variables."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD must be set in environment variables."
    return {
        "url": LOGIN_URL,
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }

def login_request(url, email, password):
    try:
        response = requests.post(
            url,
            json={"email": email, "password": password},
            timeout=10
        )
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        logging.error("Timeout occurred during login request.")
        pytest.fail("Timeout occurred during login request.")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
        pytest.fail(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        pytest.fail(f"Request failed: {e}")

@pytest.mark.login
def test_login_success(credentials):
    """
    Positive test: Successful login with valid credentials.
    """
    url = credentials["url"]
    email = credentials["email"]
    password = credentials["password"]
    response = login_request(url, email, password)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    json_resp = response.json()
    assert "token" in json_resp or "access_token" in json_resp, "Login response missing token."
    logging.info("Login successful and token received.")
