# Python App

## Creat Virtual Environment

```
python3 -m venv .venv
```

```.venv``` is the name of the virtual environment.
You will see a folder created with the name .venv


## Checking the python interpreter source

```
which python3
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
```
> For windows you will have to use "where" instead of "which"


## Activate the virtual environment

### For Unix based systems

```
source .venv/bin/activate
```

### For Windows based systems

```
.venv\Scripts\activate
```

## Checking the python interpreter source after activating the virtual environment

```
which python3
/Users/Manu/Desktop/New/python_app/.venv/bin/python3
```
> For windows you will have to use "where" instead of "which"

## Deactivate virtual environment

```
deactivate
```

## Installing numpy in virtual environment

```
source .venv/bin/activate
```

```
pip install numpy
```

## Installing Jupyter and Ipykernel

```
pip install ipykernel jupyter
```

## Open Jupyter Notebook

```
jupyter notebook
```