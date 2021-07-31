function tabHighLight() {
    const tabs = $(".navbar-link")
    const pagename = $("#page-name").text()
    $(".navbar-link").each(function() {
        if ($(this).text() == pagename) {
            $(this).addClass("selected-tab");
        }
    })
}

function toggleNav() {
    if ($('#navbar').is(':visible')) {
        $('#navbar').animate({
            width: 'toggle'
        })
        $('#content').removeClass('uk-width-5-6')
        $('#content').addClass('uk-width-1-1')
    } else {
        $('#navbar').animate({
            width: 'toggle'
        })
        $('#content').removeClass('uk-width-1-1')
        $('#content').addClass('uk-width-5-6')
    }
}