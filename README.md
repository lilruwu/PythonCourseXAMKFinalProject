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
We have three approaches:

## Option 1:
>Create a python script for Blender that reads the map height data from the file ***M5221.asc*** and creates a simple height visualization of a part of the information.
#### For reading we can use this simple Python code:  
   

We open the file:
```python
with open('M5221.asc', 'r') as file:
    lines = file.readlines()
```
Now we take the columns and rows we want changing them in the script (let's use 30 as example):
```python
ncols = 30 # Can be change
nrows = 30 # Can be change
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
At the end of the *for loop* we have the variable *height_data* with all the coordinates.

#### Now for the representation in Blender we can use this code:
  
Import the Blender library in python:
```python
import bpy
```
We create a new mesh object and we link it to the Blender' scene:
```python
mesh = bpy.data.meshes.new(name="HeightMapMesh")
obj = bpy.data.objects.new(name="HeightMapObject", object_data=mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
```
Now we create vertices and faces based on *ncols* and *nrows*
```python
vertices = [(x, y, z) for y in range(nrows) for x in range(ncols) for z in [height_data[y * ncols + x]]]
faces = [(i, i+1, i+ncols+1, i+ncols) for i in range(0, len(vertices)-ncols-1, ncols)]
```
And we create a mesh from them:
```python
mesh.from_pydata(vertices, [], faces)
mesh.update()
```
Optionally we can adjust scale and position:
```python
obj.scale = (cellsize, cellsize, cellsize) 
obj.location = (xllcorner, yllcorner, 0)   
```
And we can save the Blender file:
```python
bpy.ops.wm.save_as_mainfile(filepath="path_to_save.blend")
```

## Option 2:
>Create a more advanced version of the blender script. Whole area covered in the file cannot be rendered by planes in a way that I have done in the first exercise example. Figure out how to render a larger area. Blender can manage a huge amount of vertexes. This 3d object in next screenshot for example contains 1 002 001 vertexes.

>Add also a menu component that can be used to define the rendered area. User can for example define north/west and south/east coordinates. 


## Option 3:
>Create a script that renders height profile from one coordinate to another. There needs to be a menu where the coordinates are inserted. Addition to the profile, there also need to be start coordinates and height, end coordinates and height, highest coordinates and height, lowest coordinates and height in the image. 
