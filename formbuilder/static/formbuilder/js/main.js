$(document).ready(function(){
	$.get("get_form_templates", function(data){
		$('#magic-table').magicTable({
     		data: $.parseJSON(data),
     		columnOrderNames: [
                'name',
                'status',
                'revisionNumber',
                'uuid'
            ],
            hiddenColumns: [
                'uuid'
            ],
            searchBoxID: 'search',
            render: {
            	'name': function(row){
            		return '<a href="#">' + row.name + '</a>'
            	}
            },
            actionColumn: function(row){
            	var view = '<button type="button" class="btn pop" data-toggle="popover" title="View Template" data-content="This will show Template Form"><span class="glyphicon glyphicon-eye-open" aria-hidden="true"></span></button>';
            	var copy = '<button type="button" class="btn pop" data-toggle="popover" title="Make a copy" data-content="Click this button if you want a copy of this template"><span class="glyphicon glyphicon-transfer" aria-hidden="true"></span></button>';
            	var send = '<button type="button" class="btn pop" data-toggle="popover" title="Publish Template" data-content="This will send template"><span class="glyphicon glyphicon-send" aria-hidden="true"></span></button>';
            	var edit = '<button type="button" class="btn pop" data-toggle="popover" title="Edit Template" data-content="Press this button if you want edit this template."><span class="glyphicon glyphicon-edit" aria-hidden="true"></span></button>';
            	var del = '<button type="button" class="btn pop" data-toggle="popover" title="Remove Template" data-content="This will remove template for ever."><span class="glyphicon glyphicon-trash" aria-hidden="true"></span></button>';
            	return view +' '+ copy +' '+ edit +' '+ del +' '+ send;
            },
            actionColumnName: 'Actions',
            event: function(table){
            	table.find('.pop').popover({
            		trigger: 'hover',
            		placement: 'auto'
            	});
            }
     	});
	});
});