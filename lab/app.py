from flask import Flask, render_template, session, redirect, url_for, request

app = Flask (__name__)

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        newuser=request.form["newuser"]
        pword=request.form["newpass"]
        if newuser not in session:
            session[newuser]=pword
    return render_template("home.html")


if __name__=="__main__":
    app.debug=True
    app.secret_key="stuff"
    app.run(host="0.0.0.0", port=8000)
    
