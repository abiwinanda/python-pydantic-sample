from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, account_id):
        if account_id <= 0:
            raise ValueError(f"account_id must be positive: {account_id}")
        
        return account_id
    
    @field_validator("name")
    def validate_name_length(cls, name):
        if len(name) > 50:
            raise ValueError(f"name length must be less than or equal to 50")
        
        return name
