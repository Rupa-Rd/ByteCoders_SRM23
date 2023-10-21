import cv2
import numpy as np
from tensorflow import keras
from PIL import Image
# Load the trained model
model = keras.models.load_model('Diabetic_Retinopathy_model.pkl')

def retinopathy_prediction():
    
    image = np.array(Image.open(r"test_data\test_3.png").resize((256, 256)))
    images_list = []
    images_list.append(np.array(image))
    x = np.asarray(images_list)
    pr_mask = model.predict(x)
    p = pr_mask.tolist()
    percent = p[0]
    percent = [j*100 for j in percent]
    high_percent = max(percent)
    high_percent_index = percent.index(high_percent)
    high_percent = round(high_percent,2)
    return [high_percent,high_percent_index]

# arr = output()
# print('{}% is {}'.format(arr[0],arr[1]))
