from fastapi_users.authentication import AuthenticationBackend, JWTStrategy, CookieTransport

SECRET = "IAMGAY"

cookie_transport = CookieTransport(cookie_max_age=86400, cookie_samesite="none")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=86400)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
