import streamlit as st
<meta name="google-site-verification" content="7otJGZ-4O
import pandas as pd
import plotly.graph_objects as go

lithology_styles = {
    "Qumdaşı": {"color": "#e69c24", "pattern": "Diamonds"},
    "Əhəngdaşı": {"color": "#32a852", "pattern": "Bricks"},
    "Aleurolit": {"color": "#a8a232", "pattern": "Scattered Dots"},
    "Dolomit": {"color": "#32a89e", "pattern": "Lines"},
    "Gil": {"color": "#326fa8", "pattern": "Dense dots"},
    "Mərgel": {"color": "#a83232", "pattern": "Grid"}
}

st.title("Geoloji Model - 3D Interaktiv Litologiya")

st.sidebar.header("Parametrlər")
num_layers = st.sidebar.slider("Layların sayı", 1, 10, 3, key="num_layers_slider")

layer_data = []
previous_depth = 0.0

for i in range(num_layers):
    name = st.sidebar.text_input(f"Lay {i+1} Adı", value=f"Lay {i+1}", key=f"name_{i}")
    depth = st.sidebar.number_input(f"Lay {i+1} alt dərinliyi (m)", min_value=0.0, step=10.0, value=float((i+1)*100), key=f"depth_{i}")
    lithology = st.sidebar.selectbox(f"Lay {i+1} Litologiyası", list(lithology_styles.keys()), key=f"litho_{i}")
    
    thickness = depth - previous_depth
    style = lithology_styles[lithology]
    
    layer_data.append({
        "Lay": name,
        "Dərinlik": depth,
        "Qalınlıq (m)": thickness,
        "Litologiya": lithology,
        "Rəng": style["color"],
        "Tekstur": style["pattern"]
    })
    
    previous_depth = depth

df = pd.DataFrame(layer_data)

st.subheader("Daxil edilmiş lay məlumatları")
st.data_editor(df, use_container_width=True)

csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Lay Məlumatlarını CSV İxrac Et",
    data=csv_data,
    file_name="geoloji_lay_melumatlari.csv",
    mime="text/csv",
)

fig = go.Figure()

for i, row in df.iterrows():
    top_depth = 0.0 if i == 0 else df.loc[i-1, "Dərinlik"]
    bottom_depth = row["Dərinlik"]
    
    x_coords = [0, 100, 100, 0, 0, 0, 100, 100, 0, 0]
    y_coords = [0, 0, 100, 100, 0, 0, 0, 100, 100, 0]
    z_coords = [-top_depth, -top_depth, -top_depth, -top_depth, -top_depth, 
                -bottom_depth, -bottom_depth, -bottom_depth, -bottom_depth, -bottom_depth]
    
    fig.add_trace(go.Scatter3d(
        x=x_coords, y=y_coords, z=z_coords,
        mode='lines',
        name=f"{row['Lay']} ({row['Litologiya']})",
        line=dict(color=row["Rəng"], width=6),
        hoverinfo='text',
        text=f"Lay: {row['Lay']}<br>Litologiya: {row['Litologiya']}<br>Qalınlıq: {row['Qalınlıq (m)']}m"
    ))

fig.update_layout(
    title="3D Geoloji Lay Modelləri və Litologiya",
    scene=dict(
        xaxis_title='X Məsafəsi (m)',
        yaxis_title='Y Məsafəsi (m)',
        zaxis_title='Dərinlik (m)'
    ),
    legend_title="Litologiya və Laylar"
)

st.plotly_chart(fig)
