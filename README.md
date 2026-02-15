# Handwritten Digit Recognition (MNIST) - ANN Model

This project is a **Handwritten Digit Recognition** system using an **Artificial Neural Network (ANN)** trained on the **MNIST dataset**.  
It allows users to upload an image of a handwritten digit and predicts the number in real-time using **Streamlit**.

---

## Features

- Upload handwritten digit images (`.png`, `.jpg`, `.jpeg`)
- Real-time prediction
- Image preprocessing (resize, normalize)
- Simple and easy-to-use **Streamlit interface**

---

## Model Details

- Model type: **Artificial Neural Network (ANN)**
- Dataset: **MNIST**
- Accuracy: ~97%
- Preprocessing: Grayscale, resized to 28x28, normalized
- Dropout added to reduce overfitting
- Early stopping used for better training

---

## How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/Shoaib152/Handwritten-Digit-Recognition.git


Go to the project directory:
cd Handwritten-Digit-Recognition

Install required packages:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

handwritten-digit-recognition/handwritten digit project/
│
├─ MNIST_ANN.ipynb 
├─ app.py
├─ model.h5
├─ requirements.txt
├─ README.md


Notes

Ensure your uploaded images are grayscale and properly centered for best predictions.

The model performs best on digits similar to MNIST style (28x28, black background, white digit).

Author

Shoaib Ahmed

GitHub: https://github.com/Shoaib152
