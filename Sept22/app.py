from flask import Flask

app = Flask(__name__)
# flask works with routes
# webpage/hello hello would be route
#/about about would be route on webpage
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/oldabout")
def oldaboutpage():
    #triple quote allow multiple line long strings
    page="""
<h1>About</h1>
<br>
<ol>
<li>About1</li>
<li>About2</li>
<li>About3</li>
</ol>
"""
    return page

@app.route("/lucky")
def lucky_number():
    import random
    r=random.randrange(1,100)
    return "<h1>Lucky Number: %d</h1>" %(r)

@app.route("/home")
@app.route("/")
def home():
    return "<h1> Home Page </h1>"

if __name__ == "__main__":
        app.debug=True
        app.run(host='0.0.0.0', port=8000)
        # 0000 means anyone can use
        # if made 127.0.01 would be local. only you see on your machine
        # when connect machine to network also connect to port
        # python strings with single or double
        
#hw try make something with flask. use a template        
