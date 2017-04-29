var pagina=0,proxima=0,bandera=true,b2=true;

$(document).on('ready', function(){
	
  $('#ciudad').on('change',function(event){
    listEmpresas();
  });
  listEmpresas();
  $('#search').on('keyup', function(event){
    listEmpresas();
  });
  $('select').material_select();
});

function listEmpresas(){
      var res = "";
          res+= $("#ciudad").val() != null? "&ciudad="+$("#ciudad").val():"",
          res+= $("#search").val() != null? "&search="+$("#search").val():"";
          res+= proxima != 0? "&pagina="+proxima*10:"";
      console.log(res);
      $.ajax({
        url:'/empresa/list/empresa/?'+res,
        type:'get',
        dataType:'json',
        success:function(data){
          console.log(data);
          var empr = $('#tab_empr');
          empr.html("");
          var resul = data.object_list;
          var limite=data.count,inicio=0;
          console.log('RESULTADOS   ',resul.length,'    ',data.count,'  ',resul);
          if(resul.length){

            inicio = 0;
            for(var i=inicio;i < limite;i++){
              var empresa = resul[i].first_name,
                  ciudad = resul[i].ciudad,
                  n_tienda = resul[i].tiendas,  
                  telefono = resul[i].last_name,
                  servicios = resul[i].servicios;
                  var temporal="";
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_ciudad\" >"+ciudad+"</span></td>";
                  temporal+="<td><span class=\"mod_ntienda\" >"+n_tienda+"</span></td>";
                  temporal+="<td><span class=\"mod_telefono\" >"+telefono+"</span></td>";
                  d+="<li><a href =\""+servicios.delete+"\" class=\"btn-floating red tabla_delete\"><i class=\"material-icons\">delete</i></a></li>";
                  d+="<li><a href =\""+servicios.edit+"\" class=\"btn-floating yellow tabla_edit\"><i class=\"material-icons\">edit</i></a></li>";
                  d+="<li><a href =\""+servicios.pass+"\" class=\"btn-floating yellow tabla_edit\"><i class=\"material-icons\">add</i></a></li>";
                  temporal+="<td>"+d+"</td>";
                  emp.append("<tr>"+temporal+"</tr>")
            }

            $('.tabla_delete, .tabla_edit').on('click', function(event){
              return false;
            });
            $('.tabla_delete').on('click', function(event){
              console.log("desde los tool tabla");
            });
            $('.tabla_edit').on('click', function(event){
              console.log("desde los tool tabla");
            });
            $('.tabla_delete').on('click',function(event){
              var contenido ="Empresa "+$(this).parents('tr').find('span.mod_empresa:first').text()+"<br><br>";
              contenido +="Ciudad "+$(this).parents('tr').find('span.mod_ciudad:first').text()+"<br><br>";
              contenido +="N_Tienda "+$(this).parents('tr').find('span.mod_tienda:first').text()+"<br><br>";
              contenido +="telefono "+$(this).parents('tr').find('span.mod_identificacion:first').text()+"<br><br>";
              contenido +="<h5>Esta seguro que desea elimiar la empresa?</h5>";
              $('.delete_empresa:first').attr('href',$(this).attr('href'));
              $('#cont_delete_mod').html(contenido);
              $('#deleteempleado').modal('open');
            });
            eventosDePaginador();
          }
        }
      });
  //  }
}
