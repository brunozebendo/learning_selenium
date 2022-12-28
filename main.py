"""a ideia do código é usar o selenium para obter informações dos próximos eventos
 de Python, depois cria um dicionário com essas informações """

"""primeiro, são feitas as importações necessárias. No curso, a Angela só importou o selenium, mas agora,
aparentemente, tem que ir importando os módulos separadamente, inclusive o By, que mudou de sintaxe
do curso para cá"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
"""esse é chrome driver que faz a ponte entre o selenium e o navegador"""
chrome_driver_path = "C:\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
"""aqui o endereço do site que se quer inspecionar"""
driver.get(
    "https://www.python.org/")
"""aqui, se usou a opção de inspecionar por CSS SELECTOR, ou seja, dentro da classe event-widget, ele vai
procurar o elemento passado pela anchor tag, depois, é criado um dicionário vazio que irá guardar os dados"""
event_times = driver.find_element(By.CSS_SELECTOR, ".event-widget TIME")
event_names = driver.find_element(By.CSS_SELECTOR, ".event-widget li a")
events = {}
"""aqui é criado um for loop para iterar pelos elementos no comprimento da variável, ou seja, a depender
da quantidade de eventos armazenados, depois esse n é passado como key, ou seja, o time será o key e o time
e o name serão os values, já .text obtem o dado em forma de texto.
 O resultado deveria ser algo assim: {0: {'time': ' 2020-08-28', 'name': Pycon JP 2020'},
"""

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()