$(document).on('ready', function(){
  listsupervisor();
  $('#search').on('keyup', function(event){
    listsupervisor();
  });
});

function listsupervisor(){
  console.log("ejecutando",$("#tienda").val() != null);
  //if($("#tienda").val() != null){
  console.log($("#empresa").val() != "0",$("#ciudad").val() != "0",$("#tienda").val() != "0");
  console.log($("#empresa").val(),$("#ciudad").val(),$("#tienda").val());
      var res = "";
          res+= $("#search").val() != null? "&search="+$("#search").val():"";
      $.ajax({
        url:'/empresa/list/supervisor/?'+res,
        type:'get',
        dataType:'json',
        success:function(data){
          console.log(data);
          var emp = $('#tab_supervisor');
          emp.html("");
          var resul = data.object_list;
          var limite=data.count,inicio=0;
          if(resul.length){
            inicio = 0;
            for(var i=inicio;i < limite;i++){
              console.log("************------------------*****************");
              var empresa = resul[i].first_name,
                  apellido = resul[i].last_name,
                  user = resul[i].username,
                  celular = resul[i].celular,
                  empresas = resul[i].nom_empresa,
                  servicios = resul[i].servicios;
                  var temporal="";
                  var resul_emp = empresas.split(","),ul_emp="";
                  for(var k=1; k<resul_emp.length;k++){
                    ul_emp+="<li>"+resul_emp[k]+"</li>";
                  }
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_apellido\" >"+apellido+"</span></td>";
                  temporal+="<td><span class=\"mod_username\" >"+user+"</span></td>";
                  temporal+="<td><span class=\"mod_celular\" >"+celular+"</span></td>";
                  temporal+="<td><span class=\"mod_empresas\" ><ul class=\"lis_emp_tem\"><ul class=\"listempp\">"+ul_emp+"</ul></span></td>";
                  var d= "<ul class=\"tabla_tool\">";
                  d+="<li><a href =\""+servicios.delete+"\" class=\"btn-floating red tabla_delete\"><i class=\"material-icons\">delete</i></a></li>";
                  d+="<li><a href =\""+servicios.edit+"\" class=\"btn-floating yellow modf_supervisor\"><i class=\"material-icons\">edit</i></a></li>";
                  temporal+="<td>"+d+"</td>";
                  emp.append("<tr>"+temporal+"</tr>")
            }
            $('.tabla_delete, .tabla_edit').on('click', function(event){
              return false;
            });

            $('.tabla_edit').on('click', function(event){
              console.log("desde los tool tabla");
            });
            funcionesModificarSupervisor();
            funcionesEliminar();
            // eventosDePaginador();
          }
        }
      });
  //  }
}
