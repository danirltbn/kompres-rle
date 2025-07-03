import streamlit as st
from PIL import Image
import numpy as np
import io

st.set_page_config(page_title="Kompresi Gambar KTM - RLE", layout="wide")
st.title("🗜️ Kompresi Citra KTM - Metode Run-Length Encoding (RLE)")

# 📘 Petunjuk Penggunaan
with st.expander("📘 Cara Menggunakan Aplikasi Ini"):
    st.markdown("""
**Langkah-langkah penggunaan aplikasi kompresi gambar KTM inisfsfwwww:**

1. **Unggah gambar** KTM dalam format `.jpg`, `.jpeg`, `.png`, atau `.bmp` melalui panel di sebelah kiri.
2. Gambar akan otomatis dikonversi menjadi **hitam-putih (BW)** dan dikompresi menggunakan metode **Run-Length Encoding (RLE)**.
3. Di tab **📂 Kompresi File**, kamu bisa melihat:
   - Ukuran asli dan hasil kompresi
   - Rasio kompresi
   - Tombol untuk mengunduh **gambar hasil kompresi (BW)**
4. Di tab **🖼️ Preview Gambar**, kamu dapat melihat perbandingan gambar asli dan hasil konversi.
5. Di tab **📊 Statistik & Analisis**, kamu akan menemukan informasi statistik dari semua file yang telah dikompresi.
""")

tab1, tab2, tab3 = st.tabs(["📂 Kompresi File", "🖼️ Preview Gambar", "📊 Analisis Data"])

uploaded_files = st.sidebar.file_uploader("Unggah Gambar (PNG/JPG/BMP)", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=True)

compression_data = []

def encode_rle(data):
    if len(data) == 0:
        return ""
    encoded = []
    current = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current:
            count += 1
        else:
            color = "black" if current == 0 else "white"
            encoded.append(f"{color}:{count}")
            current = data[i]
            count = 1
    color = "black" if current == 0 else "white"
    encoded.append(f"{color}:{count}")
    return " | ".join(encoded)

with tab1:
    st.header("📥 Unggah & Kompresi")
    if uploaded_files:
        for file in uploaded_files:
            st.subheader(f"📁 {file.name}")
            image = Image.open(file)
            gray_image = image.convert("L")
            bw_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
            np_image = np.array(bw_image)

            rle_data = [encode_rle(row) for row in np_image]

            file_size = len(file.getvalue())
            compressed_size = sum(len(row) for row in rle_data)
            ratio = file_size / compressed_size if compressed_size else 0

            compression_data.append({
                "filename": file.name,
                "original_size": file_size,
                "compressed_size": compressed_size,
                "compression_ratio": ratio,
            })

            st.markdown(f"""
                **Ukuran Asli:** {file_size:,} bytes  
                **Ukuran Terkompresi:** {compressed_size:,} bytes  
                **Rasio Kompresi:** {ratio:.2f}
            """)

            # Download gambar hasil kompresi
            buffer = io.BytesIO()
            ext = file.name.split('.')[-1].lower()
            valid_exts = ["png", "jpg", "jpeg"]
            ext = ext if ext in valid_exts else "png"
            bw_image.save(buffer, format=ext.upper() if ext != "jpg" else "JPEG")
            st.download_button(f"⬇️ Unduh Gambar BW ({ext})", data=buffer.getvalue(), file_name=f"{file.name}_BW.{ext}", mime=f"image/{ext}")
    else:
        st.warning("Silakan unggah minimal 1 gambar untuk diproses.")

with tab2:
    st.header("🖼️ Preview Gambar Asli & Hitam-Putih")
    if uploaded_files:
        col1, col2 = st.columns(2)
        for file in uploaded_files:
            image = Image.open(file)
            gray_image = image.convert("L")
            bw_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
            with col1:
                st.image(image, caption=f"{file.name} - Asli", use_column_width=True)
            with col2:
                st.image(bw_image, caption=f"{file.name} - BW", use_column_width=True)
    else:
        st.info("Unggah gambar dulu di tab sebelumnya.")
        
with tab3:
    st.header("📊 Statistik & Analisis")
    if compression_data:
        total_ori = sum(f['original_size'] for f in compression_data)
        total_cmp = sum(f['compressed_size'] for f in compression_data)
        avg_ratio = total_ori / total_cmp if total_cmp else 0

        st.markdown(f"""
        - **Total file:** {len(compression_data)}  
        - **Ukuran asli total:** {total_ori:,} bytes  
        - **Ukuran terkompresi total:** {total_cmp:,} bytes  
        - **Rasio rata-rata:** {avg_ratio:.2f}  
        """)
        
        for f in compression_data:
            st.markdown(f"""
            **📄 {f['filename']}**
            - Ukuran asli: {f['original_size']:,} bytes  
            - Ukuran terkompresi: {f['compressed_size']:,} bytes  
            - Rasio: {f['compression_ratio']:.2f}
            - Penghematan: {(1 - f['compressed_size']/f['original_size'])*100:.2f}%
            """)
    else:
        st.info("Belum ada data yang dikompresi.")
