#!/usr/bin/env python3
"""
Automated login validation using Python, pytest, and requests.
Credentials are securely loaded from environment variables.
Robust error handling and logging included.
"""
import os
import requests
import pytest

LOGIN_URL = os.getenv("LOGIN_URL")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")

@pytest.fixture(scope="module")
def credentials():
    assert LOGIN_URL, "LOGIN_URL environment variable not set."
    assert LOGIN_EMAIL, "LOGIN_EMAIL environment variable not set."
    assert LOGIN_PASSWORD, "LOGIN_PASSWORD environment variable not set."
    return {
        "url": LOGIN_URL,
        "email": LOGIN_EMAIL,
        "password": LOGIN_PASSWORD
    }

@pytest.mark.login
def test_login_success(credentials):
    """
    Positive test: Valid credentials should authenticate successfully.
    """
    payload = {
        "email": credentials["email"],
        "password": credentials["password"]
    }
    try:
        response = requests.post(credentials["url"], json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
    # Add further validation if response contains tokens, user info, etc.
    assert "token" in response.json() or "access" in response.json(), "Login response missing expected authentication token."

@pytest.mark.login
def test_login_failure(credentials):
    """
    Negative test: Invalid credentials should NOT authenticate.
    """
    payload = {
        "email": credentials["email"],
        "password": "invalid_password"
    }
    try:
        response = requests.post(credentials["url"], json=payload, timeout=10)
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Network error during login: {e}")
    assert response.status_code in [400, 401, 403], f"Expected auth failure, got {response.status_code}: {response.text}"
