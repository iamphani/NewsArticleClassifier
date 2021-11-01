from datetime import datetime
from flask import Flask, render_template,request,redirect # For flask implementation
from send_data import searchnews


app = Flask(__name__)
heading = "Data Ingestion Service"
title = "Data Ingestion Service"

 #home page
@app.route("/")    
def render():
	#Display the all Tasks	
	todosnew_l={"Category":""}
	a1="active"
	return render_template('index.html',a1=a1,todos_new=todosnew_l,t=title,h=heading)

#Handle the Classify button action
@app.route("/action", methods=['POST'])
def action ():
  a1="active"
  searchstring=str(request.values.get("search"))
  searchnews(searchstring)
  todosnew_l={'Category':'Data Ingestion Service completed successfully.'} 
  return render_template('index.html',a1=a1,todos_new=todosnew_l,t=title,h=heading)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
