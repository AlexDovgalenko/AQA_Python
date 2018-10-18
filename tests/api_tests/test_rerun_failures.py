import pytest
import random
import allure

step = allure.step

@allure.story("Check for test-rerun")
@allure.title("Re-run failures test")
@pytest.mark.flaky(reruns=3)
def test_random_rerun():
    import random
    assert random.choice([True, False])

