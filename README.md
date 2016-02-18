# flask-login
A basic Flask template app that allows users to signup, login and logout. There is no confirmation needed to create a new user account.

# Requirements

```
pip install -r requirements.txt
```

# Setup

First, rename ```config.py.example``` to ```config.py```.

Second, you need to generate a secret key. Run ```python``` followed by:

```
import os
os.urandom(24)
```
Copy the output to SECRET_KEY and WTF_CSRF_SECRET KEY in ```config.py```.

# Usage
You can run the application by using:
```
python run.py
```

Then open a webbrowser and go to http://127.0.0.1:5000
