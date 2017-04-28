var temporal;
$(document).on('ready', function(){
  $('#addempleado').modal();
  $('.addempleado').on('click', function(event){
    return false;
  });
  $('.addempleado').on('click', function(event){
    $("#contenido").load($(this).attr('href'),function(responseTxt, statusTxt, xhr){
          alert(statusTxt+"   Error: " + xhr.status + ": " + xhr.statusText);
          $('#id_tienda, #id_ciudad').material_select();
          $('#modal_add_empleado').submit(function() {
                return false;
            });
          $('#addempleado').modal('open');
          $('.saveempleado').on('click',function(event){
            var options = {
                //target:        '#output2',   // target element(s) to be updated with server response
                beforeSubmit:  showRequest,  // pre-submit callback
                success:       showResponse,  // post-submit callback
                error:error,

                // other available options:
                url:       '/usuario/add/empleado/',         // override for form's 'action' attribute
                type:      'post' ,       // 'get' or 'post', override for form's 'method' attribute
                dataType:  'json',        // 'xml', 'script', or 'json' (expected server response type)
                //clearForm: true        // clear all form fields after successful submit
                //resetForm: true        // reset the form after successful submit

                // $.ajax options can be used here too, for example:
                //timeout:   3000
            };
            $("#modal_add_empleado").ajaxSubmit(options);
          });
    });
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
}

function error(response,status,xhr){
  console.log(response.responseJSON);
  $.each(response.responseJSON, function( k, v ) {
  console.log( "Key: " + k + ", Value: " + v );
});
}
