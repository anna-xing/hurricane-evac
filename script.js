$(function() {
    $("a#process_input").bind("click")
})

/* wtf is this */
$.post("/postmethod", {
    canvas_data: JSON.stringify(outputData)
}, function (err, req, resp) {
    window.location.href = "/results/" + resp["responseJSON"]["uuid"];
})