# doc.append("cheque",{"cheque_no":"test2"})
tot = int(doc.cheque_leaf_end) - int(doc.cheque_leaf_start) + 1

doc.total_leaves = tot
 
# if doc.get("cheque"):
#     frappe.throw("Cheque Leaves already made. Please delete the cheques made below")
    
if not doc.get("cheque"):
    for i in range (tot):
        doc.append("cheque",{"cheque_no": (int(doc.cheque_leaf_start)+i)})
