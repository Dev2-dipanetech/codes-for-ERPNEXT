if doc.blanket_order:
    for d in doc.get("items"):
        value = (d.qty)*(d.rate)
        ch_items = (frappe.get_doc('Blanket Order',doc.blanket_order).items)
        for item in ch_items:
            if d.item_code == item.item_code:
                if item.ordered_value is not None:
                    
                    if (int(value) + int(item.ordered_value)) > int(item.value):
                        frappe.throw(f"{d.item_code} exceeds the value cap")
                    else:
                       
                        new_value = int(item.ordered_value) + int(value)
                        item.db_set('ordered_value', int(new_value))
                
                else:
                    item.db_set('ordered_value',int(value))
