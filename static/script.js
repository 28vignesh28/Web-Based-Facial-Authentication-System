document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const registerButton = document.getElementById('register-button');
    const loginButton = document.getElementById('login-button');
    const usernameInput = document.getElementById('username');
    const feedbackDiv = document.getElementById('feedback');

  
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
                video.play();
            })
            .catch(err => {
                console.error("Error accessing webcam: ", err);
                feedbackDiv.textContent = "Could not access webcam. Please allow camera access.";
                feedbackDiv.className = 'error';
            });
    }

    function captureImage() {
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        return canvas.toDataURL('image/jpeg');
    }

    function showFeedback(message, type) {
        feedbackDiv.textContent = message;
        feedbackDiv.className = type;
    }

   
    if (registerButton) {
        registerButton.addEventListener('click', async () => {
            const username = usernameInput.value;
            if (!username) {
                showFeedback('Please enter a username.', 'error');
                return;
            }
            
            showFeedback('Processing...', '');
            const imageData = captureImage();

            try {
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, image: imageData }),
                });

                const result = await response.json();
                if (response.ok) {
                    showFeedback(result.message, 'success');
                    setTimeout(() => window.location.href = '/', 2000); 
                } else {
                    showFeedback(result.message, 'error');
                }
            } catch (error) {
                showFeedback('An error occurred. Please try again.', 'error');
            }
        });
    }

    
    if (loginButton) {
        loginButton.addEventListener('click', async () => {
            showFeedback('Authenticating...', '');
            const imageData = captureImage();
            
            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ image: imageData }),
                });

                const result = await response.json();
                if (response.ok) {
                    showFeedback(result.message, 'success');
                    window.location.href = result.redirect; 
                } else {
                    showFeedback(result.message, 'error');
                }
            } catch (error) {
                showFeedback('An error occurred. Please try again.', 'error');
            }
        });
    }
});