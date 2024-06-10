import pytest
from app.users.dao import UserDAO


@pytest.mark.asyncio
@pytest.mark.parametrize("user_id, email, exists", [
    (1, "test@test.com", True),
    (2, "gwyn@example.com", True),
    (3, "any@example.com", False),
])
async def test_find_user_by_id(user_id, email, exists):
    user = await UserDAO.find_by_id(user_id)

    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user