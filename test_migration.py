import logging
import pytest


LOG = logging.getLogger(__name__)

from automation.libs_local.authn.ui.login_to_homepage import Login
from automation.tests.cop.test_Quick_actions import QuickActionPage
from automation.tests.cop.test_Quick_actions import QuickActionPath


@pytest.mark.Quick_actions
def test_verify_Quick_actions(plcontext):
    """
         "The test verifies Navigating through Quick actions"
    """
    page = plcontext[0].new_page()
    page.goto(QuickActionPath.url)

    loginobj = Login("soltest.user15@glcpsoltest.net", "Qwerty@123")
    loginobj.login_acct(page)

    LOG.info(f"Login Successfully : ")
    QuickActionPageObj = QuickActionPage()
    QuickActionPageObj.verify_selectAddDevice_link(page)
    LOG.info(f"Device link Successfully work")
    QuickActionPageObj.verify_DeviceSubscriptions_link(page)
    LOG.info(f"Subscriptions link Successfully work")


@pytest.mark.login_error
def test_verify_login_error(plcontext):
    """
         "The test verifies Invalid user login with wrong username and password"
    """
    page = plcontext[0].new_page()
    page.goto(QuickActionPath.url)

    loginobj = Login("soltest.user15@gmail.com", "Qwerty")
    loginobj.login_acct(page)
    LOG.info(f"Login Successfully : ")
    QuickActionPageObj = QuickActionPage()
    QuickActionPageObj.verify_login_error_msg(page)
    LOG.info(f"error message appears on the screen: ")


@pytest.mark.home_page_title
def test_verify_home_title(plcontext):
    """
         "The test verifies  HPE Green Lake Badge in the GLCP global header in the homepage"
    """
    page = plcontext[0].new_page()
    page.goto(QuickActionPath.url)

    loginobj = Login("soltest.user15@glcpsoltest.net", "Qwerty@123")
    loginobj.login_acct(page)
    LOG.info(f"Login Successfully : ")
    QuickActionPageObj = QuickActionPage()
    QuickActionPageObj.veriy_Home_page_title(page)
    LOG.info(f"homepage title appears on the screen : ")

