# My Python XAMK Course's Final Project in Blender
**By Rubén Castro González**  
  
**Objective:** In this project the objective is to represent the height data of Finland in Blender using a Python script.
## The requirements for this assignment are:

 - Developed Python script works in blender and uses blender python library.

 - Script reads the file.

 - Information is parsed from the file.

 - Code is documented.

 - There are no errors that prevent execution in the code.

 - Possible exceptions are handled.

 - Visualization is done by using blender python library and 3D space.

 - Be ready to explain your code and solution if asked.

## Tools that I am going to use:

 - Blender 3.6
 - Python 3.10.12
 - Visual Studio Code
 - Git
 - GitHub
 - WSL with Ubuntu

## Process step by step:

We need to read a file like this one:

```
ncols        2400
nrows        1200
xllcorner    500000.000000000000
yllcorner    6834000.000000000000
cellsize     10.000000000000
NODATA_value  -9999.000

118.358 119.714 120.488 120.506 120.702 120.045 119.613 118.901 118.957 119.211 119.862 119.972 119.401  
118.595  116.338 115.550 114.283 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190  
114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190  
114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190 114.190    
```

For reading we can use this simple Python code:  
   

We open the file:
```python
with open('M5221.asc', 'r') as file:
    lines = file.readlines()
```
Now we ask the user how many columns and rows they want to read:
```python
ncols = int(input("How many columns do you want to read?"))
nrows = int(input("How many rows do you want to read?"))
```
We take the constraints provided in the .asc file for representing the data in Blender:
```python
xllcorner = float(lines[2].split()[1])
yllcorner = float(lines[3].split()[1])
cellsize = float(lines[4].split()[1])
nodata_value = float(lines[5].split()[1])
```
Now we read the rows and columns the user wanted to read:
```python
height_data = []
for line in lines[6:6+nrows]:
    height_data.extend([float(value) for value in line.split()[:ncols]])
```


