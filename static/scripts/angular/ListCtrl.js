/**
 * Created by wookie on 9/27/16.
 */

function ListCtrl($scope, $routeParams, NamesService, AjaxService) {
    console.log("FUCK YEAAAH");

    //$scope.currentSearchState = false;

    $scope.changeSearchState = function () {
        $scope.currentSearchState = !$scope.currentSearchState;
    };

    $scope.getParams = function (typeId, pageId, searchParams) {
        if(searchParams == null)
            searchParams = {};

        return {'typeId': typeId,
                'pageId': pageId,
                'searchParams': searchParams}
    };

    $scope.getSearchData = function (searchType, searchValue) {
        console.log("Search data");
        console.log(searchType);
        console.log(searchValue);

        return {
            'searchType' : searchType,
            'searchValue': searchValue
        }
    };

    $scope.formPages = function (count) {
        res = [];

        for(var i = 1; i <= count; i++)
            res.push(i);

        return res;
    };

    $scope.makeAjax = function (url, data) {
        var result = AjaxService.makeAjax(url, data);
        $scope.currentSearchState = false;

        result.then(function(response) {
            $scope.content = JSON.parse(response.content);
            $scope.pageCount = $scope.formPages(response.pageCount);
        })
    };

    $scope.makeAjax('/itemList', $scope.getParams($routeParams.typeId, $routeParams.pageId));

    $scope.pageId = $routeParams.pageId;
    $scope.typeId = $routeParams.typeId;
    //$scope.pageId = 1;
    // $scope.image = "images/Jackson_KingV.png";

    $scope.searchType = "None";
    $scope.searchValue = "";

    $scope.getPicture = function (man, model) {
        return NamesService.getPicture(man, model);
    };

    $scope.getFullName = function (man, model) {
        return NamesService.getFullName(man, model);
    }
}
