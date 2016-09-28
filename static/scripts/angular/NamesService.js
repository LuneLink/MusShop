/**
 * Created by wookie on 9/28/16.
 */

function NamesService() {

    this.getPicture = function (man, model) {
        return "images/" + man + "_" + model + ".png";
    };

    this.getFullName = function (man, model) {
        return man + " " + model;
    }
}
