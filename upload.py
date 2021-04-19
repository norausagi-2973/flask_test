import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from datetime import datetime
from app import canny
app = Flask(__name__)

UPLOAD_FOLDER = './target'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        img_file = request.files['img_file']
        if img_file and allowed_file(img_file.filename):
            dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_")
            filename = dt_now + ".jpg"
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = '/uploads/' + filename

            img = canny(filename)
            
            return render_template('index.html', img_url=img_url,img = img)
        else:
            return ''' <p>許可されていない拡張子です</p> '''
    else:
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.debug = True
    app.run()