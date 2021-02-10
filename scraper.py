import time
from selenium import webdriver
from statistics import mean
from selenium.webdriver.chrome.options import Options
import regex
from support import *

def parse_pages_napremicnine(url):
    PATH = "C:\chromedriver.exe"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(PATH, chrome_options=options)
    
    driver.get(url)
    print("Starting parsing for URL:")
    print(url)
    time.sleep(2)
    
    try:
        strani = driver.find_element_by_xpath("//*[@id='pagination']/ul").get_attribute("data-pages")
    except:
        strani = 1

    title_list = []
    price_list = []
    size_list = []
    link_list = []
    value_list = []
    avg_list = []
    agency_list = []  
    
    main_list =[]
    k=1
    j=1
    for i in range(int(strani)):
        time.sleep(2)
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
                
                print ("Ad " + str(j) + "...Done")
            except:
                print ("Ad " + str(j) + "...Failed")
            j +=1
        print("Page " + str(k) + "...DONE")
        k +=1
    try:
        next_page = driver.find_element_by_class_name('next')
        driver.execute_script("arguments[0].click();", next_page)
    except:
        pass
    
    driver.quit()
    
    lowest_price = min(avg_list)
    max_price = max(avg_list)
    
    for i in range(len(value_list)):
        score = set_score(lowest_price, max_price, value_list[i])

        item = {
              "Title" : title_list[i],
              "Agency" : agency_list[i],
              "Size" : size_list[i],
              "Price" : price_list[i],
              "Value" : value_list[i],
              "Avg" : str(mean(avg_list)),
              "Score" : score,
              "Link" : link_list[i],   
            }
        
        main_list.append(item)
    return main_list

def pase_pages_bolha(url):
    PATH = "C:\chromedriver.exe"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(PATH, chrome_options=options)
    
    driver.get(url)
    print("Starting parsing for URL:")
    print(url)
    time.sleep(2)
    
    title_list = []
    price_list = []
    size_list = []
    link_list = []
    value_list = []
    avg_list = []
    agency_list = []  
    
    main_list =[]
    
    running = True
    i=1
    while running:
        time.sleep(2)
        podatki = driver.find_elements_by_class_name("EntityList-item--Regular")
        j = 1
        for podatek in podatki:
            try:
                title = podatek.find_element_by_class_name("link").text
                
            except:
                title = "No TITLE"
            
            
            agency = "No AGENCY data"
            
            try:
                velikost = podatek.find_element_by_class_name("entity-description-main")
                size = regex.search(r'(\d+[0-9])(\.[0-9]{2})?(\.[0-9]{1})?', velikost.text)[0]
            except:
                size = "No SIZE data"
           
            try:
                cena = podatek.find_element_by_class_name("price-item")
                price = regex.search(r'([0-9]{1,3}\.?)+', cena.text)[0].replace(".","")
                
            except:
                price = "No PRICE data"
            
            try:
                value = str(round(float(price)/float(size), 2))
                avg_list.append(float(value))
            except:
                value = "Cannot generate VALUE"
            
            try:
                link = podatek.find_element_by_tag_name("a").get_attribute("href")
            except:
                link = "No LINK data"
           
            title_list.append(title)
            agency_list.append(agency)
            price_list.append(price)
            value_list.append(value)
            size_list.append(size)
            link_list.append(str(link))
            
           
            print("Ad " + str(j) + ' ...DONE')
            j += 1
            
        print ("Page " + str(i) + "...DONE")
        
        try:
            next_page = driver.find_element_by_class_name('Pagination-item--next')
            #driver.execute_script("arguments[0].click();", next_page)
            next_page.click()
            print("NEXT PAGE!")
        except:
            running = False
            
    driver.quit()
    
    lowest_price = min(avg_list)
    max_price = max(avg_list)
   
    
    for i in range(len(value_list)):
        score = set_score(lowest_price, max_price, value_list[i])
        
        item = {
              "Title" : title_list[i],
              "Agency" : agency_list[i],
              "Size" : size_list[i],
              "Price" : price_list[i],
              "Value" : value_list[i],
              "Avg" : str(mean(avg_list)),
              "Score" : score,
              "Link" : link_list[i],
              "Timestamp": time.time(),
              "Search": url
            }
        
        main_list.append(item)
    write_to_database(main_list)
    return main_list
