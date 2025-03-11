from .user import User

def main():
    # Creating user by calling User()
    user1 = User(
        name="user1",
        email="user1@gmail.com",
        account_id=123
    )

    print(user1.model_dump_json())

    # Creating user by unpacking a dictionary
    user2_data = {
        "name": "user2",
        "email": "user2@gmail.com",
        "account_id": 321
    }

    user2 = User(**user2_data)
    print(user2.model_dump_json())

    # Creating a user from raw json
    user3_json = '{"name": "user3", "email": "user3@gmail.com", "account_id": 231}'

    user3 = User.model_validate_json(user3_json)
    print(user3.model_dump_json())