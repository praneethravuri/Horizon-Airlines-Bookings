$(document).ready(function(){
    $("#delete-account").click(function(){
        if(confirm("Are you sure you want to delete your account?")){
            console.log("deleted account");
        }
    });
});