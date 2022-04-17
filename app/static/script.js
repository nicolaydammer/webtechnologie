$(document).ready(function () {
    $("#logout").on('click', function () {
        $.ajax({
            url: "/logout",
            method: "POST"
        }).done(function () {
            location.reload(true);
        })
    })
    
    $("#delete").on('click', function (event) {
        event.preventDefault()
        let url = document.URL;
        let id = url.substring(url.lastIndexOf('/') + 1);

        $.ajax({
            url: "/film/" + id,
            method: "DELETE"
        }).done(function () {
            document.location.href="/";
        })
    })
})

