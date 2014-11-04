var casper = require('casper').create();
var fs=require('fs');
var utils = require('utils');
casper.start('http://24h.pchome.com.tw/prod/DGAZ5T-19005EITY');
casper.waitFor(
function check() {
    return this.evaluate(function() {
        return document.querySelectorAll('#PriceTotal').length > 0;
    });
},
function then() {
  casper.each(this.getElementsInfo('#PriceTotal'), function(casper, element, j) {
    console.log(element['html'])
  });
});
casper.run();