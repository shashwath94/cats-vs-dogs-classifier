from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers.normalization import BatchNormalization

#image dimensions
img_width, img_height = 150, 150

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 10000
nb_validation_samples = 2499
nb_epoch = 10

#ConvNet model

'''
model = Sequential()

#first Conv + pool layer
model.add(Convolution2D(64, 3, 3, border_mode = 'same', input_shape = (img_width, img_height, 3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size = (2, 2), dim_ordering = 'tf'))

#second Conv + pool layer
model.add(Convolution2D(64, 3, 3, border_mode = 'same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size = (2, 2)))

#third conv + pool layer
model.add(Convolution2D(128, 4, 4, border_mode = 'same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Convolution2D(256, 3, 3, border_mode = 'same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
'''
model = Sequential()

#first layer
model.add(Convolution2D(32, 3, 3, input_shape=(img_width, img_height, 3)))
model.add(Convolution2D(32, 3, 3))
model.add(BatchNormalization())
model.add(Activation('relu'))
#model.add(MaxPooling2D(pool_size=(2, 2)))

#second layer
model.add(Convolution2D(64, 3, 3))
model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

#third layer
model.add(Convolution2D(128, 3, 3))
model.add(Convolution2D(128, 3, 3))
#model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

#fourth layer
model.add(Convolution2D(256, 3, 3))
model.add(Convolution2D(256, 3, 3))
model.add(Activation('relu'))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

#fully connected layers
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.compile(loss = 'binary_crossentropy',
    optimizer = 'rmsprop',
    metrics = ['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)


# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data
train_generator = train_datagen.flow_from_directory(
        train_data_dir,  # this is the target directory
        target_size=(img_width, img_height),  # all images will be resized to 150x150
        batch_size=32,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary')

model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples)

model.save('first_try.h5')

'''
datagen = ImageDataGenerator(
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode  = 'nearest')

img = load_img('data/train/cats/cat.0.jpg')     #this is a PIL image
x = img_to_array(img)       # converts the image to a numpy array of shape (150, 150, 3)
x = x.reshape((1, ) + x.shape)      # this is a Numpy array with shape (1, 3, 150, 150)


i = 0
for batch in datagen.flow(x, batch_size = 1, save_to_dir = 'preview', save_prefix = 'cat', save_format = 'jpeg'):
    i += 1
    if i > 20:
        break
'''
