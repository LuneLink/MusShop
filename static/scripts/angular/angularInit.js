/**
 * Created by wookie on 9/26/16.
 */

function Route($routeProvider, path) {
    $routeProvider

    .when("/", {
        templateUrl: "homePage.htm",
        resolve: {
            data: function () {
                console.log("/////////////1");
            }
        }
    })
    .when("/itemList/:typeId/:pageId", {
        templateUrl: "itemList.htm",
        controller: 'ListCtrl',
        resolve: {
            data: function () {
                console.log("/////////////2");
            }
        }
    })
    .when("/getCurrent/:typeId/:currentId", {
        templateUrl: "currentItem.htm",
        controller: 'ItemCtrl',
        resolve: {
            data: function () {
                console.log("/////////////3");
            }
        }

    })
    .when("/successPurchase", {
        templateUrl: "successPurchase.htm",
        // controller: 'successController',
        resolve: {
            data: function () {
                console.log("/////////////4");
            }
        }

    })
    .otherwise({
        controller: 'BucketCtrl'
    });
}

var app = angular.module('app', ["ngRoute"]);
app.factory('CacheFactory', function($cacheFactory) {
    var cache = $cacheFactory('cachedBucket');
    cache.put('bucket', []);
    return cache;
});
app.service('AjaxService', AjaxService);
app.service('NamesService', NamesService);
app.controller('BucketCtrl', ['$scope', '$location', 'CacheFactory', 'AjaxService', BucketCtrl]);
app.controller('ListCtrl', ['$scope','$routeParams', 'NamesService', 'AjaxService', ListCtrl]);
app.controller('ItemCtrl', ['$scope','$routeParams', 'NamesService', 'AjaxService', ItemCtrl]);
app.config(['$routeProvider', Route]);
