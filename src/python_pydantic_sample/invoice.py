from enum import Enum
from typing import Optional
from .user import User
from decimal import Decimal
from pydantic import BaseModel, EmailStr, model_validator

class InvoiceStatus(str, Enum): 
    DRAFT = "draft"
    UNPAID = "unpaid"
    PAID = "paid"

class Invoice(BaseModel):
    description: str
    customer: Optional[User]
    amount: Decimal
    tax: Decimal
    status: InvoiceStatus

    # This method runs before the model is created
    @model_validator(mode='before')
    def validate_has_customer_if_non_draft(cls, values):
        customer = values.get('customer')
        status = values.get('status')

        if status != "draft" and customer is None:
            raise ValueError('non-draft invoice must have a customer')
        
        return values

    @model_validator(mode='before')
    def calculate_tax(cls, values):
        try:
            amount = Decimal(values.get('amount'))
        except:
            raise ValueError("amount is not a valid decimal")

        values['tax'] = Decimal("0.1") * amount

        return values
