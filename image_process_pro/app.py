import cv2
import numpy as np
import json
import pygame
pygame.init()
import pathlib
from PIL import Image
import mediapipe as mp
import streamlit as st
import cvzone
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
from cvzone.SelfiSegmentationModule import SelfiSegmentation


st.set_page_config(page_title="image", page_icon="📷", layout="wide")

# ------------------ Title ------------------
st.markdown("""
<style>
    .title {
           color: white;
           font-size: 45px;
           text-align: center;
           font-weight: 700;
           padding:25px;
           background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63));
           border-radius:10px;
    }
</style>
""", unsafe_allow_html=True)


def load_lottie_file(filepath:str):
    with open(filepath,"r")as f:
        return json.load(f)

def css_file(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

filepath = pathlib.Path("image.css")
css_file(filepath)


st.markdown('<div class="title">📷 Advance Image Preprocessor</div>', unsafe_allow_html=True)

# ------------------ File Uploader ------------------
img_file = st.file_uploader("**Load Image ...**", type=['jpg', 'jpeg', 'png'])

# Initialize 'img' to None to prevent NameError
img = None

if img_file is not None:
    file_bytes = np.asarray(bytearray(img_file.read()), np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if st.button("Show Image"):
        pygame.mixer.music.load("bell.wav")
        pygame.mixer.music.play()
        st.image(img, caption="Original Image", use_container_width=True)
else:
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(29, 4, 108),rgb(120, 2, 63)); color:white;padding:10px;text-align:center;font-size:25px;font-weight:800;border-radius:10px;">👆 Please upload an image to begin.</div>',
        unsafe_allow_html=True)
    #st.warning("👆 Please upload an image to begin.")

st.markdown("---")

# ------------------ Sidebar Menu ------------------
with st.sidebar:
    st.title("Menu Design")
    st.markdown("---")
    back_remove = st.toggle("🪄 Remove Background")
    back_blur = st.toggle("🌫️ Background Blur")
    cartoon = st.toggle("🎨 Cartoon Effect")
    edge = st.toggle("✂️ Edge Detection")
    hist = st.toggle("📊 Image Histogram")
    filters = st.toggle("🔮 All Filters")

# ------------------ Background Removal ------------------
if back_remove and img is not None:
    pygame.mixer.music.load("pop_2.wav")
    pygame.mixer.music.play()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("**⚙️ Settings & Customization**")
        threshold = st.slider("**Select Threshold Value**",0.0,1.0,0.3)
        color_hex = st.color_picker("**🎨 Select Background Color**", "#00ff00")
        # convert hex → RGB (no reversal)
        color_rgb = tuple(int(color_hex.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

    with col2:
        st.subheader("🪄 Background Removed Image")
        segmentor = SelfiSegmentation()
        output = segmentor.removeBG(img, color_rgb, cutThreshold=threshold)
        st.image(output, use_container_width=True)
        success1, buffer1 = cv2.imencode(".jpg", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
        if success1:
            st.download_button(
                label="Download Image",
                data=buffer1.tobytes(),
                file_name="old.jpg",
                mime="image/jpeg"
            )
elif back_remove and img is None:
    pygame.mixer.music.load("voice_1.wav")
    pygame.mixer.music.play()
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">Please upload an image before using the background remover.</div>',
        unsafe_allow_html=True)


# ------------------ Background Blur ------------------
if back_blur and img is not None:
    pygame.mixer.music.load("pop_2.wav")
    pygame.mixer.music.play()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("**⚙️ Settings & Customization**")
        blur_label = st.slider("**Select Blur Intensity**", 1, 99, 25, step=2)
        c_threshold = st.slider("**Select Threshold Value**", 0.0, 1.0, 0.5, step=0.05)

    with col2:
        st.subheader("🌫️ Background Blur Image")
        segmentor = SelfiSegmentation()
        blur_img = cv2.GaussianBlur(img, (blur_label, blur_label), 0)
        output = segmentor.removeBG(img, blur_img, cutThreshold=c_threshold)
        #output = cv2.resize(output,(640,480))
        st.image(output, use_container_width=True)
        success2, buffer2 = cv2.imencode(".jpg", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
        if success2:
            st.download_button(
                label="Download Image",
                data=buffer2.tobytes(),
                file_name="remove.jpg",
                mime="image/jpeg"
            )
elif back_blur and img is None:
    pygame.mixer.music.load("voice_2.wav")
    pygame.mixer.music.play()
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">Please upload an image before creating blurring background.</div>',
        unsafe_allow_html=True)


# ------------------ Carton Image ------------------
if cartoon and img is not None:
    pygame.mixer.music.load("pop_2.wav")
    pygame.mixer.music.play()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("**⚙️ Settings & Customization**")
        block_size = st.slider("**Select Block Size**", 1, 99, 19, step=2)
        c = st.slider("**Select C Value**", 0, 10, 6, step=2)
        d = st.slider("**Select D Value**",1,11,9,step=2)
    with col2:
        st.subheader("🎨 Carton Image")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 3)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=block_size, C=c)
        color = cv2.bilateralFilter(img, d=d, sigmaColor=250, sigmaSpace=250)
        output = cv2.bitwise_and(color, color, mask=edges)
        st.image(output, use_container_width=True)
        success3, buffer3 = cv2.imencode(".jpg", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
        if success3:
            st.download_button(
                label="Download Image",
                data=buffer3.tobytes(),
                file_name="carton.jpg",
                mime="image/jpeg"
            )
elif cartoon and img is None:
    pygame.mixer.music.load("voice_3.wav")
    pygame.mixer.music.play()
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">Please upload an image before creating carton image.</div>',
        unsafe_allow_html=True)



# ------------------ Edge Detection ------------------
if edge and img is not None:
    pygame.mixer.music.load("pop_2.wav")
    pygame.mixer.music.play()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("**⚙️ Settings & Customization**")
        low = st.slider("🔽 Lower Threshold", 0, 255, 100)
        high = st.slider("🔼 Upper Threshold", 0, 255, 200)
    with col2:
        st.subheader("✂️ Edge Detection")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output = cv2.Canny(gray, threshold1=low, threshold2=high)
        st.image(output, use_container_width=True)
        success4, buffer4 = cv2.imencode(".jpg", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
        if success4:
            st.download_button(
                label="Download Image",
                data=buffer4.tobytes(),
                file_name="edge.jpg",
                mime="image/jpeg"
            )
elif edge and img is None:
    pygame.mixer.music.load("voice_4.wav")
    pygame.mixer.music.play()
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">Please upload an image before using the edge detection.</div>',
        unsafe_allow_html=True)

# ------------------ Plot Image Distribution ------------------
if hist and img is not None:
    pygame.mixer.music.load("pop_2.wav")
    pygame.mixer.music.play()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("**📊 Plot Image HistoGram**")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_hist = cv2.equalizeHist(gray)
        hist_values = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=np.arange(256),
            y=hist_values,
            mode='lines',
            line=dict(color='royalblue', width=2),
            name="Pixel Intensity"
        ))

        fig.update_layout(
            title="",
            xaxis_title="Pixel Intensity (0-255)",
            yaxis_title="Frequency",
            template="plotly_dark",
            width=500,
            height=350
        )

        # Show equalized image and histogram
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("**Gray Scale Image**")
        st.image(img_hist, use_container_width=True)
        success5, buffer5 = cv2.imencode(".jpg", img_hist)
        if success5:
            st.download_button(
                label="Download Image",
                data=buffer5.tobytes(),
                file_name="edge.jpg",
                mime="image/jpeg"
            )
elif hist and img is None:
    pygame.mixer.music.load("voice_5.wav")
    pygame.mixer.music.play()
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">Please upload an image before plot histogram.</div>',
        unsafe_allow_html=True)



# ------------------ Image All Filters ------------------
if filters and img is not None:
    pygame.mixer.music.load("pop_2.wav")
    pygame.mixer.music.play()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("**⚙️ Settings & Customization**")
        side  = st.columns(2)
        with side[0]:
            blur = st.button("💧 Normal Blur",key="one")
            box = st.button("📦 Box Blur",key="two")
            gauss = st.button("🌫️ Gaussian Blur",key="three")
            median = st.button("🔹 Median Blur",key="four")
            bilateral = st.button("🌀 Bilateral Blur",key="five")
        with side[1]:
            sharp_1 = st.button("**✴️ Sharp 1**",key="six")
            sharp_2 = st.button("**⚡ Sharp 2**",key="seven")
            sharp_3 = st.button("**💎 Sharp 3**",key="eight")
            laplacian = st.button("**🔹 Lapacian**",key="nine")
            sobel = st.button("**🌫️ Sobel**",key="ten")
    with col2:
        st.subheader("🔮 Image All Filters")
        output = None
        if blur:
            output = cv2.blur(img, (25, 25))
        if box:
            output = cv2.boxFilter(img, -1, (5, 5))
        if gauss:
            output = cv2.GaussianBlur(img, (5, 5), 0)
        if median:
            output = cv2.medianBlur(img, 5)
        if bilateral:
            output = cv2.bilateralFilter(img,5,6,6)
        if sharp_1:
            output = cv2.addWeighted(img,1.5,gauss,-0.5,0)
        if sharp_2:
            output = cv2.addWeighted(img, 3.5, gauss, -2.5, 0)
        if sharp_3:
            output = cv2.addWeighted(img,7.5,gauss,-6.5,0)
        if laplacian:
            output = cv2.Laplacian(img,-1)
        if sobel:
            output = cv2.Sobel(img,-1,1,0)
        if output is not None:
            st.image(output, use_container_width=True)
            success3, buffer3 = cv2.imencode(".jpg", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
            if success3:
                st.download_button(
                    label="Download Image",
                    data=buffer3.tobytes(),
                    file_name="carton.jpg",
                    mime="image/jpeg"
                )
        else:
            st.markdown(
                '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">👆 Select a filter to preview the result.</div>',
                unsafe_allow_html=True)
elif filters and img is None:
    pygame.mixer.music.load("voice_6.wav")
    pygame.mixer.music.play()
    st.markdown(
        '<div class="result-box" style="background: linear-gradient(to right, rgb(4, 97, 123),rgb(4, 4, 134)); color:white;padding:7px;text-align:center;font-size:20px;font-weight:800;border-radius:10px;">Please upload an image before using the all filters.</div>',
        unsafe_allow_html=True)

data_lottie = load_lottie_file("Icon 5 3D.json")
st_lottie(
    data_lottie,
    height=400,
    width=None
)


