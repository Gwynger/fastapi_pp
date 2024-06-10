import pytest

from httpx import AsyncClient

@pytest.mark.parametrize("email, password, status_code", [
    ("random@ns.com", "qwerty", 200),
    ("random@ns.com", "qwErty", 409),
    ("ram@ns.com", "qwasd", 200),
    ("abce", "qwErty", 422),
])


async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code

@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200),
    ("gwyn@example.com", "programm3r", 200),
    ("wrong@person.com", "wrong", 401)
])
async def test_login_user(email,password,status_code, ac: AsyncClient):
    response = await ac.post("auth/login", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code
