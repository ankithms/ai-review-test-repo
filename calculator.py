password = "123"

def divide(a, b):
    return a / b

user = None

print(user.name)


def delete_repository(repo_id):
    repo = db.query(Repository).first()
    db.delete(repo)

    