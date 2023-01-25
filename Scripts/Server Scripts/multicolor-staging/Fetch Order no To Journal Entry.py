for d in doc.get("accounts"):
    id_type = d.reference_type
    id_name = d.reference_name
    if (str(id_type)) == 'Sales Invoice':
        ch_item = (frappe.get_doc(id_type, id_name).items) # Sales Invoice Items Ids
        sale_in_item_id = (str(ch_item[0])).strip("SalesInvoiceItem").strip('(' + ')')
        sales_order = frappe.db.get_value("Sales Invoice Item", sale_in_item_id,'sales_order')
        d.order_number = sales_order
    if (str(id_type)) == 'Purchase Invoice':
        ch_item = (frappe.get_doc(id_type, id_name).items) # Purchase Invoice Items Ids
        pur_in_item_id = (str(ch_item[0])).strip("PurchaseInvoiceItem").strip('(' + ')')
        pur_order = frappe.db.get_value("Purchase Invoice Item", pur_in_item_id,'purchase_order')
        d.order_number = pur_order
    
    if (str(id_type)) == 'Sales Order' or (str(id_type)) == "Purchase Order":
        d.order_number = d.reference_name
