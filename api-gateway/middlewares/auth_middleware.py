from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from config.settings import Settings

settings = Settings()

class AuthMiddleware:
    async def __call__(self, request: Request, call_next):
        if request.url.path in settings.PUBLIC_PATHS:
            return await call_next(request)

        auth = HTTPBearer()
        credentials: HTTPAuthorizationCredentials = await auth(request)

        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authentication credentials")

        try:
            payload = jwt.decode(credentials.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            request.state.user = payload
        except JWTError:
            raise HTTPException(status_code=403, detail="Invalid token or expired token")

        return await call_next(request)