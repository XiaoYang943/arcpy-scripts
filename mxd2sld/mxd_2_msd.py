import arcpy
if __name__ == "__main__":
    mxd_name = r'D:\data\vector\mbtiles\linespaceOutPut\planetiler\dltb\dltb.mxd'
    mxd_file = arcpy.mapping.MapDocument(mxd_name)
    arcpy.mapping.ConvertToMSD(mxd_file, 'wrm')