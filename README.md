🚀 Hackathon Finalist Project  

# 🔐 AI-Powered Multi-Factor Authentication System

An intelligent, secure, and scalable authentication system that combines **biometrics, device fingerprinting, and AI-based anomaly detection** to enhance modern authentication beyond traditional passwords and OTPs.

---

## 📌 Overview

Traditional authentication methods are vulnerable to attacks like phishing, brute force, and credential stuffing.  
This project introduces a **multi-layered authentication system** that uses AI/ML to improve both **security and user experience**.

---

## ✨ Key Features

### 🔹 Multi-Factor Authentication
- PIN-based authentication  
- Biometric face verification  
- Device fingerprinting  

### 🔹 Face Recognition & Liveness Detection
- Deep learning-based identity verification  
- Detects spoofing (photos/videos)  

### 🔹 Device Fingerprinting
- Identifies unique devices using system metadata  
- Detects suspicious login attempts  

### 🔹 AI-Based Anomaly Detection
- Tracks login patterns (IP, device, behavior)  
- Blocks suspicious activity after multiple failed attempts  

### 🔹 Secure Email Verification
- Sends OTP/code via Flask-Mail  

---

## 🧠 Tech Stack

**Backend:** Python (Flask)  

**AI/ML:** DeepFace, TensorFlow/Keras, MTCNN, dlib, face_recognition  

**Computer Vision:** OpenCV, MediaPipe  

**Database:** PostgreSQL (psycopg2)  

**Other:** Docker, Device Fingerprinting (custom module)  

---

## 🏗️ Project Structure
multi-factor-authentication-system/
├── src/ # Core logic
├── database/ # DB operations
├── models/ # ML models
├── templates/ # HTML files
├── static/ # CSS & JS
├── main.py # Flask app
├── config.py
├── requirements.txt

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sarasakeena/multi-factor-authentication-system.git
cd multi-factor-authentication-system

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Create .env File
FLASK_SECRET_KEY=your_secret_key

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password

5. Run the App
python main.py

6. Open in Browser
http://127.0.0.1:5000/

🔐 Authentication Flow

User registers with face + PIN

Device fingerprint is stored

Login includes:

Face verification + liveness detection

Device validation

Risk analysis

Suspicious attempts → blocked

🚀 Future Improvements

Cloud deployment (AWS / GCP)

JWT-based authentication

Advanced ML-based anomaly detection

Mobile app integration

📌 Note

Sensitive data (.env, user images) are excluded

Developed as a hackathon finalist project

👩‍💻 Author

Sara Sakeena
GitHub: https://github.com/sarasakeena

⭐ Support

If you like this project, give it a ⭐!
