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