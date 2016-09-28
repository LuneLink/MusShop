/**
 * Created by wookie on 9/26/16.
 */


function BucketCtrl ($scope, cache) {

    this.bucketState = false;

    this.changeState = function () {
        this.bucketState = !this.bucketState;
    };

    var currentCache = cache.get('bucket');

    if(currentCache) {
        console.log("Hello NNOOOOOTT empty cache");
        console.log(currentCache);
        this.bucket = currentCache;
    }

    //this.test = bucketService.getTest();
    this.test = 'bucketTEst';


    this.addInBucket = function (id, name, cost) {
        var res = false;
        //this.bucket = cache.get('bucket');

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
        //bucketService.setBucket(this.bucket);
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

    // this.removeFromBucket = function (id) {
    //
    // };

}
