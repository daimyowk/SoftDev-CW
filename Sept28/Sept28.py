from flask import Flask, render_template

app = Flask (__name__)

#get request
#post request - sending data to server. sends more info than get
@app.route("/login", methods=["GET","POST"])
def login():
    import util
    if request.method="GET":
        return render_template("login.html")
    else:
        button=request.form['button']
        uname=request.form['username']
        pword=request.form['password']
        if button="cancel":
            return render_template("login.html")
        # if here should have user name and password
        print request.form
        return "YOU HIT POST"

@app.route("/")
def index():
    #print request
    #print "SEPERATOR"
    #print request.args
    return render_template("index.html", args= request.args)

    if __name__ == "__main__":
        app.debug=True
        app.run(host='0.0.0.0', port=800)
