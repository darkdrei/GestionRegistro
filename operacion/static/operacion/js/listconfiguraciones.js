$(document).on('ready', function(){
  listConfiguracion();
  $('#search').on('keyup', function(event){
    listConfiguracion();
  });
});

function listConfiguracion(){
      var res = "";
          res+= $("#search").val() != null? "&search="+$("#search").val():"";
      $.ajax({
        url:'/operacion/list/configuracion/?'+res,
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
              var empresa = resul[i].empresa__first_name,
                  dias = resul[i].seldias,
                  valor = resul[i].valor,
                  servicios = resul[i].servicios;
                  var temporal="";
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_dias\" >"+dias+"</span></td>";
                  temporal+="<td><span class=\"mod_valor\" >"+valor+"</span></td>";
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
            // funcionesModificarMoto();
            // funcionesEliminar();
            // eventosDePaginador();
          }
        }
      });
  //  }
}
