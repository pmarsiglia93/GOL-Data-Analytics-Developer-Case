import traceback

from typing import Annotated, Any, Dict

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config.settings import settings
from app.security.auth import decrypt_credentials


# Authentication

HTTP_BEARER = HTTPBearer()


def get_credentials(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTP_BEARER)],
    request: Request
) -> Dict[str, Any]:
    try:
        assert decrypt_credentials(credentials.credentials) == settings.AUTH_TOKEN_PASS

    except Exception as exception:
        traceback.print_exc()

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return decrypt_credentials(credentials.credentials)
