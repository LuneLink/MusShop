/**
 * Created by wookie on 9/25/16.
 */

var isOpen = false;

function stateHandler() {
    if(isOpen)
        bucketClose();
    else
        bucketOpen()
}

function bucketOpen() {
    isOpen = true;
    console.log("opened");

    $(document).ready(function() {
        console.log("ready");
        $.ajax({
            type: 'GET',
            url: '/bucketOpen',
            //data: {"name": "Andrew", "nickname": "Aramis"},
            success: function (data) {
                console.log("success");
                $('#bucket').html(data);
            }
        });
    });
}

function bucketClose() {
    isOpen = false;
    console.log("closed");

    $(document).ready(function() {
       $('#bucket').html("");
    });
}
