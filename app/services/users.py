# app/services/users.py
from app.security.password_policy import hash_password, validate_password_policy


class User:
    def __init__(self, email: str, password_hash: str):
        self.email = email
        self.password_hash = password_hash


class UserRepository:
    def save(self, user: User) -> User:
        return user


def create_user(email: str, password: str, repository: UserRepository) -> User:
    policy_result = validate_password_policy(password)
    if not policy_result.valid:
        raise ValueError(policy_result.reason or "Invalid password.")

    user = User(email=email.lower(), password_hash=hash_password(password))
    return repository.save(user)

async def load_user(user_id: int) -> str:
    repository = UserRepository()
    user = await repository.find(user_id)

    # Bug: user may be None
    if user is None:
        # Handle the case where the user is not found, e.g., raise an exception or return None
        raise ValueError(f"User with ID {user_id} not found")
    return user.name
