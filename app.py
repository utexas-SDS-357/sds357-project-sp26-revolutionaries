import streamlit as st
import pandas as pd
import os
from PIL import Image


st.set_page_config(page_title="Nashville Traffic & Stops", page_icon="🚓", layout="wide")
st.title("🚓 Nashville Traffic Crashes & Police Stops (2009 - 2019)")
st.markdown("""
Explore spatial and temporal patterns in traffic risk and enforcement across Nashville, Tennessee. 
Use the **sidebar** to select multiple plots to compare. They will automatically organize into neat rows!
""")
st.divider()
results_folder = "results"

if os.path.exists(results_folder):
    all_files = sorted(os.listdir(results_folder))
    image_files = [f for f in all_files if f.endswith(('.png', '.jpg', '.jpeg'))]
    csv_files = [f for f in all_files if f.endswith('.csv')]
    
    st.sidebar.title("🎛️ Navigation Toggle")
    if image_files:
        st.sidebar.subheader("📊 Visualizations")
        cols_per_row = st.sidebar.radio(
            "Display layout:", 
            options=[1, 2], 
            format_func=lambda x: "1 Plot per Row (Larger)" if x == 1 else "2 Plots per Row (Side-by-side)",
            index=1
        )
        default_imgs = [image_files[0]] if len(image_files) > 0 else []
        selected_imgs = st.sidebar.multiselect(
            "Choose plots to compare:", 
            image_files,
            default=default_imgs,
            format_func=lambda x: x.split('.')[0].replace("_", " ").title()
        )
        
        if selected_imgs:
            for i in range(0, len(selected_imgs), cols_per_row):
                cols = st.columns(cols_per_row)
                
                for j in range(cols_per_row):
                    if i + j < len(selected_imgs):
                        selected_img = selected_imgs[i + j]
                        with cols[j]:
                            st.subheader(selected_img.split('.')[0].replace("_", " ").title())
                            img_path = os.path.join(results_folder, selected_img)
                            # use_column_width forces it to fill whatever space the column has
                            st.image(Image.open(img_path), use_column_width=True)
        else:
            st.info("👈 Please select a visualization from the sidebar.")
            
    st.divider()
    if csv_files:
        st.sidebar.subheader("📄 Data Tables")
        selected_csv = st.sidebar.selectbox(
            "Choose a table to view:", 
            csv_files, 
            format_func=lambda x: x.split('.')[0].replace("_", " ").title()
        )
        table_title = selected_csv.split('.')[0].replace("_", " ").title()
        with st.expander(f"🔍 View Data: {table_title}", expanded=False):
            csv_path = os.path.join(results_folder, selected_csv)
            df = pd.read_csv(csv_path)
            st.dataframe(df, use_container_width=True)
else:
    st.error("⚠️ The 'results' folder could not be found. Make sure you run your modeling notebooks to generate the plots first!")