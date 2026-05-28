from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:

    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    
    #time.sleep(1)
    
    x = browser.find_element(By.ID, "input_value").text  
    
    print(x)
    
    y = math.log(abs(12*math.sin(int(x))))
    #y = 7
    
    print(y)
    
    
    #button.click()
    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    
    #select.select_by_value(str(y)) # ищем элемент
    
    #time.sleep(1)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    #time.sleep(1)
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    
    #time.sleep(1)
    
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    

#except Exception as e:
    #print(f"Тест упал с ошибкой: {type(e).__name__}")

finally:

    time.sleep(10)
    browser.quit()
    
