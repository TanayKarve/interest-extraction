from flask import Flask, send_from_directory,send_file,request, redirect, url_for, render_template
from werkzeug import secure_filename
import os
app = Flask(__name__,
            static_url_path=''
            )

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(".", filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('coco.html', filename = filename)

@app.route('/img/<filename>')
def img(filename):
	print(filename)
	return send_from_directory(os.path.join("."),filename,mimetype="image/gif")

if __name__=="__main__":
	app.run()