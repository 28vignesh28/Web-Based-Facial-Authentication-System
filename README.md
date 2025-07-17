# 👋 Web-Based Facial Authentication System

A **web-based facial authentication system** that allows users to securely register and log in using their face as a biometric credential. Designed for simplicity and clarity, this project is ideal for solo developers or interns building a secure end-to-end facial login system.

---

## ✨ Features

- **🔐 Face-Based Registration**  
  Users can create an account by providing a username and email, then capture their facial image using a webcam. The facial embedding is generated and stored securely in PostgreSQL.

- **👁️‍🗨️ Face-Based Login**  
  Authenticates users by comparing a live facial embedding with stored records. A successful match grants access.

- **🫣 Liveness Detection (Eye Blink)**  
  Prevents spoofing with static images by verifying natural eye-blink activity during login.

- **📊 Personalized Dashboard**  
  After login, users are welcomed on a dashboard personalized with their username.

- **🔓 Logout**  
  Users can securely end their session.

---

## ⚠️ Security Notice

> This prototype **stores facial embeddings in plain serialized form**, which is **not safe for production**.  
In a real-world system, use **homomorphic encryption** or secure enclaves for privacy-preserving biometric storage and comparison.

This project is meant for **educational purposes** only.

---

## 🚀 Tech Stack

### Backend (Python)

- **Flask** – Micro web framework  
- **Flask-SQLAlchemy** – ORM for PostgreSQL  
- **psycopg2-binary** – PostgreSQL driver  
- **face_recognition** – High-level face embedding and detection  
- **opencv-python** – Camera feed and frame analysis  
- **Flask-Migrate** – Database schema migration  
- **gunicorn** – WSGI server for deployment  

### Frontend (HTML/CSS/JavaScript)

- **HTML5** – Forms and layout  
- **CSS3** – UI styling  
- **JavaScript (Vanilla)** – Webcam handling, image capture, and fetch API

### Database

- **PostgreSQL** – Stores user profiles and facial embeddings  

---

## 🛠️ Getting Started

### ✅ Prerequisites

- Python 3.x  
- Git  
- PostgreSQL (installed and running)

---

### 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/28vignesh28/your-repo-name.git
   cd facial-auth-project
