$(document).on('ready', function(){
  $('#deletemoto').modal();
  $('.delete_save_moto').on('click',function(event){
    return false;
  });
  $('.delete_save_moto').on('click',function(event){
    $.ajax({
      url:$(this).attr('href'),
      type:'get',
      dataType:'json',
      success: function(data){
        $('#deletemoto').modal('close');
        listMotos();
      }
    });
  });
});


function funcionesEliminar(){
  $('.tabla_delete').on('click',function(event){
    var contenido ="Empresa "+$(this).parents('tr').find('span.mod_empresa:first').text()+"<br>";
    contenido +="Ciudad "+$(this).parents('tr').find('span.mod_ciudad:first').text()+"<br>";
    contenido +="Tienda "+$(this).parents('tr').find('span.mod_tienda:first').text()+"<br>";
    contenido +="Identificacion "+$(this).parents('tr').find('span.mod_identificacion:first').text()+"<br>";
    contenido +="Nombre "+$(this).parents('tr').find('span.mod_nombre:first').text()+" "+$('.add').parents('tr').find('span.mod_apellidos:first').text()+"<br>";
    contenido +="Placa "+$(this).parents('tr').find('span.mod_placa:first').text()+"<br>";
    contenido +="Placa "+$(this).parents('tr').find('span.mod_placa:first').text()+"<br>";
    contenido +="Marca "+$(this).parents('tr').find('span.mod_marca:first').text()+"<br>";
    contenido +="Soat "+$(this).parents('tr').find('span.mod_soat:first').text()+"<br>";
    contenido ="<h5>"+contenido+"</h5>";
    contenido +="<h5>Esta seguro que desea elimiar la moto?</h5>";
    $('.delete_save_moto:first').attr('href',$(this).attr('href'));
    $('#cont_delete_mod').html(contenido);
    $('#deletemoto').modal('open');
  });
}
