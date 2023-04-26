$(document).ready(function(){
    $("#delete-account").click(function(){
        console.log("here")
        let id = $(this).attr('id');
        if(confirm("Are you sure you want to delete your account?")){
            $.post("/delete-account", {
                id : id
            }).done(function(){
                console.log("deleted account");
            });
        }
    });
});