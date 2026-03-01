🚀 GPU Price Hunter: Market Intelligence Dashboard
โปรเจกต์นี้เป็น Interactive Dashboard สำหรับติดตามและวิเคราะห์ราคากาณ์ดจอ (GPU) ทั้งค่าย NVIDIA และ AMD เพื่อช่วยในการตัดสินใจเลือกซื้อตามงบประมาณและความคุ้มค่า

📋 คุณสมบัติของ Dashboard
Dashboard นี้ประกอบด้วย 3 กราฟหลักที่เชื่อมโยงกัน (Interactive):

Price Trend Chart (Line Chart): แสดงแนวโน้มราคาขายย้อนหลัง 5 เดือน (มกราคม - พฤษภาคม) ของแต่ละรุ่น เพื่อดูจังหวะการลดราคา

Efficiency Analysis (Scatter Plot): กราฟเปรียบเทียบระหว่าง "ราคา" และ "คะแนนประสิทธิภาพ" เพื่อหาจุดที่คุ้มค่าที่สุด (Sweet Spot)

Inventory Status (Bar Chart): แสดงจำนวนสินค้าในคลังแยกตามรุ่น เพื่อวิเคราะห์ความต้องการและการขาดแคลนของตลาด


🛠️ เทคโนโลยีที่ใช้
Python: ภาษาหลักในการพัฒนา

Streamlit: Framework สำหรับสร้าง Web Dashboard อย่างรวดเร็ว

Pandas: จัดการและทำความสะอาดข้อมูล (Data Wrangling)

Plotly Express: สร้างกราฟที่ผู้ใช้สามารถโต้ตอบได้ (Interactive Visualization)


🚀 วิธีการติดตั้งและรันโปรแกรม (How to Run)
1. การเตรียมสภาพแวดล้อม
ตรวจสอบว่าคุณมี Python ติดตั้งอยู่ในเครื่อง จากนั้นทำการ Clone Repository นี้:

Bash
git clone <URL_ของ_Git_คุณ>
cd <ชื่อโฟลเดอร์โปรเจกต์>
2. ติดตั้ง Library ที่จำเป็น
รันคำสั่งนี้ใน Terminal เพื่อติดตั้ง Dependencies ทั้งหมด:

Bash
pip install -r requirements.txt
3. เริ่มรัน Dashboard
ใช้คำสั่ง Streamlit เพื่อเปิดหน้าเว็บ:

Bash
streamlit run app.py
หมายเหตุ: หากรันบน GitHub Codespaces ให้กดปุ่ม Open in Browser เมื่อมีป็อปอัปแจ้งเตือนพอร์ต 8501


โครงสร้างไฟล์ในโปรเจกต์
app.py: ไฟล์หลักควบคุม UI, Sidebar และการแสดงผลกราฟทั้งหมด

data_manager.py: ไฟล์จัดการข้อมูลจำลอง (Mock Data) และ Logic การคำนวณราคา

requirements.txt: รายชื่อ Library ที่ต้องใช้ (Streamlit, Pandas, Plotly)

.gitignore: ไฟล์ระบุเพื่อไม่ให้ Git เก็บไฟล์ขยะ เช่น __pycache__


Sidebar Control: ใช้ st.sidebar.multiselect และ st.sidebar.slider เพื่อกรองข้อมูลแบรนด์และช่วงราคา

Data Binding: เมื่อผู้ใช้ปรับ Filter ใน Sidebar ตัวแปร filtered_df จะถูกอัปเดต และส่งข้อมูลใหม่ไปยังกราฟทั้ง 3 ทันที

Metrics: มีการใช้ st.metric เพื่อสรุปภาพรวม เช่น ราคาเฉลี่ยปัจจุบัน เพื่อให้ผู้ใช้เห็นข้อมูลสำคัญในทันที

############