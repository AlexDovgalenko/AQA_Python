import pytest
import random

@pytest.mark.flaky(reruns=3)
def test_random_rerun():
    import random
    assert random.choice([True, False])

