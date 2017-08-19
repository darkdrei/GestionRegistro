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
          console.log(data,"   ",res,"  ",res.length);
          if (res.length == 0){
            $('#mensaje_empleado').modal('open');
          }else{
            $('#empleado').material_select('destroy');
            var men="<option value=\"0\" disabled selected>Seleccione Trabajador</option>";
            for(var i=0;i < res.length; i++ ){
              men+="<option value=\""+res[i].emp_id+"\">"+res[i].nombre+" "+res[i].apellidos+"</option>";
            }
            $('#empleado').html(men);
            $('#empleado').material_select();
            $('#addlabor').modal('open');
          }
      }
    });
  })

});
