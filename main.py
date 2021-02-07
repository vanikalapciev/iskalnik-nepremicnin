from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from statistics import mean
import xlsxwriter

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

link = sys.argv[1]
driver.get(link)

time.sleep(5)

try:
	strani = driver.find_element_by_xpath("//*[@id='pagination']/ul").get_attribute("data-pages")
except:
	strani = 2
	
print(int(strani))

title_list = []
price_list = []
size_list = []
link_list = []
value_list = []
avg_list = []
agency_list = []



for i in range(int(strani) - 1):
	time.sleep(5)
	podatki = driver.find_elements_by_class_name("oglas_container")
	for podatek in podatki:
		title = podatek.find_element_by_class_name("title")
		agency = podatek.find_element_by_class_name("agencija")
		velikost = podatek.find_element_by_class_name("velikost")
		cena = podatek.find_element_by_class_name("cena")
		link = podatek.find_element_by_tag_name("a").get_attribute("href")
		
		title_list.append(title.text)
		agency_list.append(agency.text)
		price_list.append(cena.text)
		size_list.append(velikost.text)
		link_list.append(str(link))

		try:
			price = float(cena.text.replace(" €","").replace(".","").replace(",","."))
			space = float(velikost.text.replace(" m2","").replace(",","."))
			value = round(price/space,2)
			value_list.append(str(value))
			avg_list.append(value)
		except:
			pass
	try:
		next_page = driver.find_element_by_class_name('next')
		driver.execute_script("arguments[0].click();", next_page)
	except:
		pass


print(avg_list)
lowest_price = min(avg_list)
max_price = max(avg_list)
difference = max_price - lowest_price
increment = difference / 5

workbook = xlsxwriter.Workbook('export.xlsx')
worksheet = workbook.add_worksheet() 

worksheet.write('A1', 'Title') 
worksheet.write('B1', 'Agency') 
worksheet.write('C1', 'Size') 
worksheet.write('D1', 'Price')
worksheet.write('E1', 'Value') 
worksheet.write('F1', 'Price')
worksheet.write('G1', 'Score')
worksheet.write('H1', 'Link')

for i in range(len(value_list)):

	if  lowest_price <= avg_list[i] < lowest_price + increment:
		score = "VERY GOOD VALUE"
	elif lowest_price + increment <= avg_list[i] < lowest_price + increment*2:
		score = "GOOD VALUE"
	elif lowest_price + increment*2 <= avg_list[i] < lowest_price + increment*3:
		score = "NORMAL PRICE"
	elif lowest_price + increment*3 <= avg_list[i] < lowest_price + increment*4:
		score = "OVER PRICED"
	elif lowest_price + increment*4 <= avg_list[i] <= lowest_price + increment*5:
		score = "VERY OVER PRICED"

	worksheet.write('A' + str(i+2), title_list[i]) 
	worksheet.write('B' + str(i+2), agency_list[i]) 
	worksheet.write('C' + str(i+2), size_list[i]) 
	worksheet.write('D' + str(i+2), price_list[i])
	worksheet.write('E' + str(i+2), value_list[i] + " €/m2") 
	worksheet.write('F' + str(i+2), price_list[i])
	worksheet.write('G' + str(i+2), score)
	worksheet.write('H' + str(i+2), link_list[i])

	print("Title: " + title_list[i])
	print("Agency: " + agency_list[i])
	print("Size: " + size_list[i])
	print("Price: " + price_list[i])
	print("Link: " + link_list[i])
	print("Value: " + value_list[i] + " €/m2")
	print("Avg: " + str(mean(avg_list)))
	print("Score: " + score)
	print("----------")

workbook.close() 
driver.quit()
