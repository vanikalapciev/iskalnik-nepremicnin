from exporter import *
from scraper import parse_pages


#link = sys.argv[1]
link = "https://www.nepremicnine.net/oglasi-prodaja/juzna-primorska/stanovanje/3-sobno/cena-do-450000-eur/"
main_list=parse_pages(link)
generate_xlsx(main_list)
