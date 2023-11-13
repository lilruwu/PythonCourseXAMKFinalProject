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

 - [Blender 3.6](https://docs.blender.org/api/current/)
 - [Python 3.10.12](https://docs.python.org/release/3.10.12/)
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
We are going to do two different approaches:

## Option 1:
>Create a python script for Blender that reads the map height data from the file ***M5221.asc*** and creates a simple height visualization of a part of the information.
#### For reading we can use this simple Python code:  
   

We open the file:
```python
with open('PATH\\M5221.asc', 'r') as file:
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
We adjust the minimum height at the minimum height in the data set for improve the representation:
```python
min_height = min(height_data)
```
Now we adjust the *voxels* size:
```python
voxel_size = cellsize
```
And we create the map using two *for* loops:
```python
for y in range(nrows):
    for x in range(ncols):
        z = height_data[y * ncols + x] - min_height # We use this formula for improve the map representation.
        
        bpy.ops.mesh.primitive_cube_add(size=voxel_size, enter_editmode=False, location=(x * voxel_size, y * voxel_size, z))
        cubo = bpy.context.object
        cubo.scale[2] = z
```
And we can save the Blender file if we want:
```python
bpy.ops.wm.save_as_mainfile(filepath="path_to_save.blend")
```

### This is the complete code and result:

#### Code
```python
import bpy

with open('PATH\\M5221.asc', 'r') as file:
    lines = file.readlines()

ncols = 30
nrows = 30
xllcorner = float(lines[2].split()[1])
yllcorner = float(lines[3].split()[1])
cellsize = float(lines[4].split()[1])
nodata_value = float(lines[5].split()[1])

height_data = []
for line in lines[6:6+nrows]:
    height_data.extend([float(value) for value in line.split()[:ncols]])

min_height = min(height_data)

voxel_size = cellsize

for y in range(nrows):
    for x in range(ncols):
        z = height_data[y * ncols + x] - min_height
        
        bpy.ops.mesh.primitive_cube_add(size=voxel_size, enter_editmode=False, location=(x * voxel_size, y * voxel_size, z))
        cubo = bpy.context.object
        cubo.scale[2] = z

# Uncomment to save the file
#bpy.ops.wm.save_as_mainfile(filepath="path_to_save.blend")
```

#### Result
![Image could not be loaded](./Option1Result.png)

## Option 2:
>Create a more advanced version of the blender script. Whole area covered in the file cannot be rendered by planes in a way that I have done in the first exercise example. Figure out how to render a larger area. Blender can manage a huge amount of vertexes. This 3d object in next screenshot for example contains 1 002 001 vertexes.

>Add also a menu component that can be used to define the rendered area. User can for example define north/west and south/east coordinates. 

#### For reading we can use this simple Python code:  
   

We open the file:
```python
with open('PATH\\M5221.asc', 'r') as file:
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
We create a new mesh and object in Blender:
```python
mesh = bpy.data.meshes.new(name="3DMapMesh")
obj = bpy.data.objects.new(name="3DMapObject", object_data=mesh)
```
We link the object to the current collection:
```python
bpy.context.collection.objects.link(obj)
```
We set it as the active object and we select it:
```python
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
```
We scale the object in the z axis for improve the map view:
```python
obj.scale = (1, 1, 5)
```
We generatee vertices and faces for a 3D mesh from height data:
```python
vertices = [(x * cellsize, y * cellsize, z - min(height_data)) for y in range(nrows) for x in range(ncols) for z in [height_data[y * ncols + x]]]
faces = [(i, i+1, i+ncols+2, i+ncols+1) for i in range(0, len(vertices)-ncols-1) if (i+1) % ncols != 0]
```
We createe a mesh object from a set of vertices and faces and we update it:
```python
mesh.from_pydata(vertices, [], faces)
mesh.update()
```
