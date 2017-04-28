$(document).on('ready', function(){
  $('.addlabormodal').on('click', function(event){
    document.getElementById('form_labor').reset();
    $('#addlabor').modal('open');
  })

});
