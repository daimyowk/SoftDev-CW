from flask import Flask, render_template

app = Flask (__name__)

#get request
#post request - sending data to server. sends more info than get
@app.route("/")
def index():
    #print request
    #print "SEPERATOR"
    #print request.args
    return render_template("index.html", args= request.args)

    if __name__ == "__main__":
        app.debug=True
        app.run(host='0.0.0.0', port=800)
