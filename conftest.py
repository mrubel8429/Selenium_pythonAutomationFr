import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(executable_path="/Users/mdrubel/Documents/AutomationFramework_1/drivers/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()
    print("Test Completed")
