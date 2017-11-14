from flask import Flask , request , \
send_from_directory , url_for , render_template , redirect  , g

from werkzeug import secure_filename
import json
from contextlib import closing
import sqlite3

from flask_cors import *

app = Flask(__name__)
CORS(app , supports_credentials=True)
@app.route("/")
def indexFn():
    return "我是index 界面"


    
#home 路由
@app.route("/home")
def homeFn():
    # return render_template("index.html")
    return "我是home界面"




@app.errorhandler(404)
def lostPage(err):
    # return render_template("lostPage.html")
    # return redirect(url_for("indexFn"))
    return "我是404界面"



if __name__ == "__main__":
    app.run(host='192.168.1.33' , port=5678)



