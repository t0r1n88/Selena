from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time

# Импорт для клика по координатам
from helium import *

# Создаем вебдрайвер хрома
driver = webdriver.Chrome()
# Устанавливаем неявное ожидание
driver.implicitly_wait(10)
# Открываем страницу логина факультетуса
driver.get('https://www.facultetus.ru/loginpage')
driver.maximize_window()
#  данные для входа
email = 't0r1n88@mail.ru'
password = '1qaZ2wsX'

# Ищем поле ввода емайл
email_input = driver.find_element_by_id('emailinput')
email_input.send_keys(email)

password_input = driver.find_element_by_id('passwordinput')
password_input.send_keys(password)

tmp_lst= driver.find_elements_by_class_name('whitebtnloginhalfgreen')
location = tmp_lst[0].location
print(location)
# driver.execute_script('windwow.scrollTo(0,218);'%location)
# Клик по координатам
# actions = ActionChains(driver)
# actions.move_to_element(tmp_lst[0]).move_by_offset(879,318).click().perform()
# print('Glory For Lindy Booth!!!')

# Еще попытка
set_driver(driver)
click(Point(879,318))

# tmp_lst[0].click()
#{'x': 879, 'y': 318}
# (972, 339)
# log_button = driver.find_element_by_class_name('whitebtnloginhalfgreen')
# log_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'whitebtnloginhalfgreen')))
# log_button.location_once_scrolled_into_view
# log_button.click()
# driver.close()
