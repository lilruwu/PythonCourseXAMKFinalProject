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

mesh = bpy.data.meshes.new(name="3DMapMesh")
obj = bpy.data.objects.new(name="3DMapObject", object_data=mesh)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
obj.scale = (1, 1, 5)

vertices = [(x * cellsize, y * cellsize, z - min(height_data)) for y in range(nrows) for x in range(ncols) for z in [height_data[y * ncols + x]]]
faces = [(i, i+1, i+ncols+1, i+ncols) for i in range(0, len(vertices)-ncols-1) if (i+1) % ncols != 0]

mesh.from_pydata(vertices, [], faces)
mesh.update()