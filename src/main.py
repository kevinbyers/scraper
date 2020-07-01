from datetime import date

import selenium
from selenium import webdriver

from selenium.webdriver import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

USERNAME = "jcribb"
PASSWORD = "Thor#2019"
CUSTOMER_ZIP_CODE = 72719

ADDRESS_lOGIN_PAGE = "https://saconnect.stateauto.com/"
ADDRESS_PERSONAL_AUTO = "https://std-spa-personal.stateauto.com/auto/submission/customer-info"

LOGIN_USER_FIELD = '//*[@id="eid-username-input"]'
LOGIN_PASS_FIELD = '//*[@id="eid-password-input"]'
LOGIN_BUTTON = '//*[@id="eid-login"]/form/div[2]/div[2]/button'

QUOTE_MENU = '//*[@id="salesfunl_quote_button"]'
PERSONAL_AUTO_QUOTE_BUTTON = '//*[@id="salesfunl Personal Auto"]'
POLICY_EFFECTIVE_DATE_FIELD = '//*[@id="block-sa-sales-service-funnel-sales-service-funnel"]/div/sales-service-funnel/div/div[12]/div/div[1]/md-datepicker/div/input'
ZIP_CODE_FIELD = '//*[@id="input_10"]'
START_YOUR_QUOTE_BUTTON = '//*[@id="salesfunl start quote button"]'

# Navigate to login page
driver.get(ADDRESS_lOGIN_PAGE)

# Log In
driver.find_element_by_xpath(LOGIN_USER_FIELD).send_keys(USERNAME)
driver.find_element_by_xpath(LOGIN_PASS_FIELD).send_keys(PASSWORD)
driver.find_element_by_xpath(LOGIN_BUTTON).click()

# # Create Auto Quote
# driver.get(ADDRESS_PERSONAL_AUTO)
driver.find_element_by_xpath(QUOTE_MENU).click()
driver.find_element_by_xpath(PERSONAL_AUTO_QUOTE_BUTTON).click()
driver.find_element_by_xpath(POLICY_EFFECTIVE_DATE_FIELD).send_keys(date.today().strftime("%m/%d/%y"))
driver.find_element_by_xpath(ZIP_CODE_FIELD).send_keys(CUSTOMER_ZIP_CODE)

# driver.implicitly_wait(2,2)
# driver.find_element_by_xpath(START_YOUR_QUOTE_BUTTON).tap()
#
# print(driver.find_element_by_id("salesfunl start quote button"))
# element = driver.find_element_by_id("salesfunl start quote button")
# print("is displayed: " + element.is_displayed())
# print("is selected: " + element.is_selected())
# print("ID: " + element.id)
# print(element.location)


# startQuoteElement = driver.find_element_by_xpath(START_YOUR_QUOTE_BUTTON)
# startQuoteElement = driver.find_element_by_id("sf-quote-button")
# ActionChains(driver).move_to_element(startQuoteElement).click()
# driver.find_element_by_xpath(START_YOUR_QUOTE_BUTTON).click()

# driver.quit();

