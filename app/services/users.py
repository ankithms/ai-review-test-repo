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


def reset_password(user: User, new_password: str) -> User:
    policy_result = validate_password_policy(new_password)
    if not policy_result.valid:
        raise ValueError(policy_result.reason or "Invalid password.")
    user.password_hash = hash_password(new_password)
    return user

def change_email(user: User, new_email: str) -> User:
    user.email = new_email
    return user
