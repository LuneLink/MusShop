/**
 * Created by wookie on 9/27/16.
 */

function ListCtrl($scope, $routeParams, NamesService, AjaxService) {
    console.log("FUCK YEAAAH");

    this.makeAjax = function (url, data) {
        var result = AjaxService.makeAjax(url, data);

        result.then(function(response) {
            $scope.content = response.content;
        })
    };

    this.makeAjax('/itemList', $routeParams.id);

    // $http({
    //     method: "GET",
    //     url: '/itemList',
    //     params: {tester: $routeParams.id}
    // }).then(function mySucces(response) {
    //     //$scope.myWelcome = response.data;
    //     $scope.myWelcome = response.data.message;
    //     $scope.content = response.data.content;
    //     $scope.manufacturer = response.data.content[0].manufacturer;
    //     $scope.model = response.data.content[0].model;
    //     console.log(response.data);
    //     //$('#content').html(response.data);
    //     //return response.data;
    // });

    $scope.image = "images/Jackson_KingV.png";

    $scope.getPicture = function (man, model) {
        return NamesService.getPicture(man, model);
    };

    $scope.getFullName = function (man, model) {
        return NamesService.getFullName(man, model);
    }
}
