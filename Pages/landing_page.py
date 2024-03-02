from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Landing_page():
    def __init__(self, wait):
        self.wait = wait

    def configureSiteOption(self):
        configureSiteOption = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//a[@placement='end'][normalize-space()='Configure Site'])[1]")))
        configureSiteOption.click()

    def siteDropDown(self):
        siteDropDown = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='header-site-menu']")))
        siteDropDown.click()

    def kiwitech_QA_2_network_22_Site(self):
        site = self.wait.until(EC.presence_of_element_located((By.XPATH, """(//li[normalize-space()="Kiwitech's QA 2.0 ODIN PC 2 Network 22"])[1]""")))
        site.click()
        time.sleep(2)