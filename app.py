import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_colors(image, num_colors=5):
    image = image.resize((150, 150))
    data = np.array(image)
    data = data.reshape((-1, 3))

    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(data)
    colors = kmeans.cluster_centers_

    rounded_colors = [tuple(map(int, color)) for color in colors]
    return rounded_colors

st.title("A Cute Color Palette Generator")
st.write("Upload any image to receive a beautifully curated color palette!")
uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Your Image", use_container_width=True)
    palette = get_colors(image)

    st.write("Top Colors in the Image:")
    for color in palette:
        hex_color = "#{:02x}{:02x}{:02x}".format(*color)
        st.color_picker(label=hex_color, value=hex_color, disabled=True, key=hex_color)