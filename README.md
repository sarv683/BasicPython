# BasicPython
Cheat Sheet :

1. Copying files from all files inside a directory to another folder :

rc_dir = ""
dst_dir = ""
for filename in glob.iglob(src_dir + "**/*.TIFF",recursive=True):
    shutil.copy(filename, dst_dir)
