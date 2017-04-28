$(document).on('ready', function(){
});
// function cerrarLabor(){
//   $('.tabla_edit').on('click',function(event){
//     return false;
//   });
//   $('.tabla_edit').on('click',function(event){
//     var usuario = $(this).parent().find('input[nam="username"]').val(),
//         id=$(this).parent().find('input[nam="ids"]').val();
//     console.log("****************** ",usuario);
//     $('#userc,#passwordc').val(usuario);
//     $('#passwordc').val("");
//     $('#cerrarlaborc').modal('open');
//
//     $.ajax({
//       url:$(this).attr('href'),
//       data:{id:id}
//       dataType:'json',
//       type:'get',
//       success:function(data){
//         console.log("el resultado del usuario ", data);
//         listLabores()
//         // if(data[0].status){
//         //   listLabores();
//         // }
//       }
//     });
//   });
// }
