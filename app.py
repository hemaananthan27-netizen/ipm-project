import streamlit as st

st.title("🌿 AI-Based Pest Detection System")

st.write("Upload an image to detect pest and get recommendation")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("🧠 AI Prediction: Pest detected (Demo)")
    st.write("⚠️ Severity: Medium")
    st.write("💡 Recommendation: Use neem-based pesticide")
