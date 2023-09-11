$('#checkbox-all-search').change(function () {
    $('#checkbox-table-search-1').prop('checked', this.checked);
});

$("#checkbox-table-search-1").change(function () {
    if ($("#checkbox-table-search-1:checked").length == $("#checkbox-table-search-1").length) {
        $('#checkAll').prop('checked', 'checked');
    } else {
        $('#checkAll').prop('checked', false);
    }
});