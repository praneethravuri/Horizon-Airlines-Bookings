$(document).ready(function(){
    $(".add-flight-btn").click(function(){
        let flight_id = $(this).attr('id');
        if(confirm("Are you sure you want to book this flight?")){
            $.post('/add-flight', {
                flight_id: flight_id
            }).done(function(response) {
                if (response && response['error'] == "booked") {
                    document.getElementsByClassName('flight-already-booked')[0].style.display = 'block';
                }
                else if(response){
                    let flight_id = response["flight_id"];
                    $.ajax({
                        type: "POST",
                        contentType:'application/json;charset-utf-08',
                        dataType:'json',
                        url : 'http://127.0.0.1:5000/payment?value='+flight_id,
                        success : function(data){
                            let reply = data.reply;
                            if(reply == "success"){
                                return;
                            }
                            else{
                                alert("Something went wrong");
                            }
                        }
                    });
                }
            });
        }
    });
});