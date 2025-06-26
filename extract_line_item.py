
import os
import json
def extract_line_items_from_pages(data):
    final_list = []  
    for i in range(len(data)):
        final_data = data[i]
        fields = final_data.get("fields", {})
        product_details = fields.get("products")
        products_ = fields.get("productDetails")
        items = fields.get("items",[])
        consinge = fields.get("consigneeDetail")
        print(len(items),"#######%%%%%%%%%%%%%%%")
        if items:
            if len(items) < 30:
                final_list.extend(items)
        if products_:
            final_list.extend(products_)

        if consinge:
            final_list.extend(consinge)
        # Extend only valid product details
        if product_details:
            final_list.extend(product_details)
    # print(final_list, '###################')
    outPutFile = os.path.join(os.path.dirname(__file__), "result1.json")
    with open(outPutFile,'w+') as fl:
        json.dump(final_list, fl, indent=4) 
    return final_list ,len(final_list)
