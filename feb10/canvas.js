var c = document.getElementById("ftb2maga");
var ctx = c.getContext("2d");


ctx.fillStyle="blue";
ctx.lineWidth="20";
ctx.beginPath();
ctx.moveTo(15,20); //moving the pencil or point to start at
ctx.lineTo(15,120); // should 
ctx.lineTo(115,120);
ctx.lineTo(115,20);
ctx.lineTo(15,20);
ctx.stroke();
ctx.fill(); //fills in only a closed shape. only the inside of the lines. does not include the edges
//ctx.stroke(); //need stroke to see the lines

ctx.moveTo(300,200);
ctx.arc(200,200,100,0,2); //xcor for center, ycor for center, radius, start angle, end angle
// angle in radians and drawn clock-wise
ctx.stroke();
ctx.fill();

ctx.font="30px arial"
ctx.fillText("Hello",400,400);



ctx.closePath();
