import pytest


global list_id
@pytest.fixture(scope='class')
def browser(request):
    "pytest fixture for browser"
    return request.config.getoption("-B")

@pytest.fixture(scope='class')
def browserstack_flag(request):
    "pytest fixture for browserstack flag"
    return request.config.getoption("-M")

@pytest.fixture(scope='class')
def browser_version(request):
    "pytest fixture for browser version"
    return request.config.getoption("-V")

@pytest.fixture(scope='class')
def platform(request):
    "pytest fixture for platform"
    return request.config.getoption("-P")

@pytest.fixture(scope='class')
def os_version(request):
    "pytest fixture for os version"
    return request.config.getoption("-O")

@pytest.fixture(scope='class')
def bstk_server(request):
    "pytest fixture for os version"
    return request.config.getoption("-S")


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="chrome",
                     help="Browser. Valid options are firefox, ie and chrome")
    parser.addoption("-M", "--browserstack_flag",
                     dest="browserstack_flag",
                     default="N",
                     help="Run the test in Browserstack: Y or N")
    parser.addoption("-V", "--ver",
                     dest="browser_version",
                     help="The version of the browser: a whole number",
                     default=45)
    parser.addoption("-P", "--platform",
                     dest="platform",
                     help="The operating system: Windows 7, Linux",
                     default="Windows")
    parser.addoption("-O", "--os_version",
                     dest="os_version",
                     help="The operating system: xp, 7",
                     default="7")
    parser.addoption("-S", "--bstk_server",
                     dest="bstk_server",
                     help="The BlueStacks Server: wp-s, qa-internal, www",
                     default="qa-internal")