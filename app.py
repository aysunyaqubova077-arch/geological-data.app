import streamlit as st import pandas as pd import plotly.graph_objects as go
lithology_options = ["Qumdaşı", "Əhəngdaşı", "Aleurolit", "Dolomit", "Çınqıl", "Gil", "Mergel"]
st.title("Geoloji Model - 3D Vizualizasiya")
st.sidebar.header("Parametrlər və Lay Tənzimləmələri") num_layers = st.sidebar.slider("Layların sayı", 1, 10, 3)
layer_data = [] for i in range(num_layers): name = st.sidebar.text_input(f"Lay {i+1} Adı", value=f"Lay {i+1}") depth = st.sidebar.number_input(f"Lay {i+1} dərinliyi (m)", value=float((i+1)*100)) color = st.sidebar.color_picker(f"Lay {i+1} rəngi", value="#1f77b4" if i==0 else "#ff7f0e") lithology = st.selectbox(f"Lay {i+1} Litologiyası", lithology_options)
prev_depth = 0 if i == 0 else layer_data[i-1]["Dərinlik"]
thickness = depth - prev_depth

layer_data.append({
    "Lay": name, 
    "Dərinlik": depth, 
    "Qalınlıq (m)": thickness, 
    "Litologiya": lithology, 
    "Rəng": color
})
st.markdown("---") if not layer_data: df = pd.DataFrame(columns=["Lay", "Dərinlik", "Qalınlıq (m)", "Litologiya", "Rəng"]) else: df = pd.DataFrame(layer_data)
col1, col2, col3 = st.columns(3) col1.metric("Ümumi Qazma Dərinliyi", f"{df['Dərinlik'].max() if not df.empty else 0} m") col2.metric("Ümumi Lay Sayı", len(df)) col3.metric("Əsas Litologiya", df['Litologiya'].mode()[0] if not df.empty else "-")
st.subheader("Daxil edilmiş lay məlumatları:") st.data_editor(df)
csv_data = df.to_csv(index=False).encode('utf-8') st.download_button( label="📥 Lay Məlumatlarını Hesabat Kimi Yüklə (CSV)", data=csv_data, file_name="geoloji_lay_hesabati.csv", mime="text/csv", )
fig = go.Figure()
for i, row in df.iterrows(): fig.add_trace(go.Scatter3d( x=[0, 1, 1, 0, 0], y=[0, 0, 1, 1, 0], z=[-row["Dərinlik"], -row["Dərinlik"], -row["Dərinlik"], -row["Dərinlik"], -row["Dərinlik"]], mode='lines', name=row["Lay"], line=dict(color=row["Rəng"], width=5) ))
fig.update_layout( title="3D Geoloji Lay Modelləri", scene=dict( xaxis_title='X (metr)', yaxis_title='Y (metr)', zaxis_title='Dərinlik Z (metr)' ) )
st.plotly_chart(fig)


