var x = 20;
var l = {1,2,3,4,5}

var d = {'one':1,
         2:"hello"};

console.log("javascrip loaded");

function f(p){
    x = 30; // without var: makes its global
    console.log("in fnction f: "+p+x);
}

var fact = function fact(n){
    var prod = 1;
    for ( ; n>1 ; n--){
	prod = prod * n;
	}
    return prod;
};
//flymate and flycheck for code check
//document is the html. allows interact with webpage
//many functions to get stuff out of html eg. doucment.getElementByID("div1")

var addItem  = fuction  addItem(s){
    var l = document.getElementById("thelist");
    var n = document.createElement("li");
    n.innerHTML=s;
    l.appendCHild(n);
};

