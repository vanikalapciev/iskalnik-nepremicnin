from exporter import *
from scraper import parse_pages_napremicnine, pase_pages_bolha


#link = sys.argv[1]
link = "https://www.bolha.com/prodaja-stanovanja/osrednjeslovenska?buildingState%5Bnew-building%5D=1"

if "nepremicnine.net" in link:
	main_list=parse_pages_napremicnine(link)
elif "bolha.com" in link:
	main_list=pase_pages_bolha(link)
else:
	print ("i dont do that")
	
generate_xlsx(main_list)
