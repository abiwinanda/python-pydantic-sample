from .invoice import Invoice
from .user import User

def main():
    create_users()
    create_invoices()

def create_users():
    # Creating user by calling User()
    user1 = User(
        name="user1",
        email="user1@gmail.com",
        account_id=123
    )

    print(user1.model_dump_json())
    print()

    # Creating user by unpacking a dictionary
    user2_data = {
        "name": "user2",
        "email": "user2@gmail.com",
        "account_id": 321
    }

    user2 = User(**user2_data)
    print(user2.model_dump_json())
    print()

    # Creating a user from raw json
    user3_json = '{"name": "user3", "email": "user3@gmail.com", "account_id": 231}'

    user3 = User.model_validate_json(user3_json)
    print(user3.model_dump_json())
    print()

    # Creating a user with invalid data
    try:
        User(
            name="invalidUser",
            email="invalidUser@gmail.com",
            # invalid (negative number)
            account_id=-10
        )
    except ValueError as e:
        print(e)
        print()

    try:
        User(
            # invalid (more than 50 chars)
            name="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            email="invalidUser@gmail.com",
            account_id=10
        )
    except ValueError as e:
        print(e)
        print()

    try:
        User(
            # invalid (more than 50 chars)
            name="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            email="invalidUser@gmail.com",
            # invalid (negative number)
            account_id=-10
        )
    except ValueError as e:
        print(e)
        print()

    # Print the errors in list of dict format
    try:
        User(
            # invalid (more than 50 chars)
            name="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
            # invalid (incorrect email format)
            email="invalidUser",
            # invalid (negative number)
            account_id=-10
        )
    except ValueError as e:
        print(e.errors())
        print()

def create_invoices():
    customer = User(
        name="customer",
        email="customer@gmail.com",
        account_id=1
    )

    # Create a valid invoice
    valid_invoice = Invoice(
        description="Netflix monthly fee",
        customer=customer,
        # or Decimal("24.99") also works
        amount="24.99",
        status="unpaid"
    )

    print(valid_invoice.model_dump_json())
    print()

    # Create an invalid invoices
    try:
        Invoice(
            description="Netflix monthly fee",
            customer=customer,
            amount="24.99",
            # invalid status (not a value of InvoiceStatus enum)
            status="open"
        )
    except ValueError as e:
        print(e.errors())
        print()

    try:
        Invoice(
            description="Netflix monthly fee",
            customer=customer,
            # invalid amount (not numerical)
            amount="aaa",
            status="draft"
        )
    except ValueError as e:
        print(e.errors())
        print()

    try:
        Invoice(
            description="Netflix monthly fee",
            # invalid customer (not a User object)
            customer=123,
            amount="5000",
            status="draft"
        )
    except ValueError as e:
        print(e.errors())
        print()

    try:
        Invoice(
            # invalid description (empty description)
            description=None,
            customer=customer,
            amount="5000",
            status="draft"
        )
    except ValueError as e:
        print(e.errors())
        print()

    try:
        Invoice(
            description="Netflix monthly fee",
            # invalid customer (must not be null if status is not draft)
            customer=None,
            amount="5000",
            status="unpaid"
        )
    except ValueError as e:
        print(e)
        print()
