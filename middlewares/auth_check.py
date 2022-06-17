import os
import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

secret_key = os.environ.get('SECRET_KEY')


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True, admin_check=False):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.admin_check = admin_check

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            isTokenValid, isAdmin = self.verify_jwt(credentials.credentials)
            if not isTokenValid:
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            else:
                if self.admin_check:
                    if not isAdmin:
                        raise HTTPException(status_code=403, detail="Access to this endpoint requires admin role.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False
        isAdmin: bool = False

        try:
            info = jwt.decode(jwtoken, key=secret_key)
            isTokenValid = True if info else False
            isAdmin = info['role'] == 'admin'
        except:
            pass

        return isTokenValid, isAdmin