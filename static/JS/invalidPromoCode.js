$(document).ready(function(){
    $(".validate-btn").click(function(){
        $.post('/validate-promo-code').done(function(response){
            if(response){
                document.getElementById("status").style.display = "block";
                document.getElementById("status").innerHTML = "Invalid Promo Code"
                $(window).scrollTop(0);
            }
        });
    });
})