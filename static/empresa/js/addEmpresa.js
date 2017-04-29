$(document).on('ready', function(){
  $('#addEmpresa').modal();
  $('.addEmpresa,.saveEmpresa').on('click', function(event){
    return false;
  });
  $('.addEmpresa').on('click', function(event){
    $("#contenido").load($(this).attr('href'),function(responseTxt, statusTxt, xhr){
          $('#add_form').submit(function() {
                return false;
          });
          $('#addEmpresa').modal('open');
          
          $('select').material_select();
          $('.saveEmpresa').on('click',function(event){
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
            console.log('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨__***');
            //$("#add_form").submit();
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
  listMotos()
  $('#addEmpresa').modal('close');
}

function error(response,status,xhr){
  console.log("se exploto la vaina");
  validadFormulario(response.responseJSON,"add_form");
}
