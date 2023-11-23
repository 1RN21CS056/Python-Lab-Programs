import openpyxl

try:
    wb = openpyxl.load_workbook('C:\\Users\\Eshwar K\\OneDrive\\Desktop\\example.xlsx')
    sheet = wb.active
    
    for row in sheet.iter_rows(values_only=True):
        print('\t'.join(map(str, row)))
    
    wb.close()

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
