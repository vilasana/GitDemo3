import pytest
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("openbrowser")
class BaseClass:
    pass

