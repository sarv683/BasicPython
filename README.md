# BasicPython
Cheat Sheet :

1. Copying files from all files inside a directory to another folder :

org_dir = ""
dst_dir = ""

for filename in glob.iglob(src_dir + "**/*.TIFF",recursive=True):

    shutil.copy(filename, dst_dir)

2. Getting images and image paths: 

img_rgb = [cv2.imread(file) for file in glob.glob("")]

names = [os.path.basename(x) for x in glob.glob("")]
