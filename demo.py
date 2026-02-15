
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# ----- Load Model -----
model = load_model("my_model.h5")  # Tumhara saved model ka naam

st.title("MNIST Handwritten Digit Recognition")
st.write("Upload karo apna handwritten digit image aur predict dekho!")

# ----- File uploader -----
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Image ko load aur preprocess karo
    image = Image.open(uploaded_file).convert("L")  # Grayscale
    # image = ImageOps.invert(image)                  # Invert if background is black
    image = image.resize((28, 28))                  # MNIST size
    image_array = np.array(image) / 255.0           # Normalize
    image_array = image_array.reshape(1, 28, 28, 1)

    # Prediction
    prediction = np.argmax(model.predict(image_array))
    st.write(f"Predicted Digit: {prediction}")
    st.image(image, caption="Uploaded Image", use_column_width=True)
