
import streamlit as st

import numpy as np
import keras
import tensorflow as tf
import tensorflow.keras.layers as KerasLayer
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_custom_objects
import tensorflow_hub as hub

from tensorflow.keras.models import load_model

my_reloaded_model = tf.keras.models.load_model(
       ('satellite_military.h5'),
       custom_objects={'KerasLayer':hub.KerasLayer}
)



# Define a dictionary to map custom layer names to their implementations
#custom_objects1 = {'KerasLayer': KerasLayer}

# Load the model using custom_objects
#loaded_model=load_model('satellite_military.h5')
#custom_objects=custom_objects1)


#l#oaded_model = keras.models.load_model(r'C:/Users/eberd/Desktop/satellite_military.h5')





