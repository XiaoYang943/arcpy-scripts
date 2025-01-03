import arcpy

def print_arcgis_config():
    print(arcpy.metadata.Metadata)
    infos=arcpy.GetInstallInfo()
    for key, value in infos.items():
        print(u"{}={}".format(key, value))

if __name__ == '__main__':
    print_arcgis_config()
