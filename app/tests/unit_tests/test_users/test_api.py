import pytest

@pytest.mark.asyncio(scope="session")
async def test_adc(prepare_database):
    assert 1 == 1