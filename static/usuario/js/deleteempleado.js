$(document).on('ready', function(){
  $('#deleteempleado').modal();
  $('.delete_save_empleado').on('click',function(event){
    return false;
  });
  $('.delete_save_empleado').on('click',function(event){
    $.ajax({
      url:$(this).attr('href'),
      type:'get',
      dataType:'json',
      success: function(data){
        $('#deleteempleado').modal('close');
        listEmpleados();
      }
    });
  });
});
