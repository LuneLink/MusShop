/**
 * Created by wookie on 9/25/16.
 */

function showCurrent(id) {
    $(document).ready(function() {
        console.log("ready");
        $.ajax({
            type: 'GET',
            url: '/getCurrent',
            data: {"id": id},
            success: function (data) {
                console.log("success");
                $('#content').html(data);
            }
        });
    });
}
