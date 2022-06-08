from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
import numpy as np
import pandas as pd

PATH = "C:/Users/br_go/Desktop/anvisa-code/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://consultas.anvisa.gov.br/#/saude/")

wait = WebDriverWait(driver, 10)
i_input = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))

i_name = i_input[1]
i_name.send_keys('selenia')
i_name.send_keys(Keys.RETURN)

time.sleep(3) #descobrir o que rolou

try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )

    s_result = table.text
    s_result = s_result.split('\n')
    s_result.pop(0)

    #pegar nome da empresa e cnpj
    for row in s_result:
        if row.find(':') > 0:
            empresa = row[(row.find(':')+2):(row.find('-')-1)]
            cnpj = row[-18:]

            print(empresa)
            print(cnpj)
        else:
            registro = [int(s) for s in row.split() if s.isdigit()]
            registro = registro[0]
            nome = row[:(row.find(str(registro)))-1]
            
            print(registro)
            print(nome)
finally:
    driver.quit()