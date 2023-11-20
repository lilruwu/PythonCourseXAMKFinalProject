import bpy
import bmesh

def create_map(rows,columns):
    with open('PATH\\M5221.asc', 'r') as file:
        lines = file.readlines()

    ncols = rows
    nrows = columns
    xllcorner = float(lines[2].split()[1])
    yllcorner = float(lines[3].split()[1])
    cellsize = float(lines[4].split()[1])
    #nodata_value = float(lines[5].split()[1])

    height_data = []
    for line in lines[6:6+nrows]:
        height_data.extend([float(value) for value in line.split()[:ncols]])

    bm = bmesh.new()

    vertices = [(x * cellsize, y * cellsize, z - min(height_data)) for y in range(nrows) for x in range(ncols) for z in
                [height_data[y * ncols + x]]]

    bm_verts = [bm.verts.new(v) for v in vertices]
    bm.verts.ensure_lookup_table()

    faces = [(i, i + 1, i + ncols + 1, i + ncols) for i in range(0, len(vertices) - ncols - 1) if (i + 1) % ncols != 0]

    for f in faces:
        bm.faces.new([bm_verts[i] for i in f])

    mesh = bpy.data.meshes.new("3DMapMesh")
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name="3DMapObject", object_data=mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    obj.scale = (1, 1, 1)

    mesh.update()

class MapDataProps(bpy.types.PropertyGroup):
    rows: bpy.props.IntProperty(name="Rows")
    columns: bpy.props.IntProperty(name="Columns")
    

class MapDataOperator(bpy.types.Operator):
    bl_idname = "object.map_data"
    bl_label = "Render with this data"

    def execute(self, context):
        create_map(bpy.context.scene.MapDataProps.rows, bpy.context.scene.MapDataProps.columns)
        return {'FINISHED'}


class ReadMapDataPanel(bpy.types.Panel):
    #"""Creates a Panel in the Object properties window"""
    """Creates a Panel in the 3D window"""
    bl_label = "Render Menu"
    #bl_idname = "OBJECT_PT_read_map_data"
    bl_idname = "VIEW3D_PT_map_data"
    #bl_space_type = "PROPERTIES"
    bl_space_type = "VIEW_3D"
    #bl_region_type = "WINDOW"
    bl_region_type = "UI"
    #bl_context = "object"
    bl_category = "Map Menu"

    def draw(self, context):
        props = bpy.context.scene.MapDataProps
        layout = self.layout

        col = layout.column()

        row = col.row()
        row.prop(props, "rows")
        row.prop(props, "columns")
        row = col.row()
        row.operator("object.map_data")

def register():
    bpy.utils.register_class(MapDataProps)
    bpy.utils.register_class(MapDataOperator)
    bpy.utils.register_class(ReadMapDataPanel)
    bpy.types.Scene.MapDataProps = bpy.props.PointerProperty(type=MapDataProps)

def unregister():
    bpy.utils.unregister_class(ReadMapDataPanel)
    bpy.utils.unregister_class(MapDataOperator)
    bpy.utils.unregister_class(MapDataProps)
    del(bpy.types.Scene.MapDataProps)

if __name__ == "__main__":
    register()
    # This can be used to remove the menu.
    # unregister()