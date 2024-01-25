"""This module is called if there is no dataset nor model. It downloads the plant village dataset from tensorflow as a default."""
import tensorflow_datasets as tfds
import os
from shutil import rmtree

#Set the directory where the dataset will be stored
main_dir = os.path.join(os.getcwd(), "Dataset")

#Download
_, _ = tfds.as_numpy(tfds.load('plant_village', 
                                split=['train[:80%]', 'train[80%:]'], 
                                as_supervised=True, 
                                data_dir=main_dir))

#Remove the leaves without background as they are not useful
rmtree(os.path.join(os.getcwd(),
                    "Dataset",
                    "downloads",
                    "extracted",
                    "ZIP.data.mend.com_publ-file_data_tywb_file_d565-c1rDQyRTmE0CqGGXmH53WlQp0NWefMfDW89aj1A0m5D_A",
                    "Plant_leave_diseases_dataset_without_augmentation", 
                    "Background_without_leaves"))