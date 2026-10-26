import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Geoloji Model - 3D Vizuallaşdırma")

st.sidebar.header("Parametrlər və Lay Tənzimləmələri")
num_layers = st.sidebar.slider("Layların sayı", 1, 10, 3)

layer_data = []
for i in range(num_layers):
    name = st.sidebar.text_input(f"Lay {i+1} Adı", value=f"Lay {i+1}")
    depth = st.sidebar.number_input(f"{name} dərinliyi (m)", value=float((i+1)*100))
    color = st.sidebar.color_picker(f"{name} rəngi", value="#1f77b4" if i==0 else ("#ff7f0e" if i==1 else "#2ca02c"))
    layer_data.append({"Lay": name, "Dərinlik": depth, "Rəng": color})

df = pd.DataFrame(layer_data)
st.subheader("Daxil edilmiş lay məlumatları:")
st.data_editor(df)

fig = go.Figure()

for i, row in df.iterrows():
    fig.add_trace(go.Scatter3d(
        x=[0, 1, 1, 0, 0],
        y=[0, 0, 1, 1, 0],
        z=[-row["Dərinlik"], -row["Dərinlik"], -row["Dərinlik"], -row["Dərinlik"], -row["Dərinlik"]],
        mode='lines',
        name=row["Lay"],
        line=dict(color=row["Rəng"], width=5)
    ))

fig.update_layout(
    title="3D Geoloji Lay Modeli",
    scene=dict(
        xaxis_title='X (metr)',
        yaxis_title='Y (metr)',
        zaxis_title='Dərinlik Z (metr)'
    )
)

st.plotly_chart(fig)
