password = "123"

def divide(a, b):
    return a / b

user_id = request.query_params.get("user_id")
query = f"SELECT * FROM users WHERE id = {user_id}"
result = db.execute(query)