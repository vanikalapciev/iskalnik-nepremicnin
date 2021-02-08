import xlsxwriter

def generate_xlsx(main_list):
    workbook = xlsxwriter.Workbook('export.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Title') 
    worksheet.write('B1', 'Agency') 
    worksheet.write('C1', 'Size') 
    worksheet.write('D1', 'Price')
    worksheet.write('E1', 'Value') 
    worksheet.write('F1', 'Score')
    worksheet.write('G1', 'Link')
    for i in range(len(main_list)):
        worksheet.write('A' + str(i+2), main_list[i]["Title"]) 
        worksheet.write('B' + str(i+2), main_list[i]["Agency"]) 
        worksheet.write('C' + str(i+2), main_list[i]["Size"]) 
        worksheet.write('D' + str(i+2), main_list[i]["Price"])
        worksheet.write('E' + str(i+2), main_list[i]["Value"] + " €/m2") 
        worksheet.write('F' + str(i+2), main_list[i]["Score"])
        worksheet.write('G' + str(i+2), main_list[i]["Link"])
    workbook.close()