$('.form-contato').on('submit', function(e){
	e.preventDefault();
	var valores = $(this).serialize();
	$('#myModal').modal('show');
	$.post(this.action, valores, function(data){
		$('#myModal').hide();	
		$('.modal-backdrop').hide();
		$('body').removeClass('modal-open');	
		$('#div-form-contato').html(data);
	}).fail(function(){
		$('#myModal').hide();	
		$('.modal-backdrop').hide();
		$('body').removeClass('modal-open');	
		$('#div-form-contato').html(data);
	});	
});

function myMap() {
	var myCenter = new google.maps.LatLng(41.878114, -87.629798);
	var mapProp = {center:myCenter, zoom:12, scrollwheel:false, draggable:false, mapTypeId:google.maps.MapTypeId.ROADMAP};
	var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
	var marker = new google.maps.Marker({position:myCenter});
	marker.setMap(map);
}