from openpyxl import Workbook

def createExcel(length, vendorName, finalList):
    Wb = Workbook()
    Ws = Wb.active
    
    # Setting up header
    Ws["A1"] = "VendorName"
    Ws["B1"] = "ProductName"
    Ws["C1"] = "Quantity"
    Ws["D1"] = "UnitPrice"
    Ws["E1"] = "DeliveryDate"

    # Populating data
    print(finalList)
    for i in range(length):
        row = i + 2  # Data starts from row 2
        Ws[f"A{row}"] = vendorName
        Ws[f"B{row}"] = finalList[i].get("productName", "")
        Ws[f"C{row}"] = finalList[i].get("orderedQuantity") or finalList[i].get("quantity", "")
        Ws[f"D{row}"] = finalList[i].get("price") or finalList[i].get("unitPrice") or finalList[i].get("rate") or finalList[i].get("pricePerUnit")
        Ws[f"E{row}"] = "15.03.2025"  # Fixed delivery date

    # Save workbook
    Wb.save("Output12.xlsx")