$(document).ready(function(){
    $(".confirm-booking").click(function(){
        $.post('/confirm-payment').done(function(response){
            if(response && response["status"] == "error"){
                console.log("duplicate");
                document.getElementById("status").style.display = "block";
                document.getElementById("status").innerHTML = "You have already booked this flight"
            }
            else if(response && response["status"] == "booked"){
                document.getElementById("status").style.display = "block";
                document.getElementById("status").innerHTML = "Booked Flight Successfully"
                document.getElementById("status").style.backgroundColor = "green";

            }
        });
    });
});

$(document).ready(function(){
    $(".validate-btn").click(function(){
        $.post('/validate-promo-code').done(function(response){
            if(response  && response["status"] == "Invalid Promo Code"){
                document.getElementById("status").style.display = "block";
                document.getElementById("status").innerHTML = "Invalid Promo Code"
            }
        });
    });
})