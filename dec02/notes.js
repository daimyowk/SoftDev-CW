var buttonCallback  =function buttonCallback(e){
    console.log(e);
    console.log(this);
    additem('hello')
};

var b2Callback = function b2Callback(e){
    e.preventDefault(); //dont do default action ex dont goto link, only remove
    console.log(e);
    console.log(this);
    removeItem(0);
};

var button = document.getElementById('b');
b.addEventListener('click',buttonCallback);

var b2 = document.getElementById('b2');
b2.addEventListener('click',b2Callback);
//this in javascript kind of like this in java but not exactly
//this refers to a context,object,dic
//dont have to just use button or radio to do stuff
//can use div, anything

var redCallback=function(e){
    this.classList.toggle('red');
};

var thelist = document.getElementById('thelist');
var items = thelist.chdilren;
console.log(items);

for (var i=00; i<items.length; i++){
    items[i].addEventListener('click',redCallBack);
    items[i].addEventListner('mouseover',function(e){
	console.log('in'+this);
	this.classList.toggle('green');
	});
};

//HW make a fake todo list
//area of screen
// text box
//add to list box
//look up how to get text from text entry box
// if click, to do item, move over to right to done box
//if that clcik make do someting
