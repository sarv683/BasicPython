# BasicPython
Cheat Sheet :

1. Copying files from all files inside a directory to another folder :

```

import os
import glob
src_dir = ""
dst_dir = ""
for myfile in glob.iglob(src_dir + "**/*.TIFF",recursive=True):
    shutil.copy(myfile, dst_dir)

```



2. Getting images and image paths: 

```

img_rgb = [cv2.imread(file) for file in glob.glob("")]

names = [os.path.basename(x) for x in glob.glob("")]

```

3. Pandas basics
```
Reading csv : 
data = pd.read_csv("",sep=";")

dropping columns/rows

data=data.drop(data.rows[[1,2,3....]],axis=0)
# axis=1 for columns

merging files : 
merged = data.merge(data1, on='')
merged.to_csv("xx.csv", index=False)


displaying all columns/rows : 
pandas.set_option('display.max_columns', None)
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

```

4. Basics of Plotting/Visualization
```
plot_distribution( titanic , var = 'Age' , target = 'Survived' , row = 'Sex' )
plot_correlation_map( titanic )

Missing variables : 

# Create dataset
imputed = pd.DataFrame()

# Fill missing values of Age with the average of Age (mean)
imputed[ 'Age' ] = full.Age.fillna( full.Age.mean() )

# Fill missing values of Fare with the average of Fare (mean)
imputed[ 'Fare' ] = full.Fare.fillna( full.Fare.mean() )

imputed.head()
