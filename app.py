import streamlit as st
import pandas as pd
import pickle
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# --- FUNGSI UNTUK MEMUAT MODEL ---
@st.cache_data
def load_model():
    """Memuat pipeline model yang telah disimpan."""
    try:
        with open('CatBoost_pipeline.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("File model 'CatBoost_pipeline.pkl' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama.")
        return None

# --- MEMUAT MODEL ---
pipeline = load_model()

# --- JUDUL DAN DESKRIPSI APLIKASI ---
st.title("🎓 Aplikasi Prediksi Status Mahasiswa")
st.write(
    "Aplikasi ini menggunakan model **CatBoost** untuk memprediksi status kelulusan seorang mahasiswa "
    "menjadi salah satu dari tiga kategori: **Dropout, Enrolled, atau Graduate**. "
    "Silakan masukkan data di panel sebelah kiri."
)
st.markdown("---")


# --- INPUT PENGGUNA DI SIDEBAR ---
st.sidebar.header("Masukkan Data Mahasiswa")

marital_status_map = {0: "Lajang", 1: "Menikah", 2: "Janda/Duda", 3: "Bercerai", 4: "Dipisahkan secara hukum", 5: "Lainnya"}
course_map = {
    1: "Biofuel Production Technology", 2: "Animation and Multimedia Design", 3: "Social Service (evening attendance)",
    4: "Agronomy", 5: "Communication Design", 6: "Veterinary Nursing", 7: "Informatics Engineering",
    8: "Equiniculture", 9: "Management", 10: "Social Service", 11: "Tourism", 12: "Nursing",
    13: "Oral Hygiene", 14: "Advertising and Marketing Management", 15: "Journalism and Communication",
    16: "Basic Education", 17: "Management (evening attendance)"
}
gender_map = {1: "Pria", 0: "Wanita"}
scholarship_map = {1: "Ya", 0: "Tidak"}
tuition_map = {1: "Ya", 0: "Tidak"}

def user_input_features():
    st.sidebar.subheader("Informasi Pribadi")
    marital_status = st.sidebar.selectbox("Status Pernikahan", list(marital_status_map.values()))
    gender = st.sidebar.selectbox("Gender", list(gender_map.values()))
    age_at_enrollment = st.sidebar.slider("Umur saat Pendaftaran", 17, 70, 20)
    
    st.sidebar.subheader("Informasi Akademik")
    course = st.sidebar.selectbox("Program Studi", list(course_map.values()))
    scholarship_holder = st.sidebar.selectbox("Penerima Beasiswa?", list(scholarship_map.values()))
    tuition_fees_up_to_date = st.sidebar.selectbox("Biaya Kuliah Lunas?", list(tuition_map.values()))
    
    st.sidebar.subheader("Nilai Akademik")
    previous_qualification_grade = st.sidebar.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 120.0)
    admission_grade = st.sidebar.slider("Nilai Penerimaan", 0.0, 200.0, 125.0)
    gdp = st.sidebar.slider("GDP (Indikator Ekonomi)", -4.0, 4.0, 0.0)

    marital_status_num = [k for k, v in marital_status_map.items() if v == marital_status][0]
    course_num = [k for k, v in course_map.items() if v == course][0]
    gender_num = [k for k, v in gender_map.items() if v == gender][0]
    scholarship_holder_num = [k for k, v in scholarship_map.items() if v == scholarship_holder][0]
    tuition_fees_up_to_date_num = [k for k, v in tuition_map.items() if v == tuition_fees_up_to_date][0]

    data = {
        'Marital_status': marital_status_num,
        'Course': course_num,
        'Gender': gender_num,
        'Scholarship_holder': scholarship_holder_num,
        'Age_at_enrollment': age_at_enrollment,
        'Previous_qualification_grade': previous_qualification_grade,
        'Admission_grade': admission_grade,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date_num,
        'GDP': gdp
    }
    
    all_cols = ['Marital_status', 'Application_mode', 'Application_order', 'Course',
       'Daytime_evening_attendance', 'Previous_qualification',
       'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
       'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
       'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
       'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
       'Age_at_enrollment', 'International',
       'Curricular_units_1st_sem_credited',
       'Curricular_units_1st_sem_enrolled',
       'Curricular_units_1st_sem_evaluations',
       'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
       'Curricular_units_1st_sem_without_evaluations',
       'Curricular_units_2nd_sem_credited',
       'Curricular_units_2nd_sem_enrolled',
       'Curricular_units_2nd_sem_evaluations',
       'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
       'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate',
       'Inflation_rate', 'GDP']
    
    default_values = {
        'Application_mode': 1, 'Application_order': 1, 'Daytime_evening_attendance': 1, 
        'Previous_qualification': 1, 'Nacionality': 1, 'Mothers_qualification': 1, 
        'Fathers_qualification': 1, 'Mothers_occupation': 1, 'Fathers_occupation': 1,
        'Displaced': 0, 'Educational_special_needs': 0, 'Debtor': 0, 'International': 0,
        'Curricular_units_1st_sem_credited': 0, 'Curricular_units_1st_sem_enrolled': 10,
        'Curricular_units_1st_sem_evaluations': 10, 'Curricular_units_1st_sem_approved': 9,
        'Curricular_units_1st_sem_grade': 12.0, 'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0, 'Curricular_units_2nd_sem_enrolled': 10,
        'Curricular_units_2nd_sem_evaluations': 10, 'Curricular_units_2nd_sem_approved': 9,
        'Curricular_units_2nd_sem_grade': 12.0, 'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 12.0, 'Inflation_rate': 1.0
    }

    full_data = {**default_values, **data}
    features = pd.DataFrame(full_data, index=[0])
    features = features[all_cols]
    return features


if pipeline:
    # --- MENAMPILKAN INPUT DAN MEMBUAT TOMBOL PREDIKSI ---
    input_df = user_input_features()

    st.subheader("Data Mahasiswa yang Dimasukkan:")
    st.dataframe(input_df, use_container_width=True, hide_index=True)

    predict_button = st.button("🚀 Prediksi Status Mahasiswa", type="primary")
    st.markdown("---")

    # --- LOGIKA PREDIKSI DAN TAMPILAN HASIL ---
    if predict_button:
        with st.spinner("🧠 Model sedang berpikir..."):
            prediction = pipeline.predict(input_df)
            prediction_proba = pipeline.predict_proba(input_df)

            predicted_value = int(prediction[0])

            status_map = {0: 'Dropout', 1: 'Enrolled', 2: 'Graduate'}
            predicted_status = status_map[predicted_value]

            st.subheader("Hasil Prediksi:")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                if predicted_status == 'Dropout':
                    st.error(f"**Status: Berisiko TINGGI untuk {predicted_status}**")
                    st.write("Model memprediksi mahasiswa ini cenderung akan berhenti kuliah. Perlu perhatian dan bimbingan khusus.")
                elif predicted_status == 'Enrolled':
                    st.warning(f"**Status: Diprediksi masih dalam status {predicted_status}**")
                    st.write("Model memprediksi mahasiswa ini masih aktif dalam masa studi. Performa perlu terus dipantau.")
                else:
                    st.success(f"**Status: Cenderung akan {predicted_status}**")
                    st.write("Model memprediksi mahasiswa ini memiliki probabilitas tinggi untuk menyelesaikan pendidikannya dengan baik.")
            
            with col2:
                st.metric(label="Probabilitas Dropout", value=f"{prediction_proba[0][0]*100:.2f}%")
                st.metric(label="Probabilitas Enrolled", value=f"{prediction_proba[0][1]*100:.2f}%")
                st.metric(label="Probabilitas Graduate", value=f"{prediction_proba[0][2]*100:.2f}%")
            
            st.info(
                "**Catatan:** Prediksi ini didasarkan pada data historis dan tidak mutlak 100% akurat. "
                "Gunakan hasil ini sebagai alat bantu untuk identifikasi dini, bukan sebagai keputusan final."
            )
else:
    st.warning("Model tidak dapat dimuat. Aplikasi tidak dapat berjalan.")