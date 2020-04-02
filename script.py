from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC



#NAO MEXA
driver = webdriver.Chrome('C:\\Users\\XXX\\Desktop\\chromedriver') #Localize o Chromedriver no PC


driver.get('https://www.bing.com')
try:
    pesquisa = WebDriverWait(driver, 7).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'sb_form_q'))
    )
    pesquisa.send_keys('site:chat.whatsapp.com')
    pesquisa.send_keys(Keys.ENTER)
except:
    print('Algo deu errado :(')
