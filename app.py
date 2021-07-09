import os
from time import time
from vcf_creator.vcf import vcard_generator
from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename, send_file

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ["csv", "CSV"]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def upload_file():
    # Get the uploaded file
    uploaded_file = request.files['file']
    file = secure_filename(uploaded_file.filename)

    # Check if no file is provided
    if file == '':
        abort(400, "No file provided")
    else:
        file_name = file.split(".")[0]
        file_ext = file.split(".")[1]
        # Check the extension of file
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400, "The uploaded file is not a csv file. Try again!")
        else:
            # Create uploads folder
            directory = os.path.join(app.root_path, "uploads")
            if not os.path.exists(directory):
                os.mkdir(directory)
            csv_file = file_name + "_" + str(int(time())) + "." + file_ext
            csv_file_path = os.path.join(app.root_path, "uploads", csv_file)
            uploaded_file.save(csv_file_path)

            # Create processed folder
            directory = os.path.join(app.root_path, "processed")
            if not os.path.exists(directory):
                os.mkdir(directory)
            vcf_file_path = os.path.join(
                app.root_path, "processed", csv_file.split(".")[0] + ".vcf")
            # Write the VCF file
            with open(vcf_file_path, "w") as f:
                res = vcard_generator(csv_file_path)
                if res != -1:
                    f.write(res)
                else:
                    # Remove temp files
                    os.remove(csv_file_path)
                    os.remove(vcf_file_path)
                    abort(400, """Some error occured. Re-submit the CSV making sure:
                                    1. CSV isn't empty
                                    2. The headers are present and format is correct
                                    3. No fields are empty
                                
                                Otherwise contact the developer at animeshsingh38@gmail.com
                    
                    """)
            # Remove temp files
            os.remove(csv_file_path)
            return send_file(vcf_file_path, as_attachment=True, environ=request.environ)


if __name__ == "__main__":
    app.run()
