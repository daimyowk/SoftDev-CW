var thluffy = document.querySelector("#thluffy");
//give any css selector but slow
/*
window.addEventListener('mousemove',function(e){
    if(e.pageX>200){
	thluffy.src(
    } else{
});
*/

var doStuff = function doStuff(){
    console.log("stuff has been done");
    //setTimeout(doStuff,5000); good if want do something once
};

var myInterval  = setInterval(doStuff,5000);
document.querySelector("#stop").addEventListener('click',function(e){
    clearInterval(myInterval);
});

//full to do list. have a highlight button. change something. everytime
//click button, revert previous then do the next thing to next

//start stop
// start every sec do the thing. then stop
