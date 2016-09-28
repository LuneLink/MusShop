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
    .when("/itemList/:id", {
        templateUrl: "itemList.htm",
        controller: 'ListCtrl',
        resolve: {
            data: function () {
                console.log("/////////////2");
            }
        }
    })
    .when("/getCurrent/:currentId", {
        templateUrl: "currentItem.htm",
        controller: 'ItemCtrl',
        resolve: {
            data: function () {
                console.log("/////////////3");
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
app.controller('BucketCtrl', ['$scope', 'CacheFactory', BucketCtrl]);
app.service('NamesService', NamesService);
app.service('AjaxService', AjaxService);
app.controller('ListCtrl', ['$scope','$routeParams', 'NamesService', 'AjaxService', ListCtrl]);
app.controller('ItemCtrl', ['$scope','$routeParams', 'NamesService', 'AjaxService', ItemCtrl]);
app.config(['$routeProvider', Route]);
