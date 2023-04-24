$(document).ready(function(){
    $(".add-flight-btn").click(function(){
        let flight_id = $(this).attr('id');
        if(confirm("Are you sure you want to book this flight?")){
            $.post('/add-flight', {
                flight_id: flight_id
            }).done(function() {
                console.log("sent message");
            });
        }
    })
})