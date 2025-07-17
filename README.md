<h1 align="center">Welcome to Web-Based-Facial-Authentication-System 👋</h1>
<p>
</p>

> This project is a **web-based facial authentication system**. It allows users to register and log in to a web application using their face as a credential.### FunctionalityThe application has the following key features:* **User Registration**: New users can create an account by providing a username and allowing the application to capture an image of their face from their webcam. The system then processes this image to create a facial encoding, which is stored in a database along with the username.* **User Login**: To log in, a registered user simply needs to look into their webcam and click the &#34;Login with Face&#34; button. The application captures their image, generates a facial encoding, and compares it with the stored encodings in the database. If a match is found, the user is authenticated and redirected to their dashboard.* **Dashboard**: After successful authentication, the user is taken to a personal dashboard page that welcomes them by their username.* **Logout**: The application also provides a logout functionality that clears the user's session.### Technologies UsedThe project is built using a combination of Python for the backend and standard web technologies for the frontend.* **Backend**: The backend is a **Flask** application. It uses **Flask-SQLAlchemy** to interact with a **PostgreSQL** database where user data and facial encodings are stored. The core facial recognition functionality is implemented using the **`face_recognition`** and **`opencv-python-headless`** libraries.* **Frontend**: The user interface is created with **HTML**, **CSS**, and **JavaScript**. The JavaScript code handles capturing video from the user's webcam, taking a picture, and sending it to the backend for processing during registration and login.

## Install

```sh
pip install -r requirements.txt
```

## Run tests

```sh
python app.py
```

## Author

👤 **Vignesh Ganisetty**

* Github: [@28vignesh28](https://github.com/28vignesh28)
* LinkedIn: [@vignesh ganisetty](https://linkedin.com/in/vignesh ganisetty)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_