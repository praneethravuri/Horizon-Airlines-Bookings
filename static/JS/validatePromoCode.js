$(document).ready(function(){
    $(".validate-btn").click(function(){
        $.post('/validate-promo-code');
        console.log("here");
    });
});