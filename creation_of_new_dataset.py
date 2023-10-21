import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import pathlib

df=pd.read_csv (r"data\readmission.csv")


dir = pathlib.Path('data')

# Get a list of all the files in the data directory and its subdirectories
image_files = list(dir.glob('*/*'))
severity_labels = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

diabetic = []

for j in severity_labels:
        folderPath = os.path.join(dir,j)
        for k in tqdm(os.listdir(folderPath)):
            img = os.path.join(folderPath,k)
            diabetic.append(img)
print(diabetic)

df['diabetic_eye'] = diabetic

print(df)

df.to_csv('data/Overall_Dataset.csv')