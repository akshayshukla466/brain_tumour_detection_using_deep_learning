# 🧠 Brain Tumor Detection Using Deep Learning

A Deep Learning-based web application that detects brain tumors from MRI scan images using a trained Convolutional Neural Network (CNN). Users can upload MRI images and receive predictions regarding the presence of a brain tumor.

---

## 📌 Project Overview

Brain tumors are abnormal growths of cells inside the brain that can become life-threatening if not diagnosed early. This project uses Deep Learning and Computer Vision techniques to automate brain tumor detection from MRI scans.

The model is trained on MRI image datasets and deployed through a simple web application for real-time predictions.

---

## 🚀 Features

- Upload MRI brain scan images
- Detect presence of brain tumors
- Deep Learning-based prediction
- User-friendly interface
- Fast and efficient inference
- Pre-trained model included (`model.h5`)

---

## 📂 Project Structure

```text
Brain_Tumor_Detection/
│
├── venv/                               # Virtual environment
├── .venv/                              # Virtual environment
├── sample_images/
│   ├── tumor_sample.jpg
│   └── no_tumor_sample.jpg
├── app.py                              # Main application file
├── model.h5                            # Trained CNN model
├── brain_tumour_detection_using_deep_learning.ipynb
│                                      # Model training notebook
├── requirements.txt                    # Required dependencies
├── README.md                           # Project documentation
└── step to run on this machine.md      # Execution guide
```

---
## 📊 Dataset

This project uses the **Brain Tumor MRI Dataset** available on Kaggle.

Dataset Source:

- Kaggle: Brain Tumor MRI Dataset by Masoud Nickparvar
- Link: https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

### Dataset Classes

The dataset contains MRI images belonging to the following categories:

- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- No Tumor
---
### Dataset Structure

```text
Data/
├── Training/
│   ├── glioma/
│   ├── meningioma/
│   ├── pituitary/
│   └── notumor/
│
└── Testing/
    ├── glioma/
    ├── meningioma/
    ├── pituitary/
    └── notumor/
```

> Note: The dataset is not included in this repository due to its large size. Please download it directly from Kaggle and place it inside the `Data/` directory before training or testing the model.
## Model File

The trained model (`model.h5`) is not included in this repository because it exceeds GitHub's file size limit.

To use the application:

1. Train the model using the provided notebook.
2. Save the trained model as `model.h5`.
3. Place the file in the project root directory.
## Download Pretrained Model

Download the pretrained model from:

https://drive.google.com/file/d/111L-RDMkXn198g-Ha9VsCK9d6pWqpv5k/view?usp=drivesdk

 Place `model.h5` in the project root directory before running the application.
---

## 🧪 Testing the Application

For quick testing, sample MRI images are provided in the `sample_images/` folder.

### Steps

1. Run the application.
2. Upload an image from the `sample_images/` folder.
3. Click **Predict**.
4. View the prediction result.

Sample files:

- `tumor_sample.jpg`
- `no_tumor_sample.jpg`

---



## 🛠️ Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- OpenCV
- Matplotlib
- Jupyter Notebook
- Flask

---

## 🧠 Model Workflow

1. Load MRI images
2. Preprocess images
   - Resize images
   - Normalize pixel values
3. Train CNN model
4. Save trained model (`model.h5`)
5. Load model in the application
6. Predict tumor presence from uploaded MRI scans

---

## 📊 Dataset

The dataset contains MRI brain scan images categorized into:

- Tumor
- No Tumor

Dataset is stored inside the `Data/` folder.

> Make sure the dataset structure remains the same as used during training.

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd Brain_Tumor_Detection
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧪 Model Training

To retrain the model:

1. Open the notebook:

```bash
brain_tumour_detection_using_deep_learning.ipynb
```

2. Run all cells.

3. Save the trained model:

```python
model.save("model.h5")
```

---

## 📸 Usage

1. Start the application.
2. Upload an MRI scan image.
3. Click **Predict**.
4. View prediction results.
5. Check whether a brain tumor is detected.

---

## 📈 Future Enhancements

- Multi-class tumor classification
- Improved prediction accuracy
- Grad-CAM visualization
- Cloud deployment
- Mobile application support
- Automatic medical report generation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes only.

The predictions generated by the model should **not** be considered a replacement for professional medical diagnosis. Always consult qualified healthcare professionals for medical advice.

---

## 📜 License

This project is available for educational and non-commercial use.

---
