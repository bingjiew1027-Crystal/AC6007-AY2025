# Flask

from flask import Flask,render template, request

app = Flask(_name_)

@app.route("/",methods=["GET","POST"])
 def index():
return(render template("index.html"))

if_name_== "_main_ ":
  app.run()
