from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image

app = Flask(__name__)

if not os.path.exists('UserProfilePics'):
    os.makedirs('UserProfilePics')


@app.route('/')
def home():
    return render_template('addProfilePic.html')


@app.route('/upload_profile_pic', methods=['POST'])
def upload_profile_pic():
    file = request.files['profile-pic-input']
    filename = secure_filename(file.filename)
    file_path = os.path.join('UserProfilePics', filename)
    
    img = Image.open(file)
    img = img.resize((500, 500))
    img.save(file_path)
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Profile picture uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)

