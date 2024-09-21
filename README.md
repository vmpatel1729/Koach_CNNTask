# Digit Recognition Project

This project implements a Convolutional Neural Network (CNN) for digit classification using TensorFlow and Keras. It includes model training, evaluation, and a script for testing the model on individual images.

## Project Structure

```
project_root/
│
├── images/
│   └── image_8.png
│
├── models/
│   └── model6/
│       ├── digit_classification_cnn_with_BatchNormalizationAndDropout_2.h5
│       ├── digitclassification-2.py
│       ├── model_history-2.json
│
├── check_image.py
└── curves.py
```

## Description

This project focuses on digit recognition using a CNN model. The main components are:

1. **Model Training**: The model is trained using the script `digitclassification-2.py` in the `models/model6/` directory.

2. **Model Evaluation**: The training history is stored in `model_history-2.json`, and performance curves can be generated using `curves.py`.

3. **Image Classification**: The `check_image.py` script allows for testing the model on individual images.

## Usage

### Testing an Image

To classify a digit in an image:

1. Ensure you have the required dependencies installed:
   ```
   pip install tensorflow pillow numpy
   ```

2. Run the `check_image.py` script:
   ```
   python check_image.py
   ```

   This script:
   - Loads the trained model
   - Opens and preprocesses an image (default: `./images/image_8.png`)
   - Predicts the digit and outputs the result with a confidence score

3. To use your own image:
   - Open `check_image.py` in a text editor
   - Locate the line: `path = "./images/image_8.png"`
   - Change the path to the location of your image file, e.g.:
     ```python
     path = "./your_image_folder/your_image.png"
     ```
   - Save the file and run the script as described in step 2

Note: Ensure your image is a clear, well-lit picture of a single handwritten digit for best results.

## Model Details

The CNN model used for digit classification includes Batch Normalization and Dropout layers for improved performance and generalization. The model file is located at:

```
./models/model6/digit_classification_cnn_with_BatchNormalizationAndDropout_2.h5
```

### Model Architecture

Inspired from LeNet-5 architecture, this model uses a combination of Convolutional layers, Batch Normalization, Average Pooling, and Dropout:

1. **Batch Normalization**: It was applied after each dense and convolutional layer to normalize the inputs, which helped in:
   - Stabilizing the learning process i.e., 
   - Allowing higher learning rates, without worrying too much about vanishing and exploding gradients.
   - Reducing the sensitivity to weight initialization so that we do not have to worry about fine-tuning initialization techniques.

2. **Dropout**: Applied in the dense layers (with a rate of 0.5) to:
   - Prevent overfitting by randomly setting a fraction of input units to 0 during training
   - Improve generalization by reducing the model's reliance on specific features


### Model Performance

![Screenshot 2024-09-21 at 2 15 25 AM](https://github.com/user-attachments/assets/a304860b-a5e4-4ecc-ac0c-fcb196501a8c)
![Screenshot 2024-09-21 at 2 15 39 AM](https://github.com/user-attachments/assets/97e848dc-ca90-4dfc-a25d-e668d6228096)

The high test accuracy of 98.97% demonstrates the model's strong generalization capabilities on unseen data.

![training and validation loss](https://github.com/user-attachments/assets/38cf5d21-68ee-4202-81fb-51ee1750b29c)

## Contributors

Vishwesh Patel
