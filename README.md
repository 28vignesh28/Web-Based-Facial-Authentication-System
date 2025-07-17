# Web-Based Facial Authentication System 👋

This project implements a **web-based facial authentication system** designed to allow users to securely register and log in using their face as a primary credential. Built with a focus on simplicity for a solo developer internship, it showcases a complete end-to-end user journey for biometric authentication.

## ✨ Key Features

* **User Registration with Face**: New users can create an account by providing a username and email, and then capturing their facial image via webcam. [cite_start]This image is processed to generate a unique facial embedding, which is securely stored in a PostgreSQL database alongside their user profile. [cite: 555]
* **User Login with Face**: Registered users can log in by simply looking into their webcam. The application captures their live image, generates a new facial embedding, and compares it against stored profiles. [cite_start]Upon a successful match, the user is authenticated. [cite: 557, 756]
* **Basic Liveness Detection (Eye-Blink)**: To enhance security against simple spoofing attacks (e.g., holding up a photo), the system incorporates eye-blink detection during the login process. [cite_start]Authentication proceeds only if a genuine blink is detected, ensuring the presented face is from a live person. [cite: 902, 924, 994]
* [cite_start]**Personalized Dashboard**: After successful authentication, users are redirected to a personalized dashboard, welcoming them by their registered username. [cite: 993]
* **Logout Functionality**: Provides a simple way to clear the user's session and log out of the application.

### ⚠️ Important Security Note (Prototype)

It is crucial to understand that this prototype stores facial embeddings in a simply serialized format for simplicity and educational purposes. [cite_start]**This approach is fundamentally insecure for production environments.** [cite: 774] [cite_start]In a real-world application, advanced cryptographic techniques like Homomorphic Encryption would be required to perform comparisons on encrypted biometric data, ensuring maximum security and privacy. [cite: 781, 999] [cite_start]This project serves as a foundational learning experience, highlighting both functional implementation and critical security considerations. [cite: 787]

## 🚀 Technology Stack

[cite_start]This project leverages a unified Python-based full-stack approach, optimizing for Machine Learning (ML) integration and ease of development for a solo developer. [cite: 571, 575]

* **Backend (Python)**:
    * [cite_start]**Flask**: A lightweight and flexible micro-framework, ideal for smaller projects and APIs due to its simplicity and minimal boilerplate. [cite: 581, 582]
    * [cite_start]**Flask-SQLAlchemy**: An Object-Relational Mapper (ORM) that simplifies database interactions by allowing manipulation of database records using Python objects. [cite: 603, 677]
    * [cite_start]**psycopg2-binary**: The PostgreSQL adapter for Python, enabling the Flask application to connect and interact with the database. [cite: 603]
    * [cite_start]**face_recognition**: A high-level library built on `dlib` for straightforward face detection, landmark identification, and generating/comparing 128-dimensional facial embeddings with high accuracy. [cite: 596, 597, 751]
    * **opencv-python**: Essential for fundamental computer vision tasks such as decoding image data from the frontend, handling video streams, and basic image manipulations required for liveness detection. [cite: 599, 916]
    * **Flask-Migrate**: Used for handling database schema migrations, allowing for version control of your database structure.
    * **gunicorn**: A Python WSGI HTTP Server for UNIX, specified for production deployment on platforms like Heroku. 

* **Frontend (Standard Web Technologies)**:
    * **HTML**: Structures the web pages for user interaction. [cite: 586]
    * [cite_start]**CSS**: Styles the user interface for a clean and uncluttered layout. [cite: 586, 829]
    * [cite_start]**JavaScript (Vanilla)**: Handles client-side logic including webcam access (using `navigator.mediaDevices.getUserMedia`), capturing still frames (with `<canvas>`), and asynchronous communication with the Flask backend (using the `fetch` API). [cite: 587, 606, 607, 831, 863]

* **Database**:
    * **PostgreSQL**: A powerful, open-source, and highly reliable relational database. [cite_start]Chosen for its robustness and ability to store complex data types (like JSON-serialized facial embeddings). [cite: 588, 590]

## 🛠️ Getting Started

Follow these steps to get your development environment set up and run the application locally.

### Prerequisites

* Python 3.x
* Git
* PostgreSQL installed and running on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/28vignesh28/your-repo-name.git](https://github.com/28vignesh28/your-repo-name.git) # Replace with your actual repo name
    cd facial-auth-project
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This command should handle `dlib`, `face_recognition`, `opencv-python`, and others. If you face issues with `face_recognition` models specifically, try `pip install git+https://github.com/ageitgey/face_recognition_models` before retrying `python run.py`.*

### Database Setup

1.  **Create your PostgreSQL database:**
    You need to manually create a PostgreSQL database. For example, if you use the default URI in `config.py`, create a database named `facial_auth_db` and a user `postgres` with password `152328` (or configure your `SQLALCHEMY_DATABASE_URI` in `config.py` accordingly).
    ```sql
    -- Example SQL to create database (if not already done via pgAdmin/CLI)
    CREATE DATABASE facial_auth_db;
    -- CREATE USER postgres WITH PASSWORD '111111'; -- Only if user doesn't exist
    -- GRANT ALL PRIVILEGES ON DATABASE facial_auth_db TO postgres;
    ```
2.  **Initialize and run database migrations:**
    With your virtual environment active and in the `facial-auth-project` root directory:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

### Running the Application

After installing dependencies and setting up the database, you can run the Flask application:

```bash
python run.py
