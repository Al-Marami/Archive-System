// Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Trader Info", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Trader Info", 'set_posting_time', function(frm) {
    frm.trigger('set_posting_date_and_time_read_only');
});
frappe.ui.form.on("Trader Info", 'refresh', function(frm) {
    // set default posting date / time
    if(frm.doc.docstatus==0) {
        if(!frm.doc.posting_date) {
            frm.set_value('posting_date', frappe.datetime.nowdate());
        }
        if(!frm.doc.posting_time) {
            frm.set_value('posting_time', frappe.datetime.now_time());
        }
        frm.trigger('set_posting_date_and_time_read_only');
    }
});
