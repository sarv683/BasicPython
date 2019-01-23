# BasicPython
Cheat Sheet :

1. Copying files from all files inside a directory to another folder :

```

import os
import glob
img_rgb = [cv2.imread(file) for file in glob.glob("D:/Sarvesh/EvalImages/Background/*.JPEG")]
names = ["Weld" + os.path.basename(x) for x in glob.glob("D:/Sarvesh/EvalImages/Background/*.JPEG")]

```



2. Getting images and image paths: 

````

img_rgb = [cv2.imread(file) for file in glob.glob("")]

names = [os.path.basename(x) for x in glob.glob("")]

```
