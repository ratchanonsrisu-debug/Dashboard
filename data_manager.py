import pandas as pd
import random

def get_gpu_data():
    # รายชื่อรุ่นและคะแนนความแรง (Benchmark)
    gpu_models = [
        ('RTX 4090', 'NVIDIA', 100), ('RTX 4080', 'NVIDIA', 85),
        ('RTX 4070', 'NVIDIA', 70), ('RTX 4060', 'NVIDIA', 55),
        ('RX 7900 XTX', 'AMD', 92), ('RX 7800 XT', 'AMD', 78),
        ('RX 7700 XT', 'AMD', 65), ('RX 7600', 'AMD', 50)
    ]
    
    data = []
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    
    for model, brand, benchmark in gpu_models:
        # กำหนดราคาพื้นฐานตามความแรง
        base_price = benchmark * 15 + random.randint(200, 400)
        for month in months:
            # จำลองราคาให้แกว่งขึ้นลงแต่ละเดือน
            price = base_price + random.randint(-100, 150)
            stock = random.randint(5, 50)
            data.append([month, model, brand, price, benchmark, stock])
            
    return pd.DataFrame(data, columns=['Month', 'Model', 'Brand', 'Price', 'Score', 'Stock'])