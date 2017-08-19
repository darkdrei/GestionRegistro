$(document).on('ready', function(){
  $('#mensaje_empleado').modal();
  $('.addlabormodal').on('click', function(event){
    document.getElementById('form_labor').reset();
    $.ajax({
      url:'/motorizado/list/motorizado/',
      type:'get',
      dataType:'json',
      success:function(data){
         var res = data['object_list'];
          console.log(data,"   ",res);
          if (res.length == 0){
            $('#mensaje_empleado').modal('open');
          }else{
            $('#addlabor').modal('open');
          }
      }
    });
  })

});
