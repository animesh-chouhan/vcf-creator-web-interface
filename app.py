import os
from time import time
from vcf_creator.vcf import vcard_generator
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename, send_file

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ["csv"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    file = secure_filename(uploaded_file.filename)
    
    if file != '':
        file_name = file.split(".")[0]
        file_ext = file.split(".")[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400, "The uploaded file is not a csv file. Try again!")
        
        directory = os.path.join(app.root_path, "uploads")
        if not os.path.exists(directory):
            os.makedir(directory)
        csv_file = file_name + "_" +str(int(time())) + "." + file_ext
        csv_file_path = os.path.join(app.root_path, "uploads", csv_file)
        uploaded_file.save(csv_file_path)
    
    directory = os.path.join(app.root_path, "processed")
    if not os.path.exists(directory):
        os.makedir(directory)
    vcf_file = os.path.join(app.root_path, "processed", csv_file.split(".")[0] + ".vcf")
    with open(vcf_file, "w") as f:
        res = vcard_generator(csv_file_path)
        if res != -1:
            f.write(res)
        else:
            abort(400, "Some error occured. Contact the developer.")
    
    return send_file(vcf_file, as_attachment=True, environ=request.environ)

if __name__ == "__main__":
    app.run()