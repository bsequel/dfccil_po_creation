def extract_invoice_details(data):
    field = data.get("fields"," ")
    try:
        contact_data = field["contractDetails"]
        seller_details = field.get("sellerDetails"," ")
        contract_number = contact_data.get("contractNo") or contact_data.get("contractNumber"," ")
        date = contact_data.get("generatedDate"," ")
        vendor_name = seller_details.get("companyName"," ")
    except:
        seller_details = field.get("sellerDetails"," ")
        vendor_name = seller_details.get("companyName"," ")
        date = field.get("generatedDate"," ")
        contract_number = field.get("contractNumber"," ")
    return vendor_name , contract_number