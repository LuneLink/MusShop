/**
 * Created by wookie on 9/23/16.
 */


function testz() {
    console.log("testz");

    // $(document).ready(function() {
    //    $('#result').html("Changed!!");
    // });

    $(document).ready(function() {
        console.log("ready");
        $.ajax({
            type: 'GET',
            url: '/ajaxTest',
            //data: {"name": "Andrew", "nickname": "Aramis"},
            success: function (data) {
                console.log("success");
                $('#content').html(data);
            }
        });
    });
}