from exporter import *
from scraper import parse_pages


link = sys.argv[1]

main_list=parse_pages(link)

generate_xlsx(main_list)
