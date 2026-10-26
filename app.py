# ==========================================
# Müəllif: Yaqubzadə Aysun
# Layihə: Geoloji Model - 3D İnteraktiv Litologiya
# ==========================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Səhifə konfiqurasiyası
st.set_page_config(page_title="Geoloji Model", layout="wide")

# Müəllif məlumatı (Yan paneldə göstərilməsi)
st.sidebar.markdown("### 👩‍💻 Müəllif")
st.sidebar.info("**Hazırladı:** Yaqubzadə Aysun")
st.sidebar.markdown("---")

# Litologiya üslubları və rəngləri
lithology_styles = {
    "Qumdaşı": {"color": "#e69c24", "pattern": "Diamonds"},
    "Əhəngdaşı": {"color": "#32a852", "pattern": "Bricks"},
    "Aleurolit": {"color": "#a8a232", "pattern": "Scattered Dots"},
    "Dolomit": {"color": "#32a89e", "pattern": "Lines"},
    "Gilli": {"color": "#326fa8", "pattern": "Dense Dots"},
    "Mergel": {"color": "#a83232", "pattern": "Grid"}
}

st.title("Geoloji Model - 3D İnteraktiv Litologiya")
st.caption("Hazırladı: **Yaqubzadə Aysun**")

st.sidebar.header("Parametrlər")
num_layers = st.sidebar.slider("Layların sayı", 1, 10, 3, key="num_layers_slider")

layer_data = []
previous_depth = 0.0

for i in range(num_layers):
    name =
