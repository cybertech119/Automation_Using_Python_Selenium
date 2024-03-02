from selenium.webdriver.common.by import By


class Login_page():
    def __init__(self, driver):
        self.driver = driver

    def emailAddressField(self, emailId):
        emailAddress = self.driver.find_element(By.XPATH, "//input[@id='emailAddress']")
        emailAddress.send_keys(emailId)

    def passwordField(self, password):
        passwordText = self.driver.find_element(By.XPATH, "//input[@id='userPassword']")
        passwordText.send_keys(password)

    def loginButton(self):
        loginButton = self.driver.find_element(By.XPATH, "//button[normalize-space()='Log In']")
        loginButton.click()