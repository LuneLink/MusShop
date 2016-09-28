/**
 * Created by wookie on 9/28/16.
 */

function AjaxService($http) {

    this.makeAjax = function (url, data) {
        console.log("IN AJAX");
        console.log(url);
        console.log(data);
            var promise = $http({
                method: "GET",
                url: url,
                params: {send: data}
            }).then(function mySucces(response) {
                console.log("LOOK AT ME");
                console.log(response.data);
                return response.data;
            });

        return promise;
    };
}
