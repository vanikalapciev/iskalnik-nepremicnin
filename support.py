import time

def set_score (lowest_price, max_price, value):
    difference = max_price - lowest_price
    increment = difference / 5
    try:
        if  lowest_price <= float(value) < lowest_price + increment:
            score = "VERY GOOD VALUE"
        elif lowest_price + increment <= float(value) < lowest_price + increment*2:
            score = "GOOD VALUE"
        elif lowest_price + increment*2 <= float(value) < lowest_price + increment*3:
            score = "NORMAL PRICE"
        elif lowest_price + increment*3 <= float(value) < lowest_price + increment*4:
            score = "OVER PRICED"
        elif lowest_price + increment*4 <= float(value) <= lowest_price + increment*5:
            score = "VERY OVER PRICED"
    except:
        score = "NO SCORE"
    return(score)

def write_to_database(item):
    item = str(item).replace("[", "").replace("]", "").replace("}, ", "}\n")
    with open("Output.txt", "a", encoding="utf-8") as text_file:
        text_file.write(str(item) + "\n")
