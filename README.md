Install `virtualenv`. Go to project directory and create a new virtual environment:
```
$ virtualenv --python=python3 virtual
```

Source the virtual environment by running:
```
$ source virtual/bin/activate
```

Update the virtual environment with required packages:
```
$ pip install --requirement requirements.txt
```

Install latest [geckodriver from Mozilla](https://github.com/mozilla/geckodriver/releases). Make sure it is in your `PATH`.
