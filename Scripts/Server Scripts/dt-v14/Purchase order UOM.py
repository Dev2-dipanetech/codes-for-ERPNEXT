for count,d in enumerate(doc.get("items")):
    ch_item = (frappe.get_doc("Item", d.item_code).uoms)
    flag = 1
    for item in ch_item:
        uom_conv_id = (str(item)).strip("UOMConversionDetail").strip('(' + ')')
        if (str(d.uom)) == (frappe.db.get_value("UOM Conversion Detail", uom_conv_id, 'uom')):
            flag = 0
            break
    if flag == 1:
        frappe.throw(f"Please Select valid UOM for {d.item_code} in row: {(count+1)}")
    # test = ch_item[0]
    
    
    


# frappe.throw(str(test))
