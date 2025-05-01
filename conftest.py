import pytest


def pytest_addoption(parser):
    parser.addoption("--runzmq", action="store_true", help="run zmq tests")


def pytest_configure(config):
    config.addinivalue_line("markers", "zmq: mark test as zmq")  # Register the marker


def pytest_collection_modifyitems(items, config):
    skip_slow = not config.getoption("--runzmq")

    if skip_slow:
        skip_zmq_marker = pytest.mark.skip(reason="Skipping zmq tests")
        for item in items:
            if "zmq" in item.keywords:
                item.add_marker(skip_zmq_marker)
