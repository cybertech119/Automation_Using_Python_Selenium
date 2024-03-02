import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Configure_site_page():
    def __init__(self, wait, discoveryWait):
        self.wait = wait
        self.discoveryWait = discoveryWait

    def checkBox_for_device_discovery(self):
        checkBox = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='dx-checkbox-icon'])[1]")))
        checkBox.click()

    def discoverButton(self):
        discoverButton = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Discover']")))
        discoverButton.click()

    def discoveryProgressBar(self):

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h4[normalize-space()='Discovering Devices...']")))
        self.discoveryWait.until(EC.invisibility_of_element_located((By.XPATH, "//h4[normalize-space()='Discovering Devices...']")))