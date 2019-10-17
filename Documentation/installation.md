To install the software >

Make sure you have Python 3.6.x or newer installed. 
https://www.python.org/downloads/

Then, download the project source files

After this, open up the console and locate the directory the project is downloaded to
and run the following commands in the root of the project

Linux/mac:

```
python -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Windows:

```
python3 -m venv venv/
venv/Scripts/activate
pip install -r requirements.txt
py app.py
```

The project should start up, and be availiable in your browser in the address [localhost:5050](http://localhost:5000)

