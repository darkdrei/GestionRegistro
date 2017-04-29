function listEmpleados(){
  console.log("ejecutando",$("#tienda").val() != null);
  //if($("#tienda").val() != null){
  console.log($("#empresa").val() != "0",$("#ciudad").val() != "0",$("#tienda").val() != "0");
  console.log($("#empresa").val(),$("#ciudad").val(),$("#tienda").val());
      var res = "";
          res+= $("#search").val() != null? "&search="+$("#search").val():"";
      $.ajax({
        url:'/motorizado/list/moto/?'+res,
        type:'get',
        dataType:'json',
        success:function(data){
          console.log(data);
          var emp = $('#tab_mot');
          emp.html("");
          var resul = data.object_list;
          var limite=data.count,inicio=0;
          if(resul.length){
            inicio = 0;
            for(var i=inicio;i < limite;i++){
              console.log("************------------------*****************");
              var empresa = resul[i].empresa_e,
                  ciudad = resul[i].ciudad_e,
                  tienda = resul[i].tienda_e,
                  identificacion = resul[i].identificacion,
                  nombre = resul[i].first_name,
                   soat= resul[i].numeroS,
                  marca = resul[i].marca,
                  placa = resul[i].placa,
                  apellidos = resul[i].last_name,
                  servicios = resul[i].servicios;
                  var temporal="";
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_ciudad\" >"+ciudad+"</span></td>";
                  temporal+="<td><span class=\"mod_tienda\" >"+tienda+"</span></td>";
                  temporal+="<td><span class=\"mod_identificacion\" >"+identificacion+"</span></td>";
                  temporal+="<td><span class=\"mod_nombre\" >"+nombre+"</span></td>";
                  temporal+="<td><span class=\"mod_apellidos\" >"+apellidos+"</span></td>";
                  temporal+="<td><span class=\"mod_placa\" >"+placa+"</span></td>";
                  temporal+="<td><span class=\"mod_marca\" >"+marca+"</span></td>";
                  temporal+="<td><span class=\"mod_apellidos\" >"+soat+"</span></td>";
                  var d= "<ul class=\"tabla_tool\">";
                  d+="<li><a href =\""+servicios.delete+"\" class=\"btn-floating red tabla_delete\"><i class=\"material-icons\">delete</i></a></li>";
                  d+="<li><a href =\""+servicios.edit+"\" class=\"btn-floating yellow tabla_edit modf_empleado\"><i class=\"material-icons\">edit</i></a></li>";
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
            // funcionesModificar();
            // eventosDePaginador();
          }
        }
      });
  //  }
}
