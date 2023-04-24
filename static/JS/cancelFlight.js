$(document).ready(function() {
    $('.cancel-btn').click(function() {
        var flight_id = $(this).attr('id');
        if (confirm("Are you sure you want to delete this flight?")) {
            $.post('/delete-flight', {
                flight_id: flight_id
            }).done(function() {
                $("#table-" + flight_id).hide();
            });
        }
    });
});

