// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt
frappe.provide('shaokat')


frappe.ui.form.on('Library Member', {
	onload: function(frm) {
		console.log(frm)

		setTimeout(function () {
		 	new shaokat.demohtml(frm)
		 	new shaokat.demohtml1(frm)
		}, 100)
	}

		
});

shaokat.demohtml = Class.extend({
	init:function (frm) {
		this.frm = frm;
		this.$wrapper = this.frm.fields_dict.htmlfielddemo.$wrapper;
		this.make()
	},

	make:function () {
		var me = this;
		this.$btn = $('<button>').html('Push me').addClass('btn btn-success').on('click', function (e) {
			me.call_button_action(e)
		}).appendTo(this.$wrapper) 
	},
	call_button_action:function (e) {
		msgprint(__("Clecked Push Me Button"))
	}

});

shaokat.demohtml1 = Class.extend({
	init:function (frm) {
		this.frm = frm;
		this.$wrapper = this.frm.fields_dict.htmlfielddemo.$wrapper;
		this.make()
	},

	make:function () {
		var me = this;
		this.$btn = $('<button>').html('Push me1').addClass('btn btn-success').on('click', function (e) {
			me.call_button_action(e)
		}).appendTo(this.$wrapper) 
	},
	call_button_action:function (e) {
		msgprint(__("Clecked Push Me Button"))
	}

})

