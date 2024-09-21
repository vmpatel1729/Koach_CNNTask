import tensorflow as tf
from PIL import Image
import numpy as np
model = tf.keras.models.load_model("./models/model6/digit_classification_cnn_with_BatchNormalizationAndDropout_2.h5")

image_path = "./images/8.jpeg" 
image = Image.open(image_path).convert("L") 

 
image = image.resize((32, 32))
image_array = np.array(image)
image_array = image_array
# print(image_array[16])
image_array = image_array.reshape((1, 32, 32, 1))
predictions = model.predict(image_array)
predicted_class = np.argmax(predictions, axis=1)

print(f"Predicted Digit: {predicted_class[0]}")