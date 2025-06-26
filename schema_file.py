schema = {
    "fields": {
        "category": {
            "description": "This is the category for the document, check for common bill categories such as cab fare receipts, restaurant bills, institute, education or tuition fees, flight tickets, train bill, taxi bill, Cab bill, allowance bill and similar invoices. The categary helps categorize the purpose of the invoice or bill, providing context about the nature of the service or purchase. This field is essential for distinguishing between various expense types and ensuring accurate record-keeping. Or this can be the document type for the document. If document is a visa then their category should be 'Travel'. If document is a mobile bill or internet bill then their category should be 'Telephone'.",
            "enum": ["Fuel", "Meals", "Flight", "Rental", "Taxi", "Cab", "Office Supplies", "Telephone", "Travel", "Accommodation", "Parking", "Toll", "Subscription", "Education Fee", "Train", "Letter", "Email", "Tax", "Ticket"],
            "mandatory": True
        },
        "invoiceType": {
            "description": "Classification of the invoice based on transaction type as mentioned on the invoice.",
            "enum": ["performa", "tax", "sales", "return", "export", "credit", "debit"]
        },
        "invoiceNo": {
            "description": "The invoice number is a unique numeric or alphanumeric code explicitly labeled as 'Invoice Number', 'Doc. No.', or similar. For bills, receipts, cab fares, or other documents where an invoice number is not mentioned, use the 'Order ID', 'Order No.', 'Bill No', 'Receipt No', 'Schedule Number', 'Trip Booking Id' or equivalent identifier if available. In train tickets, PNR number should not be confused as Invoice Number, as in most cases Invoice Number will be given in GST details at bottom section of the PDF. Ensure the value is clearly distinguishable from other fields like acknowledgment no., party doc. no, eway bill no., certificate no., or dates. If no relevant identifier is present, the field should remain null or empty, avoiding unrelated values.",
            "required": True,
            "mandatory": True
        },
        "invoiceDate": {
            "format": "DD-MM-YYYY",
            "description": "The invoice date is the date when the invoice was issued, often labeled as 'Invoice Date', 'Inv. Date', 'Date of Invoice', 'Doc. No/Date' or similar. For tickets or any type of bookings, this field should capture the generation date or the date when the ticket or booking was created, often identified as 'Booking Date,' 'Generation Date,' or an equivalent label. It must avoid other unrelated dates such as travel dates, departure dates, or acknowledgment dates. In emails, the date which is mentioned in the front of 'Sent' should get extracted. This field is distinct from acknowledgment dates, Party Doc dates, PO dates, or any unrelated dates. Ensure the extracted date strictly matches the format DD-MM-YYYY and validates correctly. If no such date is explicitly mentioned, no date should be extracted.",
            "required": True
        },
        "purchaseOrderNo": {
            "description": "The purchase order (PO) number or buyer order number referenced in the invoice, often labeled as 'P.O. No.','P O No.','Purchase Order No.','Customer PO No.', 'Buyer's Order No.' or 'Order No.'. They are completely distinct from invoice numbers, acknowledgment numbers, reference numbers, Supplier's reference number, and DC numbers, and must not be confused with these. They may appear at the top, in the main section, or within line-item details. PO numbers consist of digits, may include multiple entries separated by commas, and must exclude dates or unrelated numbers. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "array",
            "items": {
                "type": ["string", "null"],
                "pattern": "^[0-9]{6,}$"
            },
            "required": True
        },
        "purchaseOrderDate": {
            "type": "array",
            "description": "The date(s) associated with purchase orders in the invoice, formatted as DD-MM-YYYY, often labeled as 'Customer PO Date', 'Dated', 'Dated as', 'Po Date', 'DT.', 'Buyer's Order Date', etc. This field captures only PO dates and must not be confused with other dates like DC dates, reference dates, acknowledgment dates, or delivery dates. If multiple POs are mentioned, all corresponding dates should be captured. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "items": {
                "type": ["string", "null"],
                "pattern": "^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\\d{4})$"
            },
            "format": "DD-MM-YYYY",
            "required": True
        },
        "location": {
            "description": "Capture the complete location details associated with the document, which may include the full address, city, state, or region. Look for location information in the vendor's details, service point, delivery address, or transaction context. For travel-related documents like tickets or bills, include only the departure location or the location where the ticket is booked. Arrival locations should not be included in this field. For other documents, include venue details or service locations. If a specific location is not explicitly mentioned, extract the full address provided in the document. If multiple locations are present (e.g., origin and destination), include only the relevant locations as per the document type. If no location or address can be identified, return 'Not Available'.",
            "type": ["string", "null"],
            "required": True
        },
        "lutNo": {
            "description": "Letter of Undertaking number, for tax-free exports.",
            "type": "string",
            "pattern": "^[A-Z0-9]{15}$"
        },
        "buyerName": {
            "description": "Extract the name of the buyer or customer mentioned in invoices, bills, receipts, or related documents. Prioritize identifying the name of an individual (e.g., person) if mentioned, especially when prefixed with titles such as 'Mr.', 'Ms.', 'Mrs.', or similar, or even without a prefix. But if explicitly prefix is not mentioned then don't extract any random prefix. If the buyer's person name is not mentioned, extract the buyer company or organization name instead. For travel documents (e.g., tickets, hotel bills), include full names of passengers, clients, guests, or customers. If single name is present under multiple fields, extract it only once, don't repeat same name twice. If multiple names are present (e.g., group bookings or family reservations), list all names separated by commas. Avoid capturing unrelated details such as addresses, GST numbers, or additional text. If no relevant name is found, return 'Not Available'.",
            "required": True
        },
        "buyerGSTIN": {
            "description": "The 15-character alphanumeric GSTIN (Goods & Services Tax Identification Number) of the buyer, recipient, or consignee used in tax documents. It should not be confused with the vendor's GSTIN. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": ["string", "null"],
            "required": True,
            "format": "alphanumeric",
            "pattern": "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{1}[Z]{1}[A-Z0-9]{1}$",
            "max": "15",
            "min": "15"
        },
        "buyerPAN": {
            "description": "The Permanent Account Number (PAN) of the buyer (customer, client, consignee, recipient, or receiver). This ten-character identifier is issued by the Income Tax Department. If the PAN is not explicitly mentioned on the invoice, it should be derived from the buyer's GSTIN by extracting characters 3-12. The PAN follows a specific format: 5 alphabets, followed by 4 numbers, and ending with 1 alphabet. This identifier is crucial for tax purposes and must be distinguished from other business identifiers like CIN, TAN, or the vendor's PAN. Any special characters or spaces should be removed, and it should be validated against standard format rules.",
            "type": ["string", "null"],
            "pattern": "^[A-Z]{5}[0-9]{4}[A-Z]{1}$",
            "maxLength": 10,
            "minLength": 10,
            "required": True
        },
        "buyerPhone": {
            "description": "Contact phone/telephone numbers of Buyer's or client or consignee or recipient or receiver gstin or Buyer's of the products or services.If no phone number is available, this field should not be included in the response.Important: These numbers must be distinct and should not be listed in vendor Phone field",
            "type": "array",
            "items": {
                    "type": "string",
                    "pattern": "^(\\+?[1-9]{1}[0-9]{1,14})$"
                }
            },
        "buyerEmail": {
            "description": "Email address of Buyer's or client or consignee or recipient or receiver gstin or Buyer's of the products or services"
            },
        "buyerAddress": {
            "description": "Full address of the buyer, which may be labeled as 'Customer Address', 'Client Address', 'Consignee Address', 'Recipient Address', 'Receiver Address', 'Buyer's Address', 'Billing Address', 'Shipping Address', or 'Registered Address'. Common address components include 'Street', 'Avenue', 'Road', 'Building', 'Block', 'Floor', 'Suite', 'District', 'City', 'Postal Code', 'State', and 'Country'.",
            "type": "string",
            "required": True
        },
        "vendorName": {
            "description": "Extract the name of the vendor or supplier of the products or services listed in the invoice. If the vendor name is the same as the issuing entity's name, it should also be displayed. The vendor name should be the clean and accurate name of the supplier and should exclude unrelated details such as ISO certifications, identification numbers, or other supplementary text that may appear alongside or under the name. If no vendor name is present, return 'Not Available', don't extract from vendor address.",
            "required": True
        },
        "vendorGSTIN": {
            "description": "The 15-character alphanumeric GSTIN (Goods & Services Tax Identification Number) of the vendor or supplier used in tax documents. It should not be confused with the buyer's GSTIN. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": ["string", "null"],
            "required": True,
            "format": "alphanumeric",
            "pattern": "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{1}[Z]{1}[A-Z0-9]{1}$",
            "max": "15",
            "min": "15"
        },
        "vendorPAN": {
            "description": "The Permanent Account Number (PAN) of the vendor (supplier or seller). This ten-character identifier is issued by the Income Tax Department. If the PAN is not explicitly mentioned on the invoice, it should be derived from the vendor's GSTIN by extracting characters 3-12. The PAN follows a specific format: 5 alphabets, followed by 4 numbers, and ending with 1 alphabet. This identifier is crucial for tax purposes and must be distinguished from other business identifiers like CIN, TAN, or the buyer's PAN. Any special characters or spaces should be removed, and it should be validated against standard format rules.",
            "type": ["string", "null"],
            "pattern": "^[A-Z]{5}[0-9]{4}[A-Z]{1}$",
            "maxLength": 10,
            "minLength": 10,
            "required": True
        },
        "vendorPhone": {
            "description": "Contact phone/telephone numbers of the vendor, supplier, seller, or service provider of the products or services. These numbers must be distinct and should not be listed in the buyerPhone field. In some invoices, they may appear as 'Telephone & Fax', grouped together and separated by commas or slashes. Only telephone numbers should be extracted, excluding fax numbers, by identifying and excluding patterns typically associated with fax numbers or their placement in such groupings. Also, check the 'Note' section at the end of the invoice for additional phone numbers.",
            "type": "array",
            "items": {
                "type": "string",
                "pattern": "^(02662\\d{5})$"
            }
        },
        "vendorEmail": {
            "description": "Email address of Vendor's or supplier or seller or service provider of the products or services"
        },
        "vendorAddress": {
            "description": "Complete address of the supplier or vendor, typically containing keywords like 'Street', 'Avenue', 'Road', 'Building', 'Block', 'Floor', 'Suite', 'District', 'City', 'Postal Code', and 'State'. The address should help uniquely identify the vendor's location and may also include country information."
        },
        "vendorCIN": {
            "description": "21-character Corporate Identity Number (CIN) issued by the Ministry of Corporate Affairs. Extracted value must match the expected format and context. If not present, it should remain null or empty.",
            "type": "string",
            "pattern": "^[A-Z]{1}[0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}$",
            "maxLength": 21,
            "minLength": 21
        },
        "vendorTAN": {
            "description": "10-character Tax Deduction and Collection Account Number (TAN) issued by the Income Tax Department. Extracted value must match the expected format and context. If not present, it should remain null or empty.",
            "type": "string",
            "pattern": "^[A-Z]{4}[0-9]{5}[A-Z]{1}$",
            "maxLength": 10,
            "minLength": 10
        },
        "IEC": {
            "description": "The 10-digit alphanumeric Importer Exporter Code (IEC) issued by the Directorate General of Foreign Trade (DGFT) in India. It is mandatory for businesses involved in import and export. The IEC is a unique identifier used in all customs and trade-related documents, typically found under headings like 'IEC Code' or 'Importer Exporter Code' on invoices. If not present in the invoice, it should not fetch any unrelated value.",
            "type": "string",
            "pattern": "^[A-Z0-9]{10}$"
        },
        "drugLicenseNo": {
            "description": "Extract and include all Drug License number(s) of buyer as well as vendor from the document, regardless of their location or the associated key. These numbers may appear in different sections of the invoice, such as above the products table or below tax rates, and may be labeled with various keys like 'Drug Lic.', 'Drug Licence', 'Drug License', or similar variations. The extraction process must ensure that every occurrence of a valid Drug License Number is captured and added to the results, even if the format, label, or location differs. Keywords to identify these include but are not limited to: 'Drug Licence', 'Drug License', 'Drug License No.', 'Drug Licence No.', 'Drug Mfg Lic No.', 'D.L No.', 'D.L NO', 'D.L.No', 'Mfg Drug License No', 'Trading Drug License No', 'Party DL No.', or similar variations. These numbers must not be confused with other business identifiers such as buyer's PAN, vendor's PAN, or FSSAI numbers. All valid Drug License Numbers must be consolidated and shown in the results without any omission.",
            "type": "array",
            "required": True,
            "items": {
                "type": ["string", "null"],
                "pattern": "^[a-zA-Z0-9\\-/]+$"
            }
        },
        "vat%": {
            "description": "percentage VAT, if levied on goods/services,",
            "type": "number",
            "precision": "2 decimal places"
        },
        "vatAmount": {
            "description": "Amount of VAT, if levied on goods/services,",
            "type": "number",
            "precision": "2 decimal places"
        },
        "vatTin": {
            "type": "string",
            "description": "The VAT Taxpayer Identification Number (VAT TIN) assigned to the company. This is a unique alphanumeric identifier used for tax purposes and may be labeled as 'Company's VAT TIN' on the invoice. If it's not explicitly mentioned on the invoice, it should remain null or empty.",
            "pattern": "^[A-Za-z0-9]{11,15}$"
        },
        "msmeNo": {
            "description": "Unique government-issued alphanumeric registration identifier for Micro, Small, and Medium Enterprises (MSME), serving as a critical gateway to targeted economic support and official recognition. This specialized credential validates an enterprise's status and eligibility for government-sponsored developmental programs, financial incentives, and strategic business support. Recognized through multiple nomenclatures such as 'UAM Number', 'Udyam Registration Number', 'MSME Number', 'Udyam Number', or abbreviated forms like 'MSME No', 'Udyam No.', 'Udyam Reg No.' and 'MSME Cft No', the identifier is typically found on official documents, invoices, and registration certificates. It should be extracted regardless of its location on the invoice. Comprising letters, digits, and occasional special characters (slashes or dashes), the number is concisely structured within 20 characters, ensuring precise and standardized enterprise identification across regulatory frameworks. It should not be confused with 'Insurance No.'.",
            "type": "string",
            "pattern": "^[A-Za-z0-9/-]{1,20}$"
        },        
        "irnNo": {
            "description": "Invoice Reference Number (IRN) must be a precise 64-character alphanumeric hash generated by the Invoice Registration Portal (IRP). Strict validation ensures:\n- Exactly 64 characters long\n- Consists only of hexadecimal characters (0-9, a-f, A-F)\n- Must match the SHA256 hash format\n- If the extracted value contains additional information such as an Acknowledgement Number, only the first 64 characters corresponding to the IRN must be retained, and the rest ignored\n- Null is allowed only if no IRN has been generated\n- This is a mandatory field for valid invoice entries",
            "type": ["string", "null"],
            "minLength": 64,
            "maxLength": 64,
            "pattern": "^[0-9a-fA-F]{64}$",
            "required": True,
            "mandatory": True
        },
        "ackNo": {
            "description": "The 15-digit acknowledgment number for GST e-invoice or GST returns, confirming submission. It may appear near GST details or confirmation sections, labeled as 'Acknowledgment No.', 'GST Acknowledgment', or similar. Only valid 15-digit numbers should be extracted; if not explicitly mentioned, no value should be extracted.",
            "type": ["string", "null"],
            "pattern": "^[0-9]{15}$",
            "required": True,
            "maxLength": 15,
            "minLength": 15
        },
        "ackDate": {
            "type": ["string", "null"],
            "description": "Date when the acknowledgment number was generated by the GST portal. It is typically formatted as 'DD-MM-YYYY' and is usually found near the acknowledgment number or at the bottom of the document, in the confirmation or receipt section. Ensure the extracted date matches the expected format DD-MM-YYYY and validates correctly. Note: If the 'Acknowledgement Date' is not explicitly mentioned on the invoice, it should not be fetched. Additionally, ensure it is not confused with the Date of Supply, reference date, invoice date or any other unrelated dates.",
            "pattern": "^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\\d{4})$",
            "format": "DD-MM-YYYY",
            "required": True
        },
        "ewayBillNo": {
            "description": "The unique number generated for tracking the movement of goods under the GST system. This field will only be fetched if explicitly mentioned as an e-way bill in the invoice. It may appear labeled as 'e-Way Bill No.', 'E.B.No.', 'EWB No.', or similar. The value should strictly contain numeric characters but may vary in length. If not explicitly mentioned, this field should remain null or empty.",
            "type": ["string", "null"],
            "pattern": "^[0-9]+$",
            "format": "numeric"
        },
        "ewayBillDate": {
            "description": "The date when the Electronic Way Bill (EWay Bill) was generated. This is critical for tracking the validity and movement of goods. The date is usually formatted as 'DD/MM/YYYY' or 'YYYY-MM-DD', based on regional conventions. Ensure the extracted date adheres to standard date formats and matches the corresponding EWay Bill entry. Note: If the 'Eway Bill Date' is not explicitly mentioned on the invoice, it should not be fetched. Additionally, ensure it is not confused with the Date of Supply, reference date, invoice date or any other unrelated dates. If not present, it should return null or empty.",
            "pattern": "^(\\d{2}/\\d{2}/\\d{4}|\\d{4}-\\d{2}-\\d{2})$",
            "type": ["string", "null"],
            "format": "date"
        },
        "invoiceCurrency": {
            "description": "The currency for the amount charged in the invoice, represented strictly in ISO4217 format. The currency can be determined based on the symbols or formats used in the invoice. For instance, the '₹' symbol specifically represents 'INR' and must be returned as 'INR'. If no explicit currency label is mentioned but the '₹' symbol is present, the default currency should be 'INR'. Accepted currency values are strictly limited to the provided ISO4217 options. If no valid currency symbol or label can be identified, this field should be null or empty.",
            "enum": ["USD", "INR", "EUR", "GBP", "AUD", "CAD", "JPY", "SGD", "CNY", "HKD"],
            "required": True,
            "mandatory": True
        },
        "igst%": {
            "description": "The total percentage of IGST (Integrated Goods and Services Tax) applied on the invoice, located at the end of the tabular column summarizing all line items. Extracted value must match the expected context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "number",
            "enum": [0, 5, 7, 10, 12, 14, 15, 17, 18, 19, 20, 21, 23, 25, 28],
            "required": True,
            "precision": "2 decimal places"
        },
        "igstAmount": {
            "description": "The total amount of IGST (Integrated Goods and Services Tax) applied on the invoice, located at the end of the tabular column summarizing all line items. Extracted value must match the expected context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "number",
            "required": True,
            "precision": "2 decimal places"
        },
        "sgst%": {
            "description": "The total percentage of SGST (State Goods and Services Tax) applied on the invoice, located at the end of the tabular column summarizing all line items. Extracted value must match the expected context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "number",
            "enum": [0, 2.5, 3.5, 5, 6, 7.5, 9, 10, 12, 12.5, 14, 15, 17, 18, 19, 20, 21, 23, 25, 28],
            "required": True,
            "precision": "2 decimal places"
        },
        "sgstAmount": {
            "description": "The total amount of SGST (State Goods and Services Tax) applied on the invoice, located at the end of the tabular column summarizing all line items. Extracted value must match the expected context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "number",
            "required": True,
            "precision": "2 decimal places"
        },
        "cgst%": {
            "description": "The total percentage of CGST (Central Goods and Services Tax) applied on the invoice, located at the end of the tabular column summarizing all line items. Extracted value must match the expected context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "number",
            "enum": [0, 2.5, 3.5, 5, 6, 7.5, 9, 10, 12, 12.5, 14, 15, 17, 18, 19, 20, 21, 23, 25, 28],
            "required": True,
            "precision": "2 decimal places"
        },
        "cgstAmount": {
            "description": "The total amount of CGST (Central Goods and Services Tax) applied on the invoice, located at the end of the tabular column summarizing all line items. Extracted value must match the expected context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": "number",
            "required": True,
            "precision": "2 decimal places"
        },
        "taxableAmount": {
            "description": "The total taxable value on which taxes such as CGST, IGST, SGST, or other applicable taxes are calculated. This amount represents the combined taxable value for all items on the invoice after applying the relevant tax rates, which may vary from invoice to invoice. It is typically labeled as 'Taxable Value', 'Assessable Value', or 'Tax Base Amount' and is found near the tax computation section of the invoice. This value should reflect the total taxable amount in the invoice's currency and must be captured with exactly two decimal places. It should exclude any tax-inclusive totals or individual item-level taxable amounts and instead represent the consolidated taxable base value for the entire invoice.",
            "type": "number",
            "required": True,
            "precision": "2 decimal places"
        },
        "totalTax": {
            "description": "The total amount of tax charged on the entire invoice, covering all applicable taxes, including GST, VAT, or any other indirect taxes. This amount is usually indicated as 'Total Tax', 'Total GST/VAT', 'Tax Summary', or similar terms in the invoice. It includes the total tax calculated based on the taxable amount and any other applicable rates, but does not include any intermediate tax breakdowns or taxes specific to individual items on the invoice.",
            "type": "number",
            "required": True,
            "precision": "2 decimal places"
        },
        "roundingOff": {
            "description": "An adjustment made to the invoice total to round the final amount to the nearest whole number, either up or down, based on the rounding rules followed by the invoice issuer. This value should be extracted regardless of its location on the invoice, whether as part of the overall invoice summary or within the line item table. This ensures that the total invoice amount is presented in a simplified, whole-number format and includes any necessary rounding adjustments.",
            "type": "number",
            "precision": "2 decimal places"
        },
        "netPayableAmount": {
            "description": "The final total amount to be paid, clearly mentioned at the bottom or the last section of the invoice. This amount is the sum due after all adjustments, including taxes, discounts, rebates, cess, or any other deductions or additions. It should only fetch the explicitly stated total payable amount labeled as 'Invoice Amount', 'Total Payable', 'Amount Due', or similar terms, and must not be confused with interim totals or subtotals elsewhere on the invoice.",
            "required": True,
            "type": "number",
            "precision": "2 decimal places"
        },
        "transportDetails": {
            "description": "Details related to transportation of goods or services, often relevant in logistics, export/import, or delivery services.",
            "type": "object",
            "properties": {
                "transportType": {
                    "description": "This field indicates the type of transportation used for the expense documented in the invoice. It helps categorize the transportation method such as International, National, Transport, Train, Flight, Taxi, Roadlines, Bus, or other modes of transport. This categorization is crucial for accurately identifying travel-related costs and ensuring precise record-keeping. If the invoice is a tax invoice or unrelated to transportation, this field should remain empty and not fetch any random value. The transport type provides further context to the invoice, enabling more detailed financial tracking and reporting.",
                    "type": ["string", "null"],
                    "required": True
                },
                "transportClass": {
                    "description": "A mandatory field that defines the specific category, variant, or service level of the transportation mode used. This includes but is not limited to vehicle size categories, cabin classes, seating tiers, comfort levels, or any other service-specific classifications established by the transport provider. The transport class directly corresponds to the pricing tier and service features offered, serving as a key identifier for expense categorization, reimbursement processing, and travel policy compliance tracking. For verification purposes, this classification should match exactly with what appears on the official travel document or receipt.",
                    "type": ["string", "null"],
                    "required": True
                },
                "vehicleNumber": {
                    "description": "Vehicle registration number for tracking purposes, generally visible near transport or delivery details. Typically appears next to 'Motor Vehicle No.', 'Vehicle No.' or 'Vehicle number' labels on the invoice. If not present in the invoice, it should show null.",
                    "type": ["string", "null"],
                    "pattern": "^[A-Z0-9- ]+$"
                },
                "placeOfSupply": {
                    "description": "The name of the location representing the final destination for goods or services. This field must strictly be extracted from specific keywords such as 'Place of Supply', 'Destination', 'Delivery Location', or 'Destination Location' or similar explicitly labeled identifiers on the invoice. If such a location is not explicitly mentioned using these relevant identifiers, only then fetch it from the addresses provided. However, ensure that the extracted location includes only the locality, region, area, or state names, and exclude extraneous terms like 'Station', 'Warehouse', or similar. This field should not fetch the end city or any part of the address unless no other relevant identifier is available. If no valid location can be determined, this field should be null or empty.",
                    "required": True,
                    "type": ["string", "null"],
                    "pattern": "^[a-zA-Z\\s]+$"
                },
                "mode/termsOfPayment": {
                    "description": "The conditions under which payment for the transportation or goods must be made. It can be found written as 'Pay terms', 'Credit Days', 'Terms of payment', 'Mode of payment', 'Mode/terms of payment', or 'Payment terms,' often expressed as 'X days,' where 'X' stands for the number of days. Additionally, it may be mentioned in the format 'Due date for payment,' explicitly specifying the deadline for payment. It should not be confused with transport details such as mode of transport, dispatch document number, etc. It may also include additional information on delivery, along with terms and conditions related to the responsibility for damages, delays, and costs.",
                    "type": ["string", "null"],
                    "required": True
                }   
            }
        },
        "freightCharges": {
            "description": "Comprehensive details of the freight charges associated with the shipment. This includes the total monetary value of the charges and the payment status. Note: Terms related to freight, such as 'amount' or 'freight,' may sometimes appear under 'Terms of Delivery' in the document. Ensure these terms are interpreted accurately in the context of freight charges.",
            "type": "object",
            "properties": {
                "amount": {
                    "description": "The total monetary value of the freight charges incurred for the shipment. This represents the financial cost attributed to the transportation of goods and may appear under 'Terms of Delivery' in the document. The amount should be extracted as a numeric value and validated against the context of freight details.",
                    "type": "number"
                },
                "freight": {
                    "description": "Indicates the payment status of the freight charges. This specifies whether the charges have been fully 'paid,' are still 'not paid,' or are due for payment under 'to pay.' The term 'freight' may sometimes be mentioned under 'Terms of Delivery,' and care should be taken to interpret the context correctly.",
                    "type": ["string", "null"],
                    "enum": ["paid", "not paid", "to pay"]
                },
                "freightOutward%": {
                    "description": "Percentage of Freight Outward charges applicable in the invoice, usually as a part of logistics or delivery costs.",
                    "type": "number",
                    "enum": [0, 5, 12, 18],
                    "precision": "2 decimal places"
                },
                "freightOutwardAmount": {
                    "description": "Total amount of Freight Outward charges calculated based on the applicable percentage.",
                    "type": "number",
                    "precision": "2 decimal places"
                },
                "freightInward%": {
                    "description": "Percentage of Freight Inward charges applicable in the invoice, representing transportation costs incurred for incoming goods.",
                    "type": "number",
                    "enum": [0, 5, 12, 18],
                    "precision": "2 decimal places"
                },
                "freightInwardAmount": {
                    "description": "Total amount of Freight Inward charges calculated based on the applicable percentage.",
                    "type": "number",
                    "precision": "2 decimal places"
                }
            }
        }, 
        "bankDetails": {
            "description": "Comprehensive banking information required for payment processing of global invoices.",
            "type": "object",
            "required": True,
            "properties": {
                "bankName": {
                    "description": "The full, official name of the bank where the account is held. This is usually located close to account or banking details on documents and often includes terms like 'Bank' or 'Bank of'. It should not be confused with branch names, which are location-specific. If not present in the invoice, it should not extract any other data, it should show null.",
                    "type": ["string", "null"]
                },
                "bankBranch": {
                    "description": "The specific branch name or location of the bank linked to the account. Typically found near the bank name or bank address on documents. Branch names may include locality, area, city, or unique identifiers for easy identification. If not present in the invoice, it should not extract any other data, it should show null.",
                    "type": ["string", "null"]
                },
                "ifscNo": {
                    "description": "An IFSC code is a unique 11-character identifier used specifically for Indian banks in domestic transfers. It starts with 4 uppercase letters (bank code), followed by a '0' (zero), and ends with 6 alphanumeric characters. It is distinct from a SWIFT/BIC code, which is used for international transactions. It can sometimes be found mis-spelled as ISFC. If a valid IFSC code is not explicitly present in the invoice, this field should be null or empty. Ensure that no SWIFT code is mistakenly extracted as an IFSC code.",
                    "type": ["string", "null"],
                    "pattern": "^[A-Z]{4}0[A-Z0-9]{6}$"
                },
                "accountNo": {
                    "description": "The complete bank account number associated with this account, or IBAN for international accounts. Typically appears next to 'Account No', 'Current A/C NO', 'Acct', or 'A/C' or 'Acc.No' labels on invoices or account documents. Avoids formats specific to SWIFT or IFSC. If not present in the invoice, it should show null.",
                    "type": ["string", "null"]
                }
            }
        },
        "invoiceItems": {
        "description": "Extract all itemized entries from the invoice compulsorily, ensuring no line item is missed. This includes capturing every single line item present, regardless of page breaks or table continuations. Each row must represent one distinct item entry with its associated details, and the extraction process should handle multi-page tables seamlessly.",
        "mandatory": True,
        "required": True,
        "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "serialNumber": {
                        "description": "Unique sequential or alphanumeric identifier explicitly marking each line item within an invoice. This field captures the precise line item tracking code, distinguishable from other numeric labels like package numbers, batch codes, or descriptive references. Commonly represented as 'Serial No.', 'Sr. No.', or 'SI No.', the item number provides a clear, systematic method for referencing specific goods or services. It should be extracted exactly as printed in the invoice's line item section, maintaining its original format (sequential: 1, 2, 3 or alphanumeric: A001, B002). The identifier serves as a critical navigation point for precise product or service identification, ensuring accurate invoice interpretation and line-item tracking.",
                        "type": ["string", "null"],
                        "required": True
                    },
                    "description": {
                        "description": "The full, detailed description of the product or service listed in the invoice, capturing all text that spans across multiple lines, columns, or rows. It can be found labelled as 'Description of Goods', 'Description', 'Description of Items', etc. This field should extract information even when it appears as wrapped text or split into subpoints, bullet points, or indented lines. The description must include any additional notes, technical specifications, quantities, materials, dimensions, and any other relevant details provided. Ensure that line breaks, special formatting, or column divisions in the document do not result in lost or truncated information. The extracted description should maintain the natural sequence and order of the text, preserving readability and coherence. Additionally, handle cases where the text includes a combination of bold, underlined, or handwritten annotations adjacent to the printed description.",
                        "type": "string",
                        "maxLength": 4000,
                        "multiline": True,
                        "required": True,
                        "mandatory": True
                    },
                    "matNumberOfItem": {
                        "description": "The material number or code associated with this specific line item. This field should only be extracted when mentioned in the description of the specific item. If not mentioned, this field should be returned empty.",
                        "type": ["string", "null"]
                    },
                    "hsnSac": {
                        "description": "The HSN (Harmonized System of Nomenclature) or SAC (Service Accounting Code) for the product or service. HSN codes (8 digits) classify goods, while SAC codes (6 digits) classify services for GST purposes. These codes may be labeled as 'HSN/SAC', 'hsnsac', 'hsn/sac', 'HSN Code (GST)', etc. If not found in a separate column, they might appear alongside the item or product name in the description.",
                        "type": ["string", "null"],
                        "required": True
                    },
                    "challanNumber": {
                        "description": "A unique serial number assigned to the tax payment challan. This number is typically found on tax payment documents and serves as an identifier for the specific payment or transaction. The challan serial number is usually numeric, with a maximum length of 5 digits. It is crucial for tax payment tracking and verification. This field should be extracted from the tax payment challan where it is clearly labeled and associated with the payment. The serial number must be a valid numeric value not exceeding 5 digits in length.",
                        "type": ["string", "null"],
                        "pattern": "^[0-9]{1,5}$"
                    },
                    "partyCode": {
                        "description": "A unique alphanumeric or numeric code assigned to identify a party (such as a customer, supplier, or business entity) in business transactions. This code helps in maintaining records, tracking transactions, and ensuring accurate communication with specific entities.",
                        "type": "string"
                    },
                    "partNo": {
                        "description": "A Part Number (Part No.) is a unique identifier assigned to a specific component, product, or item within an inventory system, manufacturing process, or catalog. It is commonly used in industries such as manufacturing, engineering, retail, and logistics to ensure accurate identification and management of items. It is a numeric code which is found labelled as 'Part No.', 'part no.', etc.",
                        "type": "string",
                        "pattern": "^\\d{1,10}$"
                    },
                    "sapCode": {
                        "type": "string",
                        "description": "SAP code for the item/product. Returns null if not found."
                    },
                    "drgNo": {
                        "type": "string",
                        "description": "Drug/product number (DRG). Returns null if not found."
                    },
                    "uom": {
                        "description": "The unit of measure for the product or service. It indicates the measurement standard used for the quantity of the item. Common examples include KG for weight, L for volume, and PCS for quantity. It is often labelled as 'per', 'UOM', 'uom', etc. Note: 'boxes' should not be extracted as a unit of measure.",
                        "type": ["string", "null"],
                        "enum": ["KG", "kg", "GM", "gm", "no", "nos", "NOS", "EA", "LB", "T", "L", "ML", "GAL", "PCS", "UNT", "DZ", "M", "CM", "IN", "FT", "HR", "D", "WK", "Sessions", "Visits", "Subscriptions"]
                    },
                    "rate": {
                        "description": "The rate per unit of the product or service is a monetary amount, typically found in the tabular section of the invoice. It can be labeled as 'Unit Price', 'Per Unit Price', or similar terms. This is distinct from the 'quantity' column and reflects the price per item or service unit, not the total amount or quantity.",
                        "type": "number",
                        "precision": "2 decimal places"
                    },
                    "quantity": {
                        "description": "The numeric quantity of the item or service being described. This field should capture only the numerical value, excluding units of measurement such as 'Boxes', 'KG', 'MIL', etc. The extracted quantity must be a positive number and should be distinct from the 'rate' field, which represents the price per unit. It is also distinct from 'No. of pkg' field which can be mentioned in separate column or together in the same column with quantity, separated by a '/' or a ','. Along with that, it is also distinct from 'No. of roll' or ''.No. of rolls' field. Ensure that the quantity value is accurately extracted and does not include any additional descriptors or units.",
                        "type": ["string", "null"],
                        "pattern": "^\\d+(\\.\\d+)?$"
                    },
                    "totalAmount": {
                        "description": "The total amount for this product or service (quantity * rate + tax). Check near description of product or service for Total Amount of product or service.",
                        "type": "number",
                        "required": True,
                        "precision": "2 decimal places"
                    }
                }
            }
        }
    }
}

schema1 = {
    "fields": {
        "invoiceNo": {
            "description": "The invoice number is a unique numeric or alphanumeric code explicitly labeled as 'Invoice Number', 'Doc. No.', or similar. For bills, receipts, cab fares, or other documents where an invoice number is not mentioned, use the 'Order ID', 'Order No.', 'Bill No', 'Receipt No', 'Schedule Number', 'Trip Booking Id' or equivalent identifier if available. In train tickets, PNR number should not be confused as Invoice Number, as in most cases Invoice Number will be given in GST details at bottom section of the PDF. Ensure the value is clearly distinguishable from other fields like acknowledgment no., party doc. no, eway bill no., certificate no., or dates. If no relevant identifier is present, the field should remain null or empty, avoiding unrelated values.",
            "required": True,
            "mandatory": True
        },
        "invoiceDate": {
            "format": "DD-MM-YYYY",
            "description": "The invoice date is the date when the invoice was issued, often labeled as 'Invoice Date', 'Inv. Date', 'Date of Invoice', 'Doc. No/Date' or similar. For tickets or any type of bookings, this field should capture the generation date or the date when the ticket or booking was created, often identified as 'Booking Date,' 'Generation Date,' or an equivalent label. It must avoid other unrelated dates such as travel dates, departure dates, or acknowledgment dates. In emails, the date which is mentioned in the front of 'Sent' should get extracted. This field is distinct from acknowledgment dates, Party Doc dates, PO dates, or any unrelated dates. Ensure the extracted date strictly matches the format DD-MM-YYYY and validates correctly. If no such date is explicitly mentioned, no date should be extracted.",
            "required": True
        },
        "purchaseOrderNo": {
            "description": "The purchase order (PO) number or buyer order number referenced in the invoice, often labeled as 'P.O. No.','P O No.','Purchase Order No.','Customer PO No.', 'Buyer's Order No.' or 'Order No.'. They are completely distinct from invoice numbers, acknowledgment numbers, reference numbers, Supplier's reference number, and DC numbers, and must not be confused with these. They may appear at the top, in the main section, or within line-item details. PO numbers consist of digits, and must exclude dates or unrelated numbers. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "items": {
                "type": ["string", "null"],
                "pattern": "^[0-9]{6,}$"
            },
            "required": True
        },
        "purchaseOrderDate": {
            # "type": "array",
            "description": "The date(s) associated with purchase orders in the invoice, formatted as DD-MM-YYYY, often labeled as 'Customer PO Date', 'Dated', 'Dated as', 'Po Date', 'DT.', 'Buyer's Order Date', etc. This field captures only PO dates and must not be confused with other dates like DC dates, reference dates, acknowledgment dates, or delivery dates. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "items": {
                "type": ["string", "null"],
                "pattern": "^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\\d{4})$"
            },
            "format": "DD-MM-YYYY",
            "required": True
        },
        
        "vendorName": {
            "description": "Extract the name of the vendor or supplier of the products or services listed in the invoice. If the vendor name is the same as the issuing entity's name, it should also be displayed. The vendor name should be the clean and accurate name of the supplier and should exclude unrelated details such as ISO certifications, identification numbers, or other supplementary text that may appear alongside or under the name. If no vendor name is present, return 'Not Available', don't extract from vendor address.",
            "required": True
        },
        "vendorGSTIN": {
            "description": "The 15-character alphanumeric GSTIN (Goods & Services Tax Identification Number) of the vendor or supplier used in tax documents. It should not be confused with the buyer's GSTIN. Extracted value must match the expected format and context of this field. If the field is not present in the invoice, it should remain null or empty instead of extracting an unrelated value.",
            "type": ["string", "null"],
            "required": True,
            "format": "alphanumeric",
            "pattern": "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{1}[Z]{1}[A-Z0-9]{1}$",
            "max": "15",
            "min": "15"
        },
        "vendorPAN": {
            "description": "The Permanent Account Number (PAN) of the vendor (supplier or seller). This ten-character identifier is issued by the Income Tax Department. If the PAN is not explicitly mentioned on the invoice, it should be derived from the vendor's GSTIN by extracting characters 3-12. The PAN follows a specific format: 5 alphabets, followed by 4 numbers, and ending with 1 alphabet. This identifier is crucial for tax purposes and must be distinguished from other business identifiers like CIN, TAN, or the buyer's PAN. Any special characters or spaces should be removed, and it should be validated against standard format rules.",
            "type": ["string", "null"],
            "pattern": "^[A-Z]{5}[0-9]{4}[A-Z]{1}$",
            "maxLength": 10,
            "minLength": 10,
            "required": True
        },

        "invoiceCurrency": {
            "description": "The currency for the amount charged in the invoice, represented strictly in ISO4217 format. The currency can be determined based on the symbols or formats used in the invoice. For instance, the '₹' symbol specifically represents 'INR' and must be returned as 'INR'. If no explicit currency label is mentioned but the '₹' symbol is present, the default currency should be 'INR'. Accepted currency values are strictly limited to the provided ISO4217 options. If no valid currency symbol or label can be identified, this field should be null or empty.",
            "enum": ["USD", "INR", "EUR", "GBP", "AUD", "CAD", "JPY", "SGD", "CNY", "HKD"],
            "required": True,
            "mandatory": True
        },

        "netPayableAmount": {
            "description": "The final total amount to be paid, clearly mentioned at the bottom or the last section of the invoice. This amount is the sum due after all adjustments, including taxes, discounts, rebates, cess, or any other deductions or additions. It should only fetch the explicitly stated total payable amount labeled as 'Invoice Amount', 'Total Payable', 'Amount Due', or similar terms, and must not be confused with interim totals or subtotals elsewhere on the invoice.",
            "required": True,
            "type": "number",
            "precision": "2 decimal places"
        },
        "transportDetails": {
            "description": "Details related to transportation of goods or services, often relevant in logistics, export/import, or delivery services.",
            "type": "object",
            "properties": {
                "vehicleNumber": {
                    "description": "Vehicle registration number for tracking purposes, generally visible near transport or delivery details. Typically appears next to 'Motor Vehicle No.', 'Vehicle No.' or 'Vehicle number' labels on the invoice. If not present in the invoice, it should show null.",
                    "type": ["string", "null"],
                    "pattern": "^[A-Z0-9- ]+$"
                },
            }
        },
        "freightCharges": {
            "description": "Comprehensive details of the freight charges associated with the shipment. This includes the total monetary value of the charges and the payment status. Note: Terms related to freight, such as 'amount' or 'freight,' may sometimes appear under 'Terms of Delivery' in the document. Ensure these terms are interpreted accurately in the context of freight charges.",
            "type": "object",
            "properties": {
                "amount": {
                    "description": "The total monetary value of the freight charges incurred for the shipment. This represents the financial cost attributed to the transportation of goods and may appear under 'Terms of Delivery' in the document. The amount should be extracted as a numeric value and validated against the context of freight details.",
                    "type": "number"
                },
                "freight": {
                    "description": "Indicates the payment status of the freight charges. This specifies whether the charges have been fully 'paid,' are still 'not paid,' or are due for payment under 'to pay.' The term 'freight' may sometimes be mentioned under 'Terms of Delivery,' and care should be taken to interpret the context correctly.",
                    "type": ["string", "null"],
                    "enum": ["paid", "not paid", "to pay"]
                },
                "freightOutward%": {
                    "description": "Percentage of Freight Outward charges applicable in the invoice, usually as a part of logistics or delivery costs.",
                    "type": "number",
                    "enum": [0, 5, 12, 18],
                    "precision": "2 decimal places"
                },
                "freightOutwardAmount": {
                    "description": "Total amount of Freight Outward charges calculated based on the applicable percentage.",
                    "type": "number",
                    "precision": "2 decimal places"
                },
                "freightInward%": {
                    "description": "Percentage of Freight Inward charges applicable in the invoice, representing transportation costs incurred for incoming goods.",
                    "type": "number",
                    "enum": [0, 5, 12, 18],
                    "precision": "2 decimal places"
                },
                "freightInwardAmount": {
                    "description": "Total amount of Freight Inward charges calculated based on the applicable percentage.",
                    "type": "number",
                    "precision": "2 decimal places"
                }
            }
        },
        
        "invoiceItems": {
        "description": "Extract all itemized entries from the invoice compulsorily, ensuring no line item is missed. This includes capturing every single line item present, regardless of page breaks or table continuations. Each row must represent one distinct item entry with its associated details, and the extraction process should handle multi-page tables seamlessly.",
        "mandatory": True,
        "required": True,
        "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "serialNumber": {
                        "description": "Unique sequential or alphanumeric identifier explicitly marking each line item within an invoice. This field captures the precise line item tracking code, distinguishable from other numeric labels like package numbers, batch codes, or descriptive references. Commonly represented as 'Serial No.', 'Sr. No.', or 'SI No.', the item number provides a clear, systematic method for referencing specific goods or services. It should be extracted exactly as printed in the invoice's line item section, maintaining its original format (sequential: 1, 2, 3 or alphanumeric: A001, B002). The identifier serves as a critical navigation point for precise product or service identification, ensuring accurate invoice interpretation and line-item tracking.",
                        "type": ["string", "null"],
                        "required": True
                    },
                    "description": {
                        "description": "The full, detailed description of the product or service listed in the invoice, capturing all text that spans across multiple lines, columns, or rows. It can be found labelled as 'Description of Goods', 'Description', 'Description of Items', etc. This field should extract information even when it appears as wrapped text or split into subpoints, bullet points, or indented lines. The description must include any additional notes, technical specifications, quantities, materials, dimensions, and any other relevant details provided. Ensure that line breaks, special formatting, or column divisions in the document do not result in lost or truncated information. The extracted description should maintain the natural sequence and order of the text, preserving readability and coherence. Additionally, handle cases where the text includes a combination of bold, underlined, or handwritten annotations adjacent to the printed description.",
                        "type": "string",
                        "maxLength": 4000,
                        "multiline": True,
                        "required": True,
                        "mandatory": True
                    },
                    "matNumberOfItem": {
                        "description": "The material number or code associated with this specific line item. This field should only be extracted when mentioned in the description of the specific item. If not mentioned, this field should be returned empty.",
                        "type": ["string", "null"]
                    },
                    "hsnSac": {
                        "description": "The HSN (Harmonized System of Nomenclature) or SAC (Service Accounting Code) for the product or service. HSN codes (8 digits) classify goods, while SAC codes (6 digits) classify services for GST purposes. These codes may be labeled as 'HSN/SAC', 'hsnsac', 'hsn/sac', 'HSN Code (GST)', etc. If not found in a separate column, they might appear alongside the item or product name in the description.",
                        "type": ["string", "null"],
                        "required": True
                    },
                    # "partNo": {
                    #     "description": "A Part Number (Part No.) is a unique identifier assigned to a specific component, product, or item within an inventory system, manufacturing process, or catalog. It is commonly used in industries such as manufacturing, engineering, retail, and logistics to ensure accurate identification and management of items. It is a numeric code which is found labelled as 'Part No.', 'part no.', etc.",
                    #     "type": "string",
                    #     "pattern": "^\\d{1,10}$"
                    # },
                    "rate": {
                        "description": "The rate per unit of the product or service is a monetary amount, typically found in the tabular section of the invoice. It can be labeled as 'Unit Price', 'Per Unit Price', or similar terms. This is distinct from the 'quantity' column and reflects the price per item or service unit, not the total amount or quantity.",
                        "type": "number",
                        "precision": "2 decimal places"
                    },
                    "quantity": {
                        "description": "The numeric quantity of the item or service being described. This field should capture only the numerical value, excluding units of measurement such as 'Boxes', 'KG', 'MIL', etc. The extracted quantity must be a positive number and should be distinct from the 'rate' field, which represents the price per unit. It is also distinct from 'No. of pkg' field which can be mentioned in separate column or together in the same column with quantity, separated by a '/' or a ','. Along with that, it is also distinct from 'No. of roll' or ''.No. of rolls' field. Ensure that the quantity value is accurately extracted and does not include any additional descriptors or units.",
                        "type": ["string", "null"],
                        "pattern": "^\\d+(\\.\\d+)?$"
                    },
                    "totalAmount": {
                        "description": "The total amount for this product or service (quantity * rate + tax). Check near description of product or service for Total Amount of product or service.",
                        "type": "number",
                        "required": True,
                        "precision": "2 decimal places"
                    }
                }
            }
        }
    }
}
