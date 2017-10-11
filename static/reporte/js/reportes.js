var pagina=0,proxima=0,bandera=true,b2=true;

$(document).on('ready', function(){
  //console.log("hola mundo pelao");
  seleccionarEmpleados();
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    monthsFull: [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre' ],
    monthsShort: [ 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic' ],
    weekdaysFull: [ 'Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado' ],
    weekdaysShort: [ 'Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab' ],
    formatSubmit: 'dd/mm/yyyy',
    format: 'dd/mm/yyyy',
    onSet: function( arg ){
        if ( 'select' in arg ){
            this.close();
        }
    }
  });
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
  //listEmpleados();
  $('#search').on('keyup', function(event){
    listEmpleados();
  });
  $('select').material_select();
  listEmpleados();
});

function listEmpleados(){
      var res = "";
      res+= $("#empresa").val() != null? "empresa="+$("#empresa").val():"",
          res+= $("#ciudad").val() != null? "&ciudad="+$("#ciudad").val():"",
          res+= $("#tienda").val() != null? "&tienda="+$("#tienda").val():"",
          res+= $("#inicio").val().length>0? "&inicio="+$("#inicio").val():"",
          res+= $("#fin").val().length>0? "&fin="+$("#fin").val():"",
          res+= $("#search").val().length>0? "&busqueda="+$("#search").val():"";
          res+= proxima != 0? "&pagina="+proxima*10:"";
      $.ajax({
        url:'/reporte/ws/pagos/empledos/?'+res,
        type:'get',
        dataType:'json',
        success:function(data){
          var emp = $('#tab_emp');
          emp.html("");
          var resul = data;
          if(resul.length){
            inicio = 0;
            for(var i=inicio;i < resul.length;i++){
              var empresa = resul[i].nom_empre,
                  id = resul[i].id_empleado,
                  ciudad = resul[i].nombre,
                  tienda = resul[i].nom_tienda,
                  identificacion = resul[i].identificacion,
                  nombre = resul[i].nom_emp,
                  apellidos = resul[i].ape_emp,
                  horas = resul[i].total_horas,
                  total = resul[i].total_turnos;
                  var temporal="";
                  temporal+="<td><input value=\""+id+"\"name=\"reporte\" type=\"checkbox\" id=\"empl"+id+"\" ><label for=\"empl"+id+"\"></label></span></td>";
                  temporal+="<td><span class=\"mod_empresa\" >"+empresa+"</span></td>";
                  temporal+="<td><span class=\"mod_ciudad\" >"+ciudad+"</span></td>";
                  temporal+="<td><span class=\"mod_tienda\" >"+tienda+"</span></td>";
                  temporal+="<td><span class=\"mod_identificacion\" >"+identificacion+"</span></td>";
                  temporal+="<td><span class=\"mod_nombre\" >"+nombre+"</span></td>";
                  temporal+="<td><span class=\"mod_apellidos\" >"+apellidos+"</span></td>";
                  temporal+="<td><span class=\"mod_apellidos\" >"+total+"</span></td>";
                  temporal+="<td><span class=\"mod_apellidos\" >"+horas+"</span></td>";
                  temporal+="<td><a href=\"#\" class=\"report_especifico\"><input type=hidden value=\""+id+"\"><img src=\"/media/des1.png\"/></a></td>";
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
            //eventosDePaginador();
            //funcionesEliminar();
            //funcionesModificar();
            reportEspecifico();
          }
        }
      });
  }


function reportEspecifico(){
  $('.report_especifico').on('click',function(event){
    var r = $(this).parent().find('input[type="hidden"]').val();
    var res = "?";
    res+= $("#inicio").val().length>0? "&inicio="+$("#inicio").val():"",
        res+= $("#fin").val().length>0? "&fin="+$("#fin").val():"",
        res+="&reporte="+r;
        res+= proxima != 0? "&pagina="+proxima*10:"";
        window.open("/reporte/pagos/empledo/especifico/imprimir/"+res, '_blank');
  });
}

  function seleccionarEmpleados(){
    $('.all_empleados').click(function(event){
      if($(this).prop('checked')){
         $('input[name="reporte"]').prop('checked', true);
      }else{
        $('input[name="reporte"]').prop('checked', false);
      }

    });
    $('.reporte_general').click(function(event){
      var res = "?";
      res+= $("#inicio").val().length>0? "&inicio="+$("#inicio").val():"",
          res+= $("#fin").val().length>0? "&fin="+$("#fin").val():"",
          res+="&"+$('form input[name="reporte"]').serialize();
          res+= proxima != 0? "&pagina="+proxima*10:"";
          window.open("/reporte/ws/pagos/empledos/imprimir/"+res, '_blank');
    });
  }
