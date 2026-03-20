from fastapi import APIRouter, Form, HTTPException, status
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.conf import settings

auth_router = APIRouter(prefix="/login", tags=["login"])


@auth_router.post("", status_code=status.HTTP_200_OK)
def login(username: str = Form(...), password: str = Form(...)):
    if username != settings.username or password != settings.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    expire = datetime.now(timezone.utc) + timedelta(
        hours=settings.access_token_expire_hours
    )
    token_data = {"sub": username, "exp": expire}
    token = jwt.encode(token_data, settings.secret_key, algorithm=settings.algorithm)
    return {"access_token": token, "token_type": "bearer"}
