$(document).ready(function(){
    $(".add-flight-btn").click(function(){
        let flight_id = $(this).attr('id');
        console.log("reached addFlight.js")
        if(confirm("Are you sure you want to book this flight?")){
            $.post('/add-flight', {
                flight_id: flight_id
            }).done(function(response) {
                if (response && response['error'] == "booked") {
                    document.getElementsByClassName('flight-already-booked')[0].style.display = 'block';
                    $(window).scrollTop(0);
                }
            });
        }
    });
});