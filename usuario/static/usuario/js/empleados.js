var pagina=0,proxima=0,bandera=true,b2=true;
$(document).on('ready', function(){
  //console.log("hola mundo pelao");
  $('.delete_save_empleado, .addempleado').on('click', function(event){
    return false;
  });
  $('#empresa').on('change', function(){
    //console.log("entro ... ",$(this).val(),$(this).val() != "0");
    if($(this).val() != "0"){
      $.ajax({
        url:'/empresa/list/ciudad/?empresa='+$(this).val(),
        type:'get',
        dataType:'json',
        success:function(data){
          //console.log("en el ajax");
          var ciudad = $('#ciudad');
          //console.log("1");
          ciudad.html('<option value="0" disabled selected>Selecioné</option>');
          //console.log("2",data.length > 0,data.object_list.length);
          var resul = data.object_list;
          $('#ciudad').material_select('destroy');
          if (resul.length > 0){
            //console.log("3");
            $('#ciudad').prop('disabled',false);
            for(var i=0; i < resul.length; i++){
              //console.log(resul[i].id,"  ",resul[i].nombre);
              ciudad.append("<option value=\""+resul[i].id+"\">"+resul[i].nombre+"</option>");
            }
          }else{
            $('#ciudad, #tienda').material_select('destroy');
            $('#ciudad, #tienda').prop('disabled',true);
          }
          $('#ciudad, #tienda').material_select();
        }
      });
      bandera=true;
      b2=true;
    }else{
      //console.log("pelao nada");
    }
  });
  $('#ciudad').on('change',function(event){
    //console.log("entro ... ",$(this).val(),$(this).val() != "0");
    if($(this).val() != "0"){
      $.ajax({
        url:'/empresa/list/tienda/?empresa='+$("#empresa").val()+"&ciudad="+$(this).val(),
        type:'get',
        dataType:'json',
        success:function(data){
          //console.log("en el ajax");
          var tienda = $('#tienda');
          //console.log("1");
          tienda.html('<option value="0" disabled selected>Selecioné</option>');
          //console.log("2",data.length > 0,data.object_list.length);
          var resul = data.object_list;
          $('#tienda').material_select('destroy');
          if (resul.length > 0){
            //console.log("3");
            $('#tienda').prop('disabled',false);
            for(var i=0; i < resul.length; i++){
              //console.log(resul[i].id,"  ",resul[i].nombre);
              tienda.append("<option value=\""+resul[i].id+"\">"+resul[i].nombre+"</option>");
            }
          }else{
            $('#tienda').material_select('destroy');
            $('#tienda').prop('disabled',true);
          }
          $('#tienda').material_select();
        }
      });
      bandera=true;
      b2=true;
    }else{
      //console.log("pelao nada");
    }
  });
  $('#ciudad, #empresa, #tienda').on('change',function(event){
    listEmpleados();
  });
  listEmpleados();
  $('#search').on('keyup', function(event){
    listEmpleados();
  });
  $('select').material_select();
});

function listEmpleados(){
  console.log("ejecutando",$("#tienda").val() != null);
  //if($("#tienda").val() != null){
  console.log($("#empresa").val() != "0",$("#ciudad").val() != "0",$("#tienda").val() != "0");
  console.log($("#empresa").val(),$("#ciudad").val(),$("#tienda").val());
      var res = "";
      res+= $("#empresa").val() != null? "empresa="+$("#empresa").val():"",
          res+= $("#ciudad").val() != null? "&ciudad="+$("#ciudad").val():"",
          res+= $("#tienda").val() != null? "&tienda="+$("#tienda").val():"",
          res+= $("#search").val() != null? "&search="+$("#search").val():"";
          res+= proxima != 0? "&pagina="+proxima*10:"";
      console.log(res);
      $.ajax({
        url:'/usuario/list/empleados/?'+res,
        type:'get',
        dataType:'json',
        success:function(data){
          console.log(data);
          var emp = $('#tab_emp');
          emp.html("");
          var resul = data.object_list;
          var limite=data.count,inicio=0;
          console.log('RESULTADOS   ',resul.length,'    ',data.count,'  ',resul);
          if(resul.length){
            inicio = 0;
            for(var i=inicio;i < limite;i++){
              console.log("************------------------*****************");
              var empresa = resul[i].empresa_e,
                  ciudad = resul[i].ciudad_e,
                  tienda = resul[i].tienda_e,
                  identificacion = resul[i].identificacion,
                  nombre = resul[i].first_name,
                  apellidos = resul[i].last_name,
                  servicios = resul[i].servicios;
                  var temporal="";
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_ciudad\" >"+ciudad+"</span></td>";
                  temporal+="<td><span class=\"mod_tienda\" >"+tienda+"</span></td>";
                  temporal+="<td><span class=\"mod_identificacion\" >"+identificacion+"</span></td>";
                  temporal+="<td><span class=\"mod_nombre\" >"+nombre+"</span></td>";
                  temporal+="<td><span class=\"mod_apellidos\" >"+apellidos+"</span></td>";
                  var d= "<ul class=\"tabla_tool\">";
                  d+="<li><a href =\""+servicios.delete+"\" class=\"btn-floating red tabla_delete\"><i class=\"material-icons\">delete</i></a></li>";
                  d+="<li><a href =\""+servicios.edit+"\" class=\"btn-floating yellow tabla_edit modf_empleado\"><i class=\"material-icons\">edit</i></a></li>";
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
              contenido +="Tienda "+$(this).parents('tr').find('span.mod_tienda:first').text()+"<br><br>";
              contenido +="Identificacion "+$(this).parents('tr').find('span.mod_identificacion:first').text()+"<br><br>";
              contenido +="Nombre "+$(this).parents('tr').find('span.mod_nombre:first').text()+" "+$('.add').parents('tr').find('span.mod_apellidos:first').text()+"<br>";
              contenido ="<h5>"+contenido+"</h5>";
              contenido +="<h5>Esta seguro que desea elimiar a el empleado?</h5>";
              $('.delete_save_empleado:first').attr('href',$(this).attr('href'));
              $('#cont_delete_mod').html(contenido);
              $('#deleteempleado').modal('open');
            });
            funcionesModificar();
            eventosDePaginador();
            funcionesEliminar();
          }
        }
      });
  //  }
}
