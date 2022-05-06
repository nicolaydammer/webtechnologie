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

    $(".delete_regisseur").on('click', function (event) {
        let regisseur_id = event.currentTarget.id
        let url = "/regisseur/" + regisseur_id
        $.ajax({
            url: url,
            method: "DELETE"
        }).done(function () {
            location.reload(true);
        })
    })

    $(".delete_acteur").on('click', function (event) {
        let acteur_id = event.currentTarget.id
        let url = "/acteur/" + acteur_id
        $.ajax({
            url: url,
            method: "DELETE"
        }).done(function () {
            location.reload(true);
        })
    })

    $(".delete_comment").on('click', function (event) {
        let comment_id = event.currentTarget.id
        let url = "/comment/" + comment_id
        $.ajax({
            url: url,
            method: "DELETE"
        }).done(function () {
            location.reload(true);
        })
    })
})

function goTo(url) {
    location.href=url;
}
