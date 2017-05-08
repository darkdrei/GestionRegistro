$(document).on('ready', function(){
  listempresa();
  $('#search').on('keyup', function(event){
    listempresa();
  });
});

function listempresa(){
  console.log("ejecutando",$("#tienda").val() != null);
  //if($("#tienda").val() != null){
  console.log($("#empresa").val() != "0",$("#ciudad").val() != "0",$("#tienda").val() != "0");
  console.log($("#empresa").val(),$("#ciudad").val(),$("#tienda").val());
      var res = "";
          res+= $("#search").val() != null? "&search="+$("#search").val():"";
      $.ajax({
        url:'/empresa/list/empresa/?'+res,
        type:'get',
        dataType:'json',
        success:function(data){
          console.log(data);
          var emp = $('#tab_empr');
          emp.html("");
          var resul = data.object_list;
          var limite=data.count,inicio=0;
          if(resul.length){
            inicio = 0;
            for(var i=inicio;i < limite;i++){
              console.log("************------------------*****************");
              var empresa = resul[i].first_name,
                  nit = resul[i].nit,
                  ciudad = resul[i].ciudad__nombre,
                  tiendas = resul[i].tiendas,
                  telefono = resul[i].telefono,
                  servicios = resul[i].servicios;
                  var temporal="";
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_nit\" >"+nit+"</span></td>";
                  temporal+="<td><span class=\"mod_ciudad\" >"+ciudad+"</span></td>";
                  temporal+="<td><span class=\"mod_tiendas\" >"+tiendas+"</span></td>";
                  temporal+="<td><span class=\"mod_telefono\" >"+telefono+"</span></td>";
                  var d= "<ul class=\"tabla_tool\">";
                  d+="<li><a href =\""+servicios.delete+"\" class=\"btn-floating red tabla_delete\"><i class=\"material-icons\">delete</i></a></li>";
                  d+="<li><a href =\""+servicios.edit+"\" class=\"btn-floating yellow modf_empresa\"><i class=\"material-icons\">edit</i></a></li>";
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
            //funcionesModificarMoto();
            //funcionesEliminar();
            // eventosDePaginador();
          }
        }
      });
  //  }
}
