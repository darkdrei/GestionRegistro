$(document).on('ready', function(){
  listMotos();
  $('#search').on('keyup', function(event){
    listMotos();
  });
});

function listMotos(){
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
                  nombre = resul[i].nombre,
                   soat= resul[i].numeroS,
                  marca = resul[i].marca,
                  placa = resul[i].placa,
                  apellidos = resul[i].apellidos,
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
                  temporal+="<td><span class=\"mod_soat\" >"+soat+"</span></td>";
                  var d= "<ul class=\"tabla_tool\">";
                  d+="<li><a href =\""+servicios.delete+"\" class=\"btn-floating red tabla_delete\"><i class=\"material-icons\">delete</i></a></li>";
                  d+="<li><a href =\""+servicios.edit+"\" class=\"btn-floating yellow modf_moto\"><i class=\"material-icons\">edit</i></a></li>";
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
            funcionesModificarMoto();
            funcionesEliminar();
            // eventosDePaginador();
          }
        }
      });
  //  }
}
