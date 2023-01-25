for d in doc.get("pay_details"):
    ch_bk_id = d.chq_id
    ch_bk = (frappe.get_doc("Cheque Book", ch_bk_id).cheque)
    for ch in ch_bk:
        if ch.cheque_no == d.cheque_no:
            ch.date = doc.posting_date
            ch.payee = d.party_name
            # frappe.throw(f"check {ch.cheque_no}")
            ch.payee_account_no = d.party_account_no
            ch.payee_amount = d.amount_paid
            ch.used = 1
            ch.save()
   
