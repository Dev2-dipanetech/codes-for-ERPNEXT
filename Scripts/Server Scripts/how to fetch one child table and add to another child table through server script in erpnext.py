# The following was added to a server script in "https://multicolorgroup-staging2.frappe.cloud/". The name of the script
# was "Fetch Sales Order No for Payment Entry Reference".
# The requirement was to fetch the order no. from sales invoice  or purchase invoice, which is inside the child table of
# another doctype and add that number to the current doctype, which is payment entry references which is a child doctype
# in payment entry



for d in doc.get("references"): # Here the doc.get("references") gets access to the child table on row by row basis
    id_name = d.reference_name
    id_type = d.reference_doctype
    if (str(id_type)) == 'Sales Invoice':
        # frappe.throw("check")
        ch_item = (frappe.get_doc(id_type, id_name).items)  # Sales Invoice Items Ids
        sale_in_item_id = (str(ch_item[0])).strip("SalesInvoiceItem").strip('(' + ')')
        sales_order = frappe.db.get_value("Sales Invoice Item", sale_in_item_id, 'sales_order')
        d.order_number = sales_order
    if (str(id_type)) == 'Purchase Invoice':
        ch_item = (frappe.get_doc(id_type, id_name).items)  # Purchase Invoice Items Ids
        pur_in_item_id = (str(ch_item[0])).strip("PurchaseInvoiceItem").strip('(' + ')')
        pur_order = frappe.db.get_value("Purchase Invoice Item", pur_in_item_id, 'purchase_order')
        d.order_number = pur_order

    if (str(id_type)) == 'Sales Order' or (str(id_type)) == "Purchase Order":
        d.order_number = d.reference_name