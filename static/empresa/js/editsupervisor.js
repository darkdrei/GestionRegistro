var temporal;
$(document).on('ready', function(){
  $('#editsupervisor').modal();
  $('.edit_modal_supervisor').on('click',function(event){
    return false;
  });
  $('.edit_modal_supervisor').on('click',function(event){
    var options = {
        //target:        '#output2',   // target element(s) to be updated with server response
        beforeSubmit:  showRequest,  // pre-submit callback
        success:       showResponse,  // post-submit callback
        error:error,

        // other available options:
        url:       $(this).attr('href'),         // override for form's 'action' attribute
        type:      'post' ,       // 'get' or 'post', override for form's 'method' attribute
        dataType:  'json',        // 'xml', 'script', or 'json' (expected server response type)
        //clearForm: true        // clear all form fields after successful submit
        //resetForm: true        // reset the form after successful submit

        // $.ajax options can be used here too, for example:
        //timeout:   3000
    };
    $("#add_form").ajaxSubmit(options);
  });
});

// pre-submit callback
function showRequest(formData, jqForm, options) {
    var queryString = $.param(formData);
    console.log('About to submit: \n\n' + queryString);
    return true;
}



function showResponse(responseText, statusText, xhr, $form)  {
  console.log("*********************************");
  temporal = responseText;
    console.log('status: ' + statusText + '\n\nresponseText: \n' + responseText +
        '\n\nThe output div should have already been updated with the responseText.');
  listsupervisor();
  $('#editsupervisor').modal('close');
}

function error(response,status,xhr){
  validadFormulario(response.responseJSON,"add_form");
}


function funcionesModificarSupervisor(){
  $('.modf_supervisor').on('click', function(event){
    console.log("++++++++++++++++++++++++++++");
    return false;
  });
  $('.modf_supervisor').on('click', function(event){
    console.log($(this).attr('href'));
    $('a.edit_modal_supervisor').attr('href',$(this).attr('href'));
    $("#edit_contenido").load($(this).attr('href'),function(responseTxt, statusTxt, xhr){
          alert(statusTxt+"   Error: " + xhr.status + ": " + xhr.statusText);
          $('#id_tienda, #id_ciudad').material_select();
          $('#add_form').submit(function() {
                return false;
            });
          $('#editsupervisor').modal('open');
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
          $('select').material_select();
    });
  });
}
