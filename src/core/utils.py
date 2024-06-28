import re


def format_response(status_code: int, message: str, payload: dict = None) -> dict:
    """
    Formats a response dictionary with the given status code, message, and optional payload.

    Args:
        status_code (int): The HTTP status code.
        message (str): The message to include in the response.
        payload (dict, optional): The data payload to include if any. Defaults to None.

    Returns:
        dict: A dictionary representing the formatted response.

    Example:
        >>> format_response(200, "Success", {"data": "value"})
        {'statusCode': 200, 'message': 'Success', 'payload': {'data': 'value'}}

        >>> format_response(404, "Not Found")
        {'statusCode': 404, 'message': 'Not Found'}
    """
    response = {"statusCode": status_code, "message": message}
    if payload is not None:
        response["payload"] = payload
    return response


def extract_username_from_url(url: str) -> str:
    """
    Extracts the username from an Instagram URL.

    Args:
        url (str): The Instagram URL from which to extract the username.

    Returns:
        str: The extracted username if found, otherwise None.

    Example:
        >>> extract_username_from_url("https://www.instagram.com/username/")
        'username'

        >>> extract_username_from_url("https://instagram.com/username")
        'username'

        >>> extract_username_from_url("https://www.instagram.com/")
        None
    """
    # Regex pattern to extract username from Instagram URL
    pattern = re.compile(r"https?://(www\.)?instagram\.com/([A-Za-z0-9._]+)/?")
    match = pattern.match(url)
    if match:
        return match.group(2)
    return None
