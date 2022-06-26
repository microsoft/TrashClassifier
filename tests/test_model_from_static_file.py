# ------------------------------------------------------------------------
# Trash Classifier ML Project - Test script for the usage of TF Model: file access and prediction
# Expected behaviour: successfully reads the model and makes a prediction from a static image file
# 
# (c) 2020 by Jen Fox, Microsoft
# MIT License
# --------------------------------------------------------------------------

from lobe import ImageModel

# Static locations for model and image for testing. 
# Please make sure those files are in those static locations before running the script
STATIC_MODEL_PATH = "/home/pi/Lobe/model" # realpath for model
STATIC_JPG_PATH = "/home/pi/Pictures/image.jpg" # realpath for image

# Load model and create prediction from image
model = ImageModel.load(STATIC_MODEL_PATH)
result = model.predict_from_file(STATIC_JPG_PATH)
print("The result of the prediction was {0}.".format(result.prediction))
