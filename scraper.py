import time
from selenium import webdriver
from statistics import mean
from selenium.webdriver.chrome.options import Options

def parse_pages(url):
    PATH = "C:\chromedriver.exe"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(PATH, chrome_options=options)
    
    driver.get(url)
    
    time.sleep(2)
    
    try:
        strani = driver.find_element_by_xpath("//*[@id='pagination']/ul").get_attribute("data-pages")
    except:
        strani = 1
        
    print(int(strani))

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
    difference = max_price - lowest_price
    increment = difference / 5
    
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
    
        item = {
              "Title" : title_list[i],
              "Agency" : agency_list[i],
              "Size" : size_list[i],
              "Price" : price_list[i],
              "Value" : value_list[i] + " €/m2",
              "Avg" : str(mean(avg_list)),
              "Score" : score,
              "Link" : link_list[i],   
            }

        main_list.append(item)
    
    
    return main_list