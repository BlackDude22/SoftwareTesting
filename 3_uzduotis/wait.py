from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # element = browser.find_element_by_id("price")
    button = browser.find_element_by_id("book")

    wait = WebDriverWait(browser, 13)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()

    x = int(browser.find_element_by_id("input_value").text)

    inp = browser.find_element_by_id("answer")

    inp.send_keys(str(math.log(math.fabs(12*math.sin(x)))))

    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
	print("")
