$(function(){
    const item = '<li>Item</li>';
$('#add_item').click(function(){
    $('.my_list').prepend(item);
});

$('#remove_item').click(function(){
    $('.my_list li:last').remove();
});

$('#clear_list').click(function(){
    $('.my_list').empty();
});
});s