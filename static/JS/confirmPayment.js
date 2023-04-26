$(document).ready(function(){
    $(".confirm-booking").click(function(){
        $.post('/confirm-payment');
    })
})