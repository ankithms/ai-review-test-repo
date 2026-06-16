password = "123"

def divide(a, b):
    return a / b

user = None

print(user.name)

# VULNERABLE / BUGGY LINE
def add_user_to_group(username, group_list=[]):
    group_list.append(username)
    return group_list