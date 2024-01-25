import os
from tensorflow import keras

IMG_SHAPE = 256
BATCH_SIZE = 32

#Directory where all data is stored
data_dir = os.path.join(os.getcwd(),
                        "Dataset",
                        "downloads",
                        "extracted",
                        "ZIP.data.mend.com_publ-file_data_tywb_file_d565-c1rDQyRTmE0CqGGXmH53WlQp0NWefMfDW89aj1A0m5D_A",
                        "Plant_leave_diseases_dataset_without_augmentation")

#The path where model is or will be stored
model_path = os.path.join(os.getcwd(), "model")

#if model exists, then load it
if os.path.isdir(model_path):
    from tensorflow_hub import KerasLayer
    model = keras.models.load_model(model_path, custom_objects={'KerasLayer' : KerasLayer})

    class_file = open("classes.txt", "r")
    classes = class_file.read().replace(" ", "").split(",")

    #Modify some errors in dataset
    if "Pepper" in classes: classes.remove("Pepper")
    if "Pepper" in classes: classes.remove("Pepper")
    for i in range(len(classes)):
        if "_bell" in classes[i] and "Pepper" not in classes[i]:
            classes[i] = "Pepper"+classes[i]
    classes = sorted(classes)
    
#or else create it
else:
    #Download datset if not there
    if not os.path.isdir(os.path.join(os.getcwd(), "Dataset")):
        import download_data
    
    #Find all classes and save them to classes.txt for future reference
    classes = os.listdir(data_dir)
    for i in range(len(classes)):
        #Modify some errors in default dataset
        if "Pepper,_bell" in classes[i]:
            classes[i] = classes[i].replace(",", "_")
    classes = sorted(classes)
    print(classes)
    class_file = open("classes.txt", "w")
    for i in classes:
        class_file.write(i + ", ")

    #Prepare the dataset for model
    train_generator, test_generator = keras.utils.image_dataset_from_directory(data_dir,
                                                                               validation_split=0.2,
                                                                               subset="both",
                                                                               seed=123,
                                                                               image_size=(IMG_SHAPE, IMG_SHAPE),
                                                                               batch_size=BATCH_SIZE)
    
    #Make model
    model = keras.models.Sequential([keras.layers.Rescaling(1./255),
                                     keras.layers.Conv2D(8, (3,3), padding='same', activation='relu'),
                                     keras.layers.MaxPooling2D((2,2), strides=2),
                                     keras.layers.Conv2D(16, (3,3), padding='same', activation='relu'),
                                     keras.layers.MaxPooling2D((2,2), strides=2),
                                     keras.layers.Conv2D(32, (3,3), padding='same', activation='relu'),
                                     keras.layers.MaxPooling2D((2,2), strides=2),
                                     keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
                                     keras.layers.MaxPooling2D((2,2), strides=2),
                                     keras.layers.Conv2D(128, (3,3), padding='same', activation='relu'),
                                     keras.layers.MaxPooling2D((2,2), strides=2),
                                     keras.layers.Flatten(),
                                     keras.layers.Dense(128, activation='relu'),
                                     keras.layers.Dense(len(classes), activation='softmax')])

    model.build((None, IMG_SHAPE, IMG_SHAPE, 3))

    model.compile(optimizer = "adam",
                  loss = "sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    #Train model
    EPOCHS = 20
    history = model.fit(train_generator,
                        validation_data=test_generator,
                        epochs=EPOCHS)

    #Save as it would be impractical to train it every time the program runs
    keras.models.save_model(model, model_path)

class_file.close()