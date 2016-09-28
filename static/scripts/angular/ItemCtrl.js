/**
 * Created by wookie on 9/28/16.
 */

function ItemCtrl($scope, $routeParams, NamesService, AjaxService) {

    this.makeAjax = function (url, data) {
        var result = AjaxService.makeAjax(url, data);

        result.then(function(response) {
            $scope.id = response.id;
            $scope.information = response.information;
            $scope.cost = response.cost;
            $scope.manufacturer = response.manufacturer;
            $scope.model = response.model;
        })
    };

    this.makeAjax('/getCurrent', $routeParams.currentId);
    // $http({
    //     method: "GET",
    //     url: '/getCurrent',
    //     params: {currentId: $routeParams.currentId}
    // }).then(function mySucces(response) {
    //     //$scope.myWelcome = response.data;
    //     $scope.id = response.data.id;
    //     $scope.information = response.data.information;
    //     $scope.cost = response.data.cost;
    //     $scope.manufacturer = response.data.manufacturer;
    //     $scope.model = response.data.model;
    //     console.log(response.data);
    // });

    $scope.getPicture = function (man, model) {
        return NamesService.getPicture(man, model);
    };

    $scope.getFullName = function (man, model) {
        return NamesService.getFullName(man, model);
    }
}