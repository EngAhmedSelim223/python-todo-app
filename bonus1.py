import streamlit as st
from PIL import Image
import io

st.title("Camera & Upload to Grayscale Converter")

# Camera input
with st.expander("Open Camera."):
    camera_image = st.camera_input("Take a photo")

# File uploader input
uploaded_image = st.file_uploader("Or upload an image", type=["png", "jpg", "jpeg"])

# Choose which image to use
image_source = None
if camera_image is not None:
    image_source = camera_image
elif uploaded_image is not None:
    image_source = uploaded_image

if image_source is not None:
    # Display original image
    st.subheader("Original Image")
    st.image(image_source)

    # Convert to grayscale
    img = Image.open(image_source)
    gray_img = img.convert("L")

    # Display grayscale image
    st.subheader("Grayscale Image")
    st.image(gray_img)

    # Prepare grayscale image for download
    buf = io.BytesIO()
    gray_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Option to download
    st.download_button(
        label="Download Grayscale Image",
        data=byte_im,
        file_name="grayscale_image.png",
        mime="image/png"
    )
else:
    st.info("👆 Please take a photo or upload an image to see the grayscale conversion.")