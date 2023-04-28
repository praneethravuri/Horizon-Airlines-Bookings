$(document).ready(function(){
    $(".confirm-booking").click(function(){
        $.post('/confirm-payment');
        console.log("here");
    });
});