import pytest
from Pages import login_page,landing_page,configure_site_page
from TestCases import test_login

@pytest.mark.usefixtures("setup")
class Test_deviceDiscovery():

    def test_deviceDiscovery(self):
        Login_page = login_page.Login_page(self.driver)
        Login_page.emailAddressField("rohit@yopmail.com")
        Login_page.passwordField("Kiwi@2018")
        Login_page.loginButton()

        ChangeSite = landing_page.Landing_page(self.wait)
        ChangeSite.configureSiteOption()
        ChangeSite.siteDropDown()
        ChangeSite.kiwitech_QA_2_network_22_Site()

        ConfigurePage = configure_site_page.Configure_site_page(self.wait, self.discoveryWait)
        ConfigurePage.checkBox_for_device_discovery()
        ConfigurePage.discoverButton()
        ConfigurePage.discoveryProgressBar()
