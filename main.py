import os
import bot
from time import sleep

from selenium import webdriver

contacts_list_class_name= "P6z4j"
contact_class = "_1lpto"
message_class = "FTBzM"



dir_path = os.getcwd()
chrome = dir_path+'/chromedriver'
options = webdriver.ChromeOptions()

#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36")  # Workaround for whastapp works on chromium browser
options.add_argument(r"user-data-dir="+dir_path+"/profile/wpp") # Store whatsapp credentias to skiping it on next login
browser = webdriver.Chrome(chrome, options=options)

browser.get('https://web.whatsapp.com/')
browser.implicitly_wait(20)

activated = False
while True:
	unread = browser.find_elements_by_class_name(contacts_list_class_name)
	if len(unread) > 0:
		most_recent = unread[0]
		action = webdriver.common.action_chains.ActionChains(browser)
		action.move_to_element_with_offset(most_recent, 0, -20)
		action.click()
		action.perform()
		sleep(2)
		name = browser.find_element_by_class_name(contact_class).text
		text = '\n'.join(browser.find_elements_by_class_name(message_class)[-1].text.split('\n')[:-1])
		hour = browser.find_elements_by_class_name(message_class)[-1].text.split('\n')[-1]
		log = f'{hour} {name}: {text}'
		print(log)
		# if text == "oi":
		# 	activated = True
		# 	send('Estou ativado')

		# if text == "tchau":
		# 	activated = False
		# 	send('Desativado! :(')

		# if activated:
		# 	if text in ['bebidas', ' bebidas', 'bebida', ' bebida', 'Bebidas', ' Bebidas', 'Bebida', ' Bebida']:
		# 		bot.bebidas()
		# 	elif text in ['salgados', ' salgados', 'salgado', ' salgado', 'Salgados', ' Salgados', 'Salgado', ' Salgado']:
		# 		bot.salgados()
		# 	elif text in ['cervejas', ' cervejas', 'cerveja', ' cervejas', 'Cervejas', ' Cervejas', 'Cerveja', ' Cerveja']:
		# 		bot.cervejas()
		# 	elif text in ['tiragostos', ' tiragostos', 'tiragosto', ' tiragostos', 'Tiragostos', ' Tiragostos', 'Tiragosto', ' Tiragosto']:
		# 		bot.tiragostos()
		# 	elif text in ['sincroniza', ' sincroniza', 'sincronizar', ' sincronizar', 'Sincroniza', ' Sincroniza', 'Sincronizar', ' Sincronizar']:
		# 		bot.sincronizar()
		# 	else:
		# 		bot.send('Ainda não aprendi isto  :(')
