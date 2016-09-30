/**
 * Created by wookie on 9/26/16.
 */


function BucketCtrl ($scope, $location, cache, AjaxService) {

    this.bucketState = false;
    this.searchState = false;

    this.userName = "";
    this.userPhone = "";
    this.userAdress = "";

    this.changeState = function () {
        this.bucketState = !this.bucketState;
    };

    this.changeSearchState = function () {
        this.searchState = !this.searchState;
    };

    var currentCache = cache.get('bucket');

    if(currentCache) {
        this.bucket = currentCache;
    }

    //this.test = bucketService.getTest();
    this.test = 'bucketTEst';


    this.addInBucket = function (id, name, cost) {
        var res = false;

        for(var i = 0; i < this.bucket.length; i++) {
            if(this.bucket[i].id === id) {
                this.bucket[i].count++;
                res = true;
                break;
            }
        }

        if(!res)
            this.bucket.push({'id': id, 'name' : name, 'cost': cost, 'count': 1});

        cache.put('bucket', this.bucket);
    };

    this.removeFromBucket = function (id) {
        for(i = 0; i < this.bucket.length; i++) {
            if(this.bucket[i].id === id) {
                this.bucket.splice(i, 1);
                break;
            }
        }
    };

    this.getBucketCost = function () {
        var result = 0;
        for(i = 0; i < this.bucket.length; i++) {
            result += this.bucket[i].cost*this.bucket[i].count;
        }

        return result;
    };

    this.submitPurchase = function () {
        console.log("SUBMITING");
        console.log(this.bucket);
        var result = AjaxService.makeAjax('/submitPurchase', {'bucket': this.bucket,
                                                                'userName': this.userName,
                                                                'userPhone': this.userPhone,
                                                                'userAdress': this.userAdress});

        result.then(function(response) {
            $scope.content = response.content;
            $location.path("/successPurchase");
        });

    };

}
