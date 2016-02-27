console.log("HELLO");

var printresults = function(d){
		console.log(d);
};
//when using multi thread in order to make slow come back first before
//everything else, do a call back and wait for function
//callback hell

var timingTest1 = function(){

		console.log("slow");
		$.get("/getslow",printresults);
		console.log("BACK FROM SLOW");

		console.log("regular");
		$.get("/getstuff",printresults);
		console.log("BACK FROM REGULAR");


		console.log("FAST");
		$.get("/getfast",printresults);
		console.log("BACK FROM FAST");
		
		
};

var stuffdemo = function(){

		console.log("Calling getstuff");

		$.get("/getstuff",function(d){
				console.log("getstuff returned: "+d);
		});


		
		console.log("back from getstuff");

};

var paramtest = function paramtest(){
    $.getJSON("/upcase",{data:'hello'}, function(d){
	console.log(d);
	console.log(d.result);
    });

};
//more efficent if put $("#data") in a var to make sure only once bceause
//jquery very slow

$("#b").click(function(){
    var d = $("#data").val();
    $("#data".val("");
    $.getJSON("/upcase",{data:d},function(d){
	$("#result").text(d.result);
	$("#thelist").append($"<li>"+d.result+"</li>");
    });
});

