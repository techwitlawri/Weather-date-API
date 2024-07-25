from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")



@app.route("/")
def home():
    return  render_template("home.html")

@app.route("/api/v1/<station>/<date>")
# v1 means version 1
# zfill means zero fill, meaning
# if you do zfill(6) it means(00010)
def about(station, date):
    filename= 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=[ '    DATE'], sep=",", engine="python", skipfooter=1)
    temperature= df.loc[df[ '    DATE']== date]['   TG'].squeeze() /10
    
    # return  render_template("about.html")

    return {"station" : station,
           "date": date,
           "temperature": temperature}

if __name__=="__main__":
    app.run(debug= True, port = 5001)