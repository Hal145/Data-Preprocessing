# 1- Function to split train dataset into train and validation sets, including the directories of more than one class.
# 2- Creates sub-directories and directories of the train and validation classes.

import os
import shutil
from sklearn.model_selection import train_test_split

root_dir = 'path/to/the/data/directory'

val_split = 0.2

classes = os.listdir(root_dir)

train_dir = os.path.join(root_dir, 'train')
val_dir = os.path.join(root_dir, 'val')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

for cls in classes:
    cls_dir = os.path.join(root_dir, cls)
    train_cls_dir = os.path.join(train_dir, cls)
    val_cls_dir = os.path.join(val_dir, cls)
    os.makedirs(train_cls_dir, exist_ok=True)
    os.makedirs(val_cls_dir, exist_ok=True)
    
    files = os.listdir(cls_dir)
    train_files, val_files = train_test_split(files, test_size=val_split, shuffle=True)
    
    for file in train_files:
        src = os.path.join(cls_dir, file)
        dst = os.path.join(train_cls_dir, file)
        shutil.copy(src, dst)
    
    for file in val_files:
        src = os.path.join(cls_dir, file)
        dst = os.path.join(val_cls_dir, file)
        shutil.copy(src, dst)
