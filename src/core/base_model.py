from pydantic import BaseModel, Field
from typing import Optional, TypeVar

# Define a generic type variable for payload
T = TypeVar("T")


class BaseResponse(BaseModel):
    statusCode: int = Field(..., description="The HTTP status code of the response.")
    message: str = Field(
        ..., description="A message describing the result of the operation."
    )
    payload: Optional[T] = Field(
        None,
        description="Data payload containing the response data if the operation was successful.",
    )
