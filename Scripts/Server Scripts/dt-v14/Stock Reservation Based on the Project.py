
##################### SCRIPT RUNNING BEFORE SAVE ---NEED TO CHANGE IT TO BEFORE SUBMIT DOCTYPE EVENT #####################



if doc.stock_entry_type == 'Material Receipt':
    # frappe.throw("check")
    pass

else:
    # frappe.throw("not Check")
    pbs = frappe.db.get_all('Project Based Stock', fields = ['item','warehouse','project','stock'])
    
    for d in doc.get("items"):
        warehouse = d.s_warehouse
        item_code = d.item_code
        quantity = d.qty
        project = doc.project
        
        flag = 0
        for p in pbs:
            if (warehouse == p.warehouse) and (item_code == p.item) and (project == p.project):
                flag = 1
                # frappe.throw(d.s_warehouse)
                if (int(quantity)) > (int(p.stock)):
                    frappe.throw(f"Quantity exceeds for the amount present in the {warehouse} for item : {item_code} for project : {project}")
                break
            if flag == 0:
                frappe.throw(f"Item : {item_code} not present in the selected warehouse for {project} project")
