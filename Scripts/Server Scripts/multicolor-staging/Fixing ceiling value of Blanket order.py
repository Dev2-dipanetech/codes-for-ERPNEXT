for d in (doc.get("items")):
    ord_id = d.blanket_order
    ch_items = (frappe.get_doc('Blanket Order',ord_id).items)
    for item in ch_items:
        if d.item_code == item.item_code:
            if (d.qty + item.ordered_qty) > item.qty:
                frappe.throw(f"Order exceeds the blanket order qty")
        
        # frappe.throw("pass")
