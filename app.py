import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Brain Tumor Detection",
    page_icon="🧠",
    layout="wide"
)

# ==========================
# MODEL LOAD
# ==========================
@st.cache_resource
def load_my_model():
    return load_model("model.h5")

model = load_my_model()

print("Model Input Shape:", model.input_shape)
# ==========================
# CLASS LABELS
# ==========================
class_labels = [
    "pituitary",
    "glioma",
    "notumor",
    "meningioma"
]

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>
.main{
    padding:2rem;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
}

.result{
    padding:20px;
    border-radius:15px;
    background:#f5f5f5;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown(
    '<div class="title">🧠 Brain Tumor Detection System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Deep Learning Based MRI Analysis</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================
# SIDEBAR
# ==========================
st.sidebar.header("Project Information")

st.sidebar.write("""
### Classes

- Pituitary Tumor
- Glioma Tumor
- Meningioma Tumor
- No Tumor

### Model

VGG16 Transfer Learning
""")

# ==========================
# UPLOAD IMAGE
# ==========================
uploaded_file = st.file_uploader(
    "Upload MRI Scan",
    type=["jpg", "jpeg", "png"]
)

# ==========================
# PREDICTION
# ==========================
def predict_image(image):

    # Convert grayscale image to RGB
    image = image.convert("RGB")

    image = image.resize((128, 128))

    img_array = img_to_array(image)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    print("Input Shape:", img_array.shape)

    predictions = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(predictions)

    confidence = float(np.max(predictions))

    return (
        class_labels[predicted_index],
        confidence,
        predictions[0]
    )
# ==========================
# MAIN
# ==========================
if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image,
            caption="Uploaded MRI",
            use_container_width=True
        )

    with col2:

        if st.button("Detect Tumor"):

            label, confidence, probs = predict_image(image)

            if label == "notumor":

                st.success(
                    f"No Tumor Detected\n\nConfidence: {confidence*100:.2f}%"
                )

            else:

                st.error(
                    f"{label.upper()} Tumor Detected\n\nConfidence: {confidence*100:.2f}%"
                )

            st.subheader("Prediction Probability")

            chart_data = {
                "pituitary": probs[0],
                "glioma": probs[1],
                "notumor": probs[2],
                "meningioma": probs[3]
            }

            st.bar_chart(chart_data)

            st.write("### Detailed Scores")

            for cls, prob in chart_data.items():
                st.write(
                    f"**{cls}** : {prob*100:.2f}%"
                )

st.divider()

st.caption(
    "Brain Tumor Detection using VGG16 Transfer Learning"
)