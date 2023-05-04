$(document).ready(function(){
    $(".admin-add-flight").click(function(){
        $(".add-form").show();
        $(".update-form").hide();
        $(".delete-form").hide();
    });

    $(".admin-update-flight").click(function(){
        $(".add-form").hide();
        $(".update-form").show();
        $(".delete-form").hide();
    });

    $(".admin-delete-flight").click(function(){
        $(".add-form").hide();
        $(".update-form").hide();
        $(".delete-form").show();
    });
});