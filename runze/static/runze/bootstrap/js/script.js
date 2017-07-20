$('.menu-item').on('click', function(e){
	e.preventDefault();
	topoHt = $(".navbar").height()+16	;
	var id = $(this).attr('id');
	var sec = $('#conteudo').find('section.'+id)
	$("html, body").animate({scrollTop: sec.offset().top-topoHt}, 200);
});
$('.form-contato').on('submit', function(e){
	e.preventDefault();
	var valores = $(this).serialize();
	$('#myModal').modal('show');
	$.post(this.action, valores, function(data){
		$('#myModal').hide();	
		$('.modal-backdrop').hide();
		$('body').removeClass('modal-open');	
		$('#div-contato').html(data);
		//$('#div-resposta').find('span').html('Mensagem enviada com sucesso! Obrigado!');
	}).fail(function(){
		$('#myModal').hide();	
		$('.modal-backdrop').hide();
		$('body').removeClass('modal-open');	
		//$('#div-resposta').find('span').html('Ocorrou algum problema ao enviar mensagem, tente novamente mais tarde. Obrigado');
	});	
});

function myMap() {
	var myCenter = new google.maps.LatLng(-5.527286, -47.492012);
	var mapProp = {center:myCenter, zoom:16, scrollwheel:false, draggable:false, mapTypeId:google.maps.MapTypeId.ROADMAP};
	var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
	var marker = new google.maps.Marker({position:myCenter});
	marker.setMap(map);
}