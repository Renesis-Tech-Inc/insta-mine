from pydantic import BaseModel
from typing import List
from core.base_model import BaseResponse


class ProfileDetails(BaseModel):
    username: str
    avatarUrl: str
    followingCount: int
    followerCount: int
    postCount: int
    isPrivate: bool
    isVerified: bool
    bio: str
    biographyHashtags: List[str]
    fullName: str


class ProfileResponse(BaseResponse):
    payload: ProfileDetails  # Override payload to use ProfileDetails for this response
