import logging
import pytest

# logger = logging.getLogger()


@pytest.fixture(scope='session', autouse=True)
def logger():
    import logging.config
    logging.config.fileConfig('../../logging.ini')
    return logging.getLogger()