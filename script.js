$(function () {
    $("a#process_input").bind("click")
})

function passUserLocation(x) {
    $.getJSON($SCRIPT_ROOT + '/check_evac', {
            post: x
        }, function (data) {
            let response = data.result;
            console.log(response);
        }
    });
}