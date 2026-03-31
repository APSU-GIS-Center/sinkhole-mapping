import arcpy

# Set the environment workspace to your geodatabase or folder
arcpy.env.workspace = r"C:\Path\To\Your\Project.gdb"

# The name of your established sinkhole polygon layer
input_sinkholes = "Established_Sinkholes"

# The name of the output feature class that will contain the measurements
output_measurements = "Sinkholes_with_Axes"

# Execute Minimum Bounding Geometry
# 'RECTANGLE_BY_WIDTH' determines the longest axis and its width.
# 'MBG_FIELDS' ensures MBG_Length and MBG_Width are sent to the attribute table.
arcpy.management.MinimumBoundingGeometry(
    in_features=input_sinkholes,
    out_feature_class=output_measurements,
    geometry_type="RECTANGLE_BY_WIDTH",
    group_option="NONE",
    group_field=None,
    mbg_fields_option="MBG_FIELDS"
)

print("Long and short axis measurements have been successfully added to the attribute table.")