#### Description
This project is a second task of the online [course](https://academy.stepik.org/flask)
It's a simple web site for looking for hotels for traveling. Now, it's possible 
to select a departure and see according hotels at this place.

#### Install
1. Create virtualenv and activate it:
    ```shell script
    python3.7 -m venv venv && source ./venv/bin/python3
    ```
2. Install required packages:
   ```shell script
    pip install -r requirements.txt
   ```

#### Running
1. For test running type:
   ```shell script
   python app.py
   ```
2. For running with gunicorn, type:
   ```shell script
   gunicorn -b 0.0.0.0:8080 app:app
   ```
