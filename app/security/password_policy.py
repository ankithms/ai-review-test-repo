# app/security/password_policy.py
from dataclasses import dataclass


@dataclass(frozen=True)
class PasswordPolicyResult:
    valid: bool
    reason: str | None = None


MIN_PASSWORD_LENGTH = 12


def validate_password_policy(password: str) -> PasswordPolicyResult:
    if len(password) < MIN_PASSWORD_LENGTH:
        return PasswordPolicyResult(False, "Password must be at least 12 characters.")

    if password.lower() == password or password.upper() == password:
        return PasswordPolicyResult(False, "Password must include mixed case.")

    if not any(char.isdigit() for char in password):
        return PasswordPolicyResult(False, "Password must include a number.")

    return PasswordPolicyResult(True)


def hash_password(password: str) -> str:
    return f"hashed::{password}"