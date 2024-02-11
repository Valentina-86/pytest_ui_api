import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from configuration.ConfigProvider import ConfigProvider

class AuthPage:
    
    def __init__(self, driver: WebDriver) -> None:
        url = ConfigProvider().get("ui", "base_url")
        self.__url = url+"/login"
        self.__driver = driver
        
    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    
    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.ID, 'username').send_keys(email)
        self.__driver.find_element(By.ID, 'login-submit').click()
        self.__driver.find_element(By.ID, 'password').send_keys(password)
        self.__driver.find_element(By.ID, 'login-submit').click()

        # WebDriverWait(self.__driver, 46).until(EC.presence_of_element_located((By.ID, 'trello-root')))

    

        