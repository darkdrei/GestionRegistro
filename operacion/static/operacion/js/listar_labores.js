var pagina=0,proxima=0,bandera=true,b2=true,TOTAL_REGISTROS=0;
var my_cronos = null;
window.TEMPORAL_ID=0
var fecha1=null,fecha2=null;
$(document).on('ready', function(){
  $('select').material_select();
  listLabores();
  $('#busqueda').on('keyup', function(event){
    listLabores();
  });
});

function actualizarTiempos(){
    var date = new Date();
    $('.move_time').each(function(x){
      var date =new Date();
      console.log($(this));
      var fecha_inicio = $(this).parent().find('input[type="hidden"]');
      var fecha_actual = calcularTiempo(fecha_inicio.val(),date);
      $(this).text(parseFloat(fecha_actual.toFixed(2)));
      console.log(fecha_inicio,fecha_actual);
    });
}

function listLabores(){
      $.ajax({
        url:'/operacion/list/labor/?',
        type:'get',
        data:{busq:$('#busqueda').val()},
        dataType:'json',
        success:function(data){
          console.log(data);
          var emp = $('#labores');
          emp.html("");
          var resul = data.object_list;
          if(resul.length){
            var limite=0,inicio=0;
            if (proxima == 0){
              limite=10;
              incio=0;
            }else{
              limite = proxima*10;
              inicio = (proxima-1)*10;
              if (inicio < 0)
                inicio=0;
            }
            TOTAL_REGISTROS = data.count;
            var fecha_Actual = new Date();
            if(my_cronos != null){
              clearInterval(my_cronos);
            }
            for(var i=inicio;i < limite;i++){
              if (i < TOTAL_REGISTROS){
                console.log("entro ::::::::::::::::::::: en la reconstruccion");
                var identificacion = resul[i].identificacion,
                    nombre = resul[i].nombre,
                    apellidos = resul[i].apellidos,
                    inicio = resul[i].ini,
                    id = resul[i].id,
                    tiempo = resul[i].tiempo,
                    usuario = resul[i].usuario,
                    servicio = resul[i].servicios;
                    temporal="";
          					temporal+="<div class=\"col s12 m12 l12 cajaIn \">";
          					temporal+="<div class=\"col s12 m12 l12 caja\" >";
          					temporal+="<div class=\"row\">";
          					temporal+="<div class=\"col s9 m9 l9 datos\" >";
          					temporal+="<div class=\"row\">";
          					temporal+="<div class=\"col s5 m5 l5\">Nombre:"+nombre+" "+apellidos+"</div><br>";
          					temporal+="<div class=\"col s4 m4 l4\">Hora:"+inicio+"</div><br>";
          					temporal+="<div class=\"col s4 m4 l4\">Duracion:"+parseFloat(calcularTiempo(inicio, fecha_Actual)).toFixed(2)+"</div>";
          					temporal+="</div>";
          					temporal+="</div>";
          					temporal+="<div class=\"col s1 m1 l1\" >";
                    temporal+="<input type=\"hidden\" name=\"username\"  value=\""+nombre+" "+apellidos+"\">";
                    temporal+="<input type=\"hidden\" name=\"ids\"  value=\""+id+"\">";
                    console.log('+++++++++++++++++++++++++++++++++++  ',servicio.edit);
          					temporal+="<a href=\""+servicio.edit+"\" class=\"btn-floating btn-large waves-effect waves-light #4db6ac edit_labor_emp\"><i class=\"material-icons\">phonelink_lock</i></a>";
          					temporal+="</div>";
          					temporal+="</div>";
          					temporal+="</div>";
          					temporal+="</div>";
          					temporal+="</div>";
                    emp.append(temporal);
                }
            }
            //my_cronos = setInterval(function(){ actualizarTiempos(); }, 2000);
            // var paginador = $('#paginador');
            // paginador.html("");
            // paginador.append('<li class="disabled"><a href="#!" class=\"ant\"><i class="material-icons">chevron_left</i></a></li>');
            // console.log(data.next);
            // if( bandera){
            //   console.log(data.count,' valor de impresion ',data.count/5);
            //   paginas = Math.round(data.count/10);
            //   proxima = data.next;
            //   if (paginas < 1){
            //     paginas =1;
            //     proxima=1;
            //   }
            //   bandera=false;
              // var paginador = $('#paginador');
              // paginador.html("");
              // paginador.append('<li class="disabled"><a href="#!" class=\"ant\"><i class="material-icons">chevron_left</i></a></li>');
            // }else{
            //   //borrar el iterador
            // }
            // for(var i=0; i< paginas;i++){
            //   var clase="";
            //   if (b2){
            //       clase = (i+1 == proxima-1?"active":"waves-effect");
            //   }else{
            //     clase = (i+1 == proxima?"active":"waves-effect");
            //   }
            //   paginador.append("<li class=\""+clase+"\"><a href=\""+(1+i)+"\" class=\"iterator\">"+(1+i)+"</a></li>");
            // }
            // b2=false;
            // paginador.append('<li class="waves-effect"><a href="#!" class=\"sig\"><i class="material-icons">chevron_right</i></a></li>');
            $('.tabla_delete, .tabla_edit, .editLabor, .edit_labor_emp').on('click', function(event){
              return false;
            });
            // $('.edit_labor_emp').on('click', function(event){
            //   $('#cerrarlaborc ').modal('open');
            // });
            cerrarLabor();
            // $('.tabla_delete').on('click', function(event){
            //   console.log("desde los tool tabla");
            // });
            // $('.tabla_edit').on('click', function(event){
            //   console.log("desde los tool tabla");
            // });
            eventosDePaginador();
          }
        }
      });
  //  }
}

function eventosDePaginador(){
  $('.iterator').on('click', function(event){
    return false;
  });
  $('.iterator').on('click', function(event){
    proxima = $(this).attr('href');
    $('.pagination li').removeClass('active');
    var actual = $('.pagination li.active');
    actual.removeClass('active');
    actual.addClass('waves-effect');
    var proximo = $(".pagination li a[href=\""+proxima+"\"");
    console.log("El cambio de elmento es ",proximo);
    proximo.parent().addClass('active');
    proximo.parent().removeClass('waves-effect');
    listLabores();
  });
}

function calcularTiempo(valor,fechaActual){
  fecha1 = fechaActual;
  var men = valor;
  console.log(men);
  var contenedor = men.split(" ");
  console.log(contenedor);
  var fecha = contenedor[0].split("/");
  console.log(fecha);
  var h = contenedor[1].split(':');
  console.log(h);
  var hora = h[0];
  console.log(hora);
  var minutos = h[1].substring(0, 2);
  var notacion = h[1].substring(2,4);
  var c = notacion=="PM"?String(parseInt(hora)+12) : hora ;
  var date_armado = new Date(fecha[2]+"-"+fecha[1]+"-"+fecha[0]+" "+c+":"+minutos+":00 UTC-5");
  fecha2 = date_armado;
  return parseFloat(fechaActual.getTime()-date_armado.getTime())/1000/(60*60).toFixed(2);
}


function cerrarLabor(){
  $('.sendLabor').on('click', function(event){return false;});
  $('.edit_labor_emp').on('click',function(event){
    console.log("se abrio la vaina");
    var usuario = $(this).parent().find('input[name="username"]').val();
        window.TEMPORAL_ID=$(this).parent().find('input[name="ids"]').val();
    $('#userc').val(usuario);
    $('#passwordc').val("");
    $('#cerrarlaborc').modal('open');
  });
  $('.sendLabor').on('click', function(event){return false;});
  $('.sendLabor').on('click', function(event){
      var user = $('#userc').val(),
      pass = $('#passwordc').val();
      var this_ = $(this);
      $.ajax({
        url:$(this).attr('href'),
        type:'post',
        dataType:'json',
        data:{user:user,pass:pass},
        success:function(data){
          console.log(data);
          if (!data[0].status){
            document.getElementById('form_labor').reset()
            $('#form_labor label[for="mensajec"]').text("Clave y usuario invalidos");
            return;
          }
          console.log("regreso del envio ",window.TEMPORAL_ID,"  *********  ",$('.tabla_edit:first').attr('href'));
          $.ajax({
            url:$('.edit_labor_emp:first').attr('href'),
            type:'post',
            dataType:'json',
            data:{id: window.TEMPORAL_ID},
            success:function(data){
              if (!data[0].status){
                document.getElementById('form_labor').reset()
                $('#form_labor label[for="mensaje"]').text("Clave y usuario invalidos");
              }else{
                $('#cerrarlaborc').modal('close');
                listLabores();
              }
            }
          });
        }
      });
    });
}
