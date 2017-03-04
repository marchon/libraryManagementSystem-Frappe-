frappe.ui.form.on("Library Transaction",

    {
        transaction_type:function (frm) {
            frm.set_query('article',function () {
                return{
                    filters:[
                        {"transaction_status ":frm.doc.transaction_type}

                    ]
                }
            })



        },
        library_member:function(frm) {
        
        console.log(frm)
        frappe.call({
            "method": "frappe.client.get",
            args: {
                doctype: "Library Member",
                name: frm.doc.library_member
            },
            callback: function (data) {
        //frm.doc.member_name = data.message.first_name + (data.message.last_name ? (" " + data.message.last_name) : "")
        //refresh_field('member_name')
        //frm.set_value('member_name', data.message.first_name + (data.message.last_name ? (" " + data.message.last_name) : ""))
                frappe.model.set_value(frm.doctype,
                    frm.docname, "member_name",
                    data.message.first_name
                    + (data.message.last_name ?
                        (" " + data.message.last_name) : ""))
            }
        })
    }

    });

