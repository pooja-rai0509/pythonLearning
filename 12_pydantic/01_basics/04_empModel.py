from typing import Optional
from pydantic import BaseModel, Field
import re       # regular expression

#min_length - minimum character necessary
#mx_length - maximum character necessary
#ge - greater than or equal to
#gt - only greater than
#le - less than or equal to
#lt - only less than
#regex - compex(not recommended)

class Employee(Basemodel):
    id: int
    name: str = Field(
        ...,        #it means required field
        min_length=3,   #min character
        mx_length=50,   #max character
        description="Employee name",
        examples="Pooja Rai"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )

class User(BaseModel):
    email: str = Field(
        ...;
        regex=r''
    )
    phone: str = Field(
        ...,
        regex=r''
    )
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )