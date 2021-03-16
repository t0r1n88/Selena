from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time

# Создаем вебдрайвер хрома
browser = webdriver.Chrome()
# Устанавливаем неявное ожидание
browser.implicitly_wait(10)
# Открываем страницу логина факультетуса
browser.get('https://online.copp03.ru/')
browser.maximize_window()
#  данные для входа
email = 't0r1n88@mail.ru'
password = '}6VhVfw3iC'

# находим поле ввода логина
login_inp = browser.find_element_by_name('USER_LOGIN')
login_inp.send_keys(email)
# находим поле ввода пароля
password_inp = browser.find_element_by_name('USER_PASSWORD')
password_inp.send_keys(password)
password_inp.submit()
# Находим ссылку на управление записью на обучение по тексту элемента
browser.find_element_by_partial_link_text('Управление записью').click()





