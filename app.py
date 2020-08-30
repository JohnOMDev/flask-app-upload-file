""" The small flask app for uploading files """
import os
from flask import Flask, render_template, request
import requests
from werkzeug.utils import secure_filename

app = Flask(__name__)
#API
app.config["api"] = "https://patw1h5276.execute-api.eu-west-1.amazonaws.com/beta/upload/"
 #File extension
ALLOWED_EXTS = {"txt","csv","dat","XLS","XLSX","doc","docx","pdf","ppt"}

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

# """custom function to raise exception for file extension """
def check_file(file):
    return '.' in file and file.rsplit('.',1)[1].lower() in ALLOWED_EXTS

# """Main app for viewing the index page, uploading the file and posting it"""
@app.route("/index", methods=["POST","GET"])

def index():
    error = None
    filename = None
# Creating post request
    if request.method == "POST":
# Creating exception and error we might encounter
        if "file" not in request.files:
            error ="File not selected"
            return render_template ("index.html", error=error)

        file = request.files["file"]

        filename = secure_filename(file.filename)
        if filename == "":
            error = "Please select a file before attempting submitting"
            return render_template('index.html', error = error)

        if check_file(filename) == False:
            error = "This file extension is not allowed"
            return render_template('index.html', error = error)
        else:
# The request that post the payload after appending the api and the filename
            requests.post(os.path.join(app.config["api"],filename),file)

    return render_template("index.html", filename = filename)

# """error handler for the http requests"""
@app.errorhandler(413)
# pylint: disable=unused-argument
def payload_large(error):
    return render_template("413.html"),413

@app.errorhandler(404)
#   pylint: disable=unused-argument
def page_not_found(error):
    return render_template("404.html"),404

@app.errorhandler(500)
#   pylint: disable=unused-argument
def server_error(error):
    return render_template("500.html"),500

@app.errorhandler(403)
#   pylint: disable=unused-argument
def forbidden(error):
    return render_template("403.html"),403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug= True)
