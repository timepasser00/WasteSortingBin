from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import motorControl
import test_image

def start():
    # Load the model
    # model = load_model('keras_model_new.h5')
    model = load_model('keras_model1.h5')
    test_image.click()
    # web_cam.click()
    image_path="test_img.jpg"
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open('test_img.jpg')
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    # print(prediction)
    if(prediction[0][0] > 0.5):
        print("cardboard")
        motorControl.run("cardboard")
    elif(prediction[0][1]> 0.5):
        print("plastic")
        motorControl.run("plastic")
    else:
        print("metal")
        motorControl.run("metal")
    
   

