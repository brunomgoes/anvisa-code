from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

PATH = "C:/Users/br_go/Desktop/anvisa-code/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://consultas.anvisa.gov.br/#/saude/")

wait = WebDriverWait(driver, 10)
i_input = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))

i_name = i_input[1]
i_name.send_keys('dixtal')
i_name.send_keys(Keys.RETURN)

try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )

    rows = table.find_elements(By.TAG_NAME, 'td')
    print(rows)

finally:
    time.sleep(5)
    driver.quit()