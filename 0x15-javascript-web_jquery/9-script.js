// $(function () {
// 	const hello = $('#hello');
// 	$.ajax({
// 		type: 'GET',
// 		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
// 		success: (data) => {
// 			hello.text(data.hello);	
// 		}
// 	});
// });
$(function(){
	$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data, status){
		console.log(data)
	}, 'jsonp');
});