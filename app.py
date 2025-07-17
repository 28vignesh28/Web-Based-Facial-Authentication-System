import base64
import cv2
import numpy as np
import face_recognition
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:152328@localhost:5432/face_auth_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-super-secret-key' 

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    face_encoding = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


def get_face_encoding(image_data):
    """Decodes image data and returns the first face encoding found."""
    try:
        
        img_data = base64.b64decode(image_data.split(',')[1])
        nparr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        
        face_locations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
        
        if face_encodings:
            return face_encodings[0] 
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', username=user.username)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    image_data = data.get('image')

    if not username or not image_data:
        return jsonify({'status': 'error', 'message': 'Missing username or image'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'status': 'error', 'message': 'Username already exists'}), 409
    
    encoding = get_face_encoding(image_data)
    
    if encoding is None:
        return jsonify({'status': 'error', 'message': 'No face detected or error in processing image'}), 400

    new_user = User(username=username, face_encoding=encoding.tobytes())
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'status': 'success', 'message': 'User registered successfully'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    image_data = data.get('image')

    if not image_data:
        return jsonify({'status': 'error', 'message': 'No image provided'}), 400

    login_encoding = get_face_encoding(image_data)

    if login_encoding is None:
        return jsonify({'status': 'error', 'message': 'No face detected in the provided image'}), 400

    users = User.query.all()
    for user in users:
        stored_encoding = np.frombuffer(user.face_encoding, dtype=np.float64)
        
        
        matches = face_recognition.compare_faces([stored_encoding], login_encoding, tolerance=0.6)
        
        if True in matches:
            session['user_id'] = user.id 
            return jsonify({'status': 'success', 'message': f'Login successful for {user.username}', 'redirect': url_for('dashboard')})
    
    return jsonify({'status': 'error', 'message': 'Authentication failed. Face not recognized.'}), 401

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True, ssl_context='adhoc') 