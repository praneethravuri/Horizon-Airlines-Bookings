$(document).ready(function(){
    $(".confirm-booking").click(function(){
        $.post('/confirm-payment').done(function(response){
            if(response && response["status"] == "error"){
                console.log("duplicate");
                document.getElementById("status").style.display = "block";
                document.getElementById("status").innerHTML = "You have already booked this flight"
            }
            else if(response && response["status"] == "booked"){
                document.getElementById("book-flight-status").style.display = "block";
                document.getElementById("book-flight-status").style.backgroundColor = "green";

            }
        });
    });
});
