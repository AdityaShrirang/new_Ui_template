from playwright.async_api import expect

from automation.libs_local.authn.ui.login_to_homepage import Login, LoginPagePaths

from automation.logger import log


class QuickActionPath:
    Add_device_link_path = " //a[text()='Add Device']"
    Add_device_btn = " //button[contains(text(),'Add Devices')]"
    Select_Device_Type = "//h1[contains(text(),'Select Device Type')]"
    Device_Subscriptions = "//span[contains(text(),'Device Subscriptions')]"
    Device_Sub_btn = "//button[contains(text(),'Add Device Subscription')]"
    Add_Device_Sub_title="//h2[contains(text(),'Add Device Subscription')]"
    url = "https://mira.ccs.arubathena.com/"
    home_page_title = "div[class='container'] span"
    unable_signin_xpath = "//p[text()='Unable to sign in']"


class QuickActionPage(object):
    def __init__(self):
        self.selectors = QuickActionPath()
        log.info(f"Initialize {__name__}")

    def verify_selectAddDevice_link(self, page ):
        page.wait_for_load_state()
        page.wait_for_selector(self.selectors.Add_device_link_path).click()
        page.wait_for_selector(self.selectors.Add_device_btn).click()
        page.locator(self.selectors.Select_Device_Type).is_visible()
        page.go_back()

    def verify_DeviceSubscriptions_link(self, page):
        page.wait_for_selector(self.selectors.Device_Subscriptions).click()
        page.locator(self.selectors.Device_Sub_btn).click()
        page.locator(self.selectors.Add_Device_Sub_title).is_visible()

    def verify_login_error_msg(self, page):
        page.wait_for_load_state()
        act_error= page.wait_for_selector(self.selectors.unable_signin_xpath).inner_text()
        expected_error = "Unable to sign in"
        if act_error == expected_error:
            return True
        else:
            return False

    def veriy_Home_page_title(self,page):
        page.wait_for_load_state()
        error_msg = page.wait_for_selector(self.selectors.home_page_title).inner_text()
        expected_error_msg = "HPE GreenLake"
        if error_msg == expected_error_msg:
            return True
        else:
            return False

