$(document).ready(function () {
    $("#logout").on('click', function () {
        $.ajax({
            url: "/logout",
            method: "POST"
        }).done(function () {
            location.reload(true);
        })
    })
})

