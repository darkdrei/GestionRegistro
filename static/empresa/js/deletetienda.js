$(document).on('ready', function(){
  $('#deletetienda').modal();
  $('.delete_save_tienda').on('click',function(event){
    return false;
  });
  $('.delete_save_tienda').on('click',function(event){
    $.ajax({
      url:$(this).attr('href'),
      type:'get',
      dataType:'json',
      success: function(data){
        $('#deletetienda').modal('close');
        listtienda();
      }
    });
  });
});


function funcionesEliminar(){
  $('.tabla_delete').on('click',function(event){
    var contenido ="<b>Tienda: </b>"+$(this).parents('tr').find('span.mod_tienda:first').text()+"<br>";
    contenido +="<b>Ciudad: </b>"+$(this).parents('tr').find('span.mod_ciudad:first').text()+"<br>";
    contenido +="<b>Empresa: </b>"+$(this).parents('tr').find('span.mod_empresa:first').text()+"<br>";
    contenido +="<b>telefono: </b>"+$(this).parents('tr').find('span.mod_telefono:first').text()+"<br>";
    contenido ="<h6>"+contenido+"</h6>";
    contenido +="<h6>Esta seguro que desea elimiar la Tienda?</h6>";
    $('.delete_save_tienda:first').attr('href',$(this).attr('href'));
    $('#cont_delete_mod').html(contenido);
    $('#deletetienda').modal('open');
  });
}
