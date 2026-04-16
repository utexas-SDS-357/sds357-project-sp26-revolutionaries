import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="Nashville Traffic & Stops Dashboard", layout="wide")
st.title("🚓 Nashville Traffic Crashes & Police Stops between 2009 - 2019")
st.markdown("""
This dashboard analyzes traffic crashes and police stops in Nashville, Tennessee 
to understand spatial and temporal patterns in traffic risk and enforcement.
""")

st.divider()
results_folder = "results"


if os.path.exists(results_folder):
    all_files = sorted(os.listdir(results_folder))
    image_files = [f for f in all_files if f.endswith(('.png', '.jpg', '.jpeg'))]
    csv_files = [f for f in all_files if f.endswith('.csv')]
    
    st.sidebar.title("Navigation Toggle")
    
    if image_files:
        st.sidebar.subheader("Visualizations")
        selected_img = st.sidebar.selectbox(
            "Choose a plot to view:", 
            image_files, 
            format_func=lambda x: x.split('.')[0].replace("_", " ").title()
        )
        st.subheader(selected_img.split('.')[0].replace("_", " ").title())
        img_path = os.path.join(results_folder, selected_img)
        st.image(Image.open(img_path), use_column_width=True)
        
    st.divider()
    
    if csv_files:
        st.sidebar.subheader("Data Tables")
        selected_csv = st.sidebar.selectbox(
            "Choose a table to view:", 
            csv_files, 
            format_func=lambda x: x.split('.')[0].replace("_", " ").title()
        )
        st.subheader(selected_csv.split('.')[0].replace("_", " ").title())
        csv_path = os.path.join(results_folder, selected_csv)
        df = pd.read_csv(csv_path)
        st.dataframe(df)

else:
    st.error("⚠️ The 'results' folder could not be found. Make sure you run your modeling notebooks to generate the plots first!")