# rpi-sprinkler-control


# Install

## Packaging
```python
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
```

##



# Usages

Get state of each valve
 
```python
python zone_control.py get
```
 
Get state of specific zone
 
```python
python zone_control.py get --zone 1
```
 
 Set state of specific valve
 
```python
python zone_control.py set --zone 1 --state 1
```
 
 Set state of each valve
 
```python
python zone_control.py set --state 1
```
 
 Toggle state of specific valve
 
```python
python zone_control.py toggle --zone 1
```