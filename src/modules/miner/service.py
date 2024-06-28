from core.utils import extract_username_from_url
from typing import Union
import instaloader


class InstaMinerService:
    """
    Service class to scrape Instagram profile data using Instaloader.

    Methods:
        scrape_instagram_profile(username_or_url: str) -> dict:
            Scrapes and returns profile details for a given Instagram username or URL.

    Dependencies:
        - instaloader: Python package for downloading Instagram data.

    Usage:
        # Example Usage:
        insta_miner = InstaMinerService()
        profile_details = insta_miner.scrape_instagram_profile('username')

    Raises:
        ValueError: Raised if an invalid Instagram URL is provided or if the profile does not exist.
        Exception: Raised for any other unexpected errors during profile scraping.
    """

    @staticmethod
    def scrape_instagram_profile(username_or_url: str) -> dict:
        """
        Scrapes and returns profile details for a given Instagram username or URL.

        Args:
            username_or_url (str): The Instagram username or URL of the profile to scrape.

        Returns:
            dict: A dictionary containing profile details including username, avatar URL,
                  following count, follower count, post count, privacy status, verification status,
                  bio, hashtags in bio, and full name.

        Raises:
            ValueError: If an invalid Instagram URL is provided or if the profile does not exist.
            Exception: For any other unexpected errors during profile scraping.
        """
        # Extract username if URL is provided
        if (
            username_or_url.startswith("http://")
            or username_or_url.startswith("https://")
            or username_or_url is None
        ):
            username = extract_username_from_url(username_or_url)
            if not username:
                raise ValueError("Invalid Instagram URL provided.")
        else:
            username = username_or_url

        # Initialize Instaloader
        loader = instaloader.Instaloader()

        try:
            # Load the profile from Instagram
            profile = instaloader.Profile.from_username(loader.context, username)

            # Get profile details
            user_details = {
                "username": profile.username,
                "avatarUrl": profile.profile_pic_url,
                "followingCount": profile.followees,
                "followerCount": profile.followers,
                "postCount": profile.mediacount,
                "isPrivate": profile.is_private,
                "isVerified": profile.is_verified,
                "bio": profile.biography,
                "biographyHashtags": profile.biography_hashtags,
                "fullName": profile.full_name,
            }

            return user_details

        except instaloader.exceptions.ProfileNotExistsException:
            raise ValueError(f"The profile '{username}' does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while scraping the profile: {e}")
