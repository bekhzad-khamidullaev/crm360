$( document ).ready(function() {
  $("body").on("click", "#checkbox-all-search", function(){
    $('input:checkbox').not(this).prop('checked', this.checked);
  });
});
