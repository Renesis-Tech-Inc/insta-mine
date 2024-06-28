from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from typing import Annotated, Union
from .service import InstaMinerService
from core.utils import format_response
from .model import ProfileResponse

import instaloader

# Create an APIRouter instance for Instagram mining related endpoints
router = APIRouter(prefix="/insta", tags=["InstaMiner"])


@router.get("/profile")
async def mineProfile(
    instaMinerService: Annotated[InstaMinerService, Depends(InstaMinerService)],
    username_or_url: Union[str, None] = None,
) -> ProfileResponse:
    """
    Endpoint to mine Instagram user profile data.

    Args:
        instaMinerService (InstaMinerService): The service to scrape Instagram profiles.
        username_or_url (Union[str, None]): The Instagram username or URL of the profile to mine.

    Returns:
        JSONResponse: A formatted response with the mined profile data.

    Raises:
        HTTPException: Various HTTP exceptions for profile not found, private profile, bad request, and server error.
    """
    try:
        profile = instaMinerService.scrape_instagram_profile(username_or_url)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=format_response(
                status_code=200, message="Success", payload={"profile": profile}
            ),
        )
    except instaloader.exceptions.ProfileNotExistsException:
        raise HTTPException(
            status_code=404, detail=f"The profile '{username_or_url}' does not exist."
        )
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        raise HTTPException(
            status_code=403,
            detail=f"The profile '{username_or_url}' is private and not followed by you.",
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
