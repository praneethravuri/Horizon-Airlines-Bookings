$(document).ready(function(){
    $(".confirm-booking").click(function(){
        $.post('/confirm-payment').done(function(response){
            if(response && response["status"] == "error-dup"){
                console.log("duplicate");
                document.getElementById("status-dup").style.display = "block";
                document.getElementById("status-dup").innerHTML = "You have already booked this flight"
                $(window).scrollTop(0);
            }
            else if(response && response["status"] == "booked"){
                document.getElementById("book-flight-status").style.display = "block";
                document.getElementById("book-flight-status").style.backgroundColor = "green";
                $(window).scrollTop(0);

            }
        });
    });
});
