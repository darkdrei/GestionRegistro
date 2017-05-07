function validadFormulario(data,nom_form){
  $("#"+nom_form+" input.invalid, #"+nom_form+" select.invalid, #"+nom_form+" input.select-dropdown").removeClass('invalid');
  $.each(data, function( k, v ) {
    console.log( "Key: " + k + ", Value: " + v );
    var field = $("input[name=\""+k+"\"]");
    if (field.length==0){
      var field = $("select[name=\""+k+"\"]");
      field.parent().find('input.select-dropdown').addClass('invalid')
      return;
    }
    field.addClass('invalid');
  });
}
