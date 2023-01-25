pbs = frappe.db.get_all('Project Based Stock', fields = ['item','warehouse','project','name','stock', 'company'])
flag = 0
if len(pbs) is 0:
    docu = frappe.new_doc('Project Based Stock')
    docu.project = doc.project
    docu.item = doc.item_code
    docu.company = doc.company
    docu.uom = doc.stock_uom
    docu.stock = doc.actual_qty
    docu.last_updated = doc.posting_date
    docu.warehouse = doc.warehouse
    
    docu.save()
    flag = 1
    
else:
    for p in pbs:
        if (p.item == doc.item_code) and (p.project == doc.project) and (p.warehouse == doc.warehouse): # IF THERE IS ANY DATA PRESENT WITH SAME ITEM, PROJECT AND WAREHOUSE
            docum = frappe.get_doc('Project Based Stock', p.name)
            docum.stock = str(int(p.stock) + int(doc.actual_qty))
            docum.last_updated = doc.posting_date
            docum.save()
            flag = 1
            break

if flag == 0:
    
    docu = frappe.new_doc('Project Based Stock')
    docu.project = doc.project
    docu.item = doc.item_code
    docu.company = doc.company
    docu.uom = doc.stock_uom
    docu.stock = doc.actual_qty
    docu.last_updated = doc.posting_date
    docu.warehouse = doc.warehouse
    
    docu.save()
