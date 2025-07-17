# 👋 Web-Based Facial Authentication System

A web-based facial authentication system that allows users to securely register and log in using their face as a biometric credential. Designed as a complete end-to-end solution, this project is ideal for solo developers and interns seeking to explore real-world biometric authentication workflows.

## ✨ Key Features

### 🔐 Face-Based User Registration
New users can register by providing a username and email, then capturing their facial image via webcam. This image is processed into a unique facial embedding and securely stored in a PostgreSQL database alongside the user profile.

### 👁️‍🗨️ Facial Login Authentication
Registered users can log in simply by looking into their webcam. The system captures a live image, generates a new embedding, and compares it with stored profiles. Upon a successful match, the user is authenticated.

### 🫣 Basic Liveness Detection (Eye Blink)
To prevent spoofing attacks using photos or videos, the system detects natural eye blinks during login. Authentication continues only if a genuine blink is detected, ensuring the face is live.

### 📊 Personalized Dashboard
After a successful login, users are redirected to a dashboard personalized with their username and profile information.

### 🔓 Logout Functionality
A simple logout option allows users to terminate their session securely.

## ⚠️ Prototype Security Note

> [!WARNING]
> **Important:** This system stores facial embeddings in a basic serialized format, which is **insecure for production**.
>
> In a production-grade system, advanced techniques like **Homomorphic Encryption** are essential for privacy-preserving biometric comparisons.
>
> This prototype serves as an educational implementation and highlights both the functional workflow and key security considerations.

## 🚀 Technology Stack

A Python-first full-stack approach optimized for solo development and seamless Machine Learning integration.

### 🧠 Backend (Python)
- **Flask** – Lightweight, minimalistic web framework.
- **Flask-SQLAlchemy** – ORM for database interactions using Python objects.
- **psycopg2-binary** – PostgreSQL adapter for Python.
- **face_recognition** – High-level API for face detection and embeddings (based on `dlib`).
- **opencv-python** – Video capture and image processing (used for webcam feed and blink detection).
- **Flask-Migrate** – Database migrations for version-controlled schema updates.
- **gunicorn** – Production-ready WSGI server for deployment.

### 🌐 Frontend (HTML/CSS/JS)
- **HTML5** – Structures the pages and forms.
- **CSS3** – Styles the UI for a clean and responsive design.
- **Vanilla JavaScript** – Handles:
  - Webcam access (`navigator.mediaDevices.getUserMedia`)
  - Capturing image frames with `<canvas>`
  - Async API calls to Flask using the `fetch` API

### 🗄️ Database
- **PostgreSQL** – Reliable, open-source RDBMS. Chosen for its robustness and support for complex data types (e.g., JSON-serialized facial embeddings).

## 🛠️ Getting Started

### ✅ Prerequisites
- Python 3.x
- Git
- PostgreSQL (installed and running)

### ⚙️ Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/28vignesh28/your-repo-name.git](https://github.com/28vignesh28/your-repo-name.git)
    cd facial-auth-project
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    python3 -m venv venv
    ```
    *On macOS/Linux:*
    ```bash
    source venv/bin/activate
    ```
    *On Windows:*
    ```bash
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    > [!NOTE]
    > If you face issues with the `face_recognition` models, try running this command before installing from `requirements.txt`:
    > `pip install wheel setuptools pip --upgrade` 
      and `pip install git+https://github.com/ageitgey/face_recognition_models --verbose`

### 🧾 Database Setup

1.  **Create PostgreSQL Database and User**
    Open your PostgreSQL CLI or pgAdmin and run:
    ```sql
    CREATE DATABASE facial_auth_db;

    -- If needed:
    -- CREATE USER postgres WITH PASSWORD '111111';
    -- GRANT ALL PRIVILEGES ON DATABASE facial_auth_db TO postgres;
    ```

2.  **Configure Database URI**
    Make sure your `config.py` contains the correct database URI:
    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:111111@localhost/facial_auth_db'

    #use your database and it's credentials
    ```

3.  **Initialize and Migrate Database**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

### ▶️ Running the Application

1.  **Start the Flask Server**
    Once everything is installed and configured, run:
    ```bash
    python run.py
    ```

2.  **Access the Application**
    Open your browser and navigate to:
    [http://localhost:5000](http://localhost:5000)

You can now register and log in using facial recognition!

## 📌 Final Notes

This project serves as a starting point for developers interested in building secure, biometric-based authentication systems. For a production-level implementation, consider:
- Encrypted storage of embeddings
- Multi-factor authentication
- Improved spoof detection (3D liveness, infrared, etc.)
