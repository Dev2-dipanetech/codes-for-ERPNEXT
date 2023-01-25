frappe.ui.form.on('Purchase Invoice', {
	setup: function (frm) {
    frm.set_query("uom", "items", function (doc, cdt, cdn) {
      let row = locals[cdt][cdn];
      return {
            query:
              "erpnext.accounts.doctype.pricing_rule.pricing_rule.get_item_uoms",
                filters: {
                  value: row.item_code,
                  apply_on: "Item Code",
                },
            };
        });
    },
})
