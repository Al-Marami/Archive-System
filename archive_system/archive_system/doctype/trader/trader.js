// Copyright (c) 2024, Shujaa_Aldeen_almarami and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Trader", {
// 	refresh(frm) {
// frappe.provide("erpnext.stock");
// erpnext.buying.setup_buying_controller();
// 	},
// });
frappe.ui.form.on('Trader', {
    refresh: function(frm) {
        // Fetch the current logged-in user's username
        var first_name = frappe.session.user;

        // Set the value in your desired field (replace 'your_fieldname' with the actual field name)
        frm.set_value('data_entary', first_name);
    },
    // onload: function(report){

    // }
});

frappe.ui.form.on("Trader", 'set_posting_date_and_time_read_only', function(frm) {
    if(frm.doc.docstatus == 0 && frm.doc.set_posting_time) {
        frm.set_df_property('posting_date', 'read_only', 0);
        frm.set_df_property('posting_time', 'read_only', 0);
    } else {
        frm.set_df_property('posting_date', 'read_only', 1);
        frm.set_df_property('posting_time', 'read_only', 1);
    }
})



frappe.ui.form.on("Trader", 'refresh', function(frm) {
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


frappe.ui.form.on("Trader", "refresh", function(frm) {
    frm.fields_dict['items'].grid.get_field('item_name').get_query = function(doc, cdt, cdn) {
        // var child = locals[cdt][cdn];
        //console.log(child);
        return {    
            filters:[
                ['trader_name', '=', doc.trader_name],
            ]
        }
    }
});

