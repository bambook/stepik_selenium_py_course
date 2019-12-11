from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

#k = browser.find_element_by_xpath('//*[@id="price"]')
button = browser.find_element_by_id("book")

h5 = WebDriverWait(browser, 11).until(
          EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100')
      )
#print(f"h5 = {h5}")
button.click()

# ================================================================
# <span class="nowrap"> What is ln(abs(12*sin(x))), where x =  </span>
# <span class="nowrap" id="input_value">931</span>

# <input class="form-control" name="text" id="answer" type="text" required="">
input_value = browser.find_element_by_id("input_value")

x = input_value.text

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# Ввести ответ в текстовое поле.
# <input class="form-control" name="text" id="answer" type="text" required="">
answer = browser.find_element_by_id("answer")
answer.send_keys( calc(x) )

# <button id="solve" type="submit" class="btn btn-primary" disabled="disabled">Submit</button>
button2 = browser.find_element_by_id("solve")
button2.click()

# ответ 28.96476151660789
# 
