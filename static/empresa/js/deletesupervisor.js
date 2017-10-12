$(document).on('ready', function(){
  $('#deleteempresa').modal();
  $('.delete_save_empresa').on('click',function(event){
    return false;
  });
  $('.delete_save_empresa').on('click',function(event){
    $.ajax({
      url:$(this).attr('href'),
      type:'get',
      dataType:'json',
      success: function(data){
        $('#deleteempresa').modal('close');
        listempresa();
      }
    });
  });
});


function funcionesEliminar(){
  $('.tabla_delete').on('click',function(event){
    var contenido ="<b>Empresa: </b>"+$(this).parents('tr').find('span.mod_empresa:first').text()+"<br>";
    contenido +="<b>Nit:</b> "+$(this).parents('tr').find('span.mod_nit:first').text()+"<br>";
    contenido +="<b>Ciudad: </b>"+$(this).parents('tr').find('span.mod_ciudad:first').text()+"<br>";
    contenido +="<b>Numero de tiendas:</b> "+$(this).parents('tr').find('span.mod_tienda:first').text()+"<br>";
    contenido +="<b>Telefono:</b> "+$(this).parents('tr').find('span.telefono:first').text()+"<br>";    
    contenido ="<h5>"+contenido+"</h5>";
    contenido +="<h5>Esta seguro que desea elimiar la Empresa?</h5>";
    $('.delete_save_empresa:first').attr('href',$(this).attr('href'));
    $('#cont_delete_mod').html(contenido);
    $('#deleteempresa').modal('open');
  });
}
