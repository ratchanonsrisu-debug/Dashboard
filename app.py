import streamlit as st
import pandas as pd
import plotly.express as px
from data_manager import get_gpu_data

# ตั้งค่าหน้าจอ
st.set_page_config(page_title="GPU Hunter Dashboard", layout="wide")

st.title("🚀 GPU Market Intelligence Dashboard")
st.markdown("วิเคราะห์แนวโน้มราคาและประสิทธิภาพการ์ดจอแบบเรียลไทม์")

# ดึงข้อมูลจากไฟล์ data_manager
df = get_gpu_data()

# --- 1. Interactive Sidebar ---
st.sidebar.header("🎛️ Filter Options")
brands = st.sidebar.multiselect("เลือกแบรนด์:", df['Brand'].unique(), default=df['Brand'].unique())
price_limit = st.sidebar.slider("งบประมาณ (USD):", int(df['Price'].min()), int(df['Price'].max()), (200, 2500))

# กรองข้อมูลตามที่เลือกใน Sidebar
filtered_df = df[(df['Brand'].isin(brands)) & (df['Price'].between(price_limit[0], price_limit[1]))]

# --- 2. Metrics (สรุปข้อมูลด้านบน) ---
if not filtered_df.empty:
    m1, m2, m3 = st.columns(3)
    m1.metric("จำนวนรุ่นที่พบ", len(filtered_df['Model'].unique()))
    m2.metric("ราคาเฉลี่ย", f"${filtered_df['Price'].mean():,.2f}")
    m3.metric("สต็อกรวม", filtered_df['Stock'].sum())

    # --- 3. กราฟทั้ง 3 แบบ ---
    col_left, col_right = st.columns(2)

    with col_left:
        # กราฟที่ 1: Line Chart (แนวโน้มราคา)
        st.subheader("📈 แนวโน้มราคารายเดือน")
        fig1 = px.line(filtered_df, x='Month', y='Price', color='Model', markers=True)
        st.plotly_chart(fig1, use_container_width=True)

    with col_right:
        # กราฟที่ 2: Scatter Plot (ความคุ้มค่า)
        st.subheader("⚖️ ราคา vs ประสิทธิภาพ")
        fig2 = px.scatter(filtered_df, x='Price', y='Score', color='Brand', 
                         size='Stock', hover_name='Model', text='Model')
        st.plotly_chart(fig2, use_container_width=True)

    # กราฟที่ 3: Bar Chart (สต็อกสินค้า)
    st.subheader("📦 จำนวนสินค้าในคลังแยกตามรุ่น")
    fig3 = px.bar(filtered_df, x='Model', y='Stock', color='Brand', barmode='group')
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("ไม่พบข้อมูลที่ตรงตามเงื่อนไข กรุณาปรับ Filter ใหม่")