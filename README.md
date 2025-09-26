# Proyek Analisis & Dashboard Jaya jaya Institut

Dokumentasi ini merangkum proyek analisis data untuk mengidentifikasi faktor-faktor yang memengaruhi status kelulusan mahasiswa di Jaya Jaya Institut dan menyajikan hasilnya dalam sebuah dasbor analitis.

-----

## 1\. Dokumentasi Proyek

### Latar Belakang

**Jaya Jaya Institut** adalah sebuah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Dengan reputasi yang baik dalam mencetak lulusan berkualitas, institusi ini telah menjadi salah satu pilihan utama bagi calon mahasiswa. Namun, di balik keberhasilannya, Jaya Jaya Institut menghadapi tantangan internal yang signifikan terkait retensi mahasiswa.

### Permasalahan Bisnis

Permasalahan utama yang dihadapi oleh institusi adalah **tingkat *dropout* (putus studi) mahasiswa yang tinggi**. Masalah ini menimbulkan beberapa dampak negatif, antara lain:

1.  **Menurunkan Reputasi:** Angka *dropout* yang tinggi dapat merusak citra dan reputasi institusi di mata calon mahasiswa dan pemangku kepentingan.
2.  **Kerugian Finansial:** Setiap mahasiswa yang putus studi merupakan potensi kehilangan pendapatan dan pemborosan sumber daya yang telah dialokasikan.
3.  **Kurangnya Sistem Peringatan Dini:** Institusi belum memiliki cara yang sistematis untuk mengidentifikasi mahasiswa yang berisiko *dropout* sejak dini, sehingga intervensi yang dilakukan cenderung reaktif dan terlambat.

### Cakupan Proyek

Proyek ini bertujuan untuk mengatasi permasalahan di atas dengan cakupan sebagai berikut:

  * **Analisis Data Eksploratif (EDA):** Melakukan analisis mendalam terhadap dataset historis mahasiswa untuk menemukan pola dan faktor-faktor kunci yang berkorelasi dengan status kelulusan (`Graduate`, `Dropout`, `Enrolled`).
  * **Pengembangan Model Machine Learning:** Membangun dan melatih model klasifikasi untuk memprediksi status kelulusan mahasiswa. Prototipe dari model ini diimplementasikan dalam sebuah aplikasi web sederhana.
  * **Pembuatan Dasbor Analitis:** Merancang dan membangun dasbor interaktif di Looker Studio yang berfungsi sebagai alat bantu bagi manajemen untuk memonitor data dan mendapatkan wawasan strategis.

### Dashboard Analitis

<img width="1158" height="869" alt="Screenshot 2025-09-26 165750" src="https://github.com/user-attachments/assets/29758a57-7c57-4e5c-be29-cb2811809ab5" />


Struktur dasbor dibagi menjadi tiga bagian utama:

1.  **Academic Snapshot:** Memberikan gambaran umum mengenai komposisi mahasiswa dan status kelulusan saat ini.
2.  **Key Driver Analysis:** Menganalisis dan membandingkan faktor-faktor kunci seperti nilai akademis dan status finansial untuk memahami penyebab *dropout*.
3.  **High-Impact Segments:** Menyorot segmen mahasiswa paling rentan berdasarkan kombinasi beberapa faktor, seperti program studi dan status beasiswa.

-----

## 2\. Action Items untuk Jaya Jaya Institut

Berdasarkan temuan dari analisis data, berikut adalah beberapa rekomendasi tindakan yang dapat diambil:

  * **Program Bantuan Keuangan Proaktif:**

      * **Masalah:** Status pembayaran biaya kuliah adalah prediktor kuat untuk *dropout*.
      * **Aksi:** Mengembangkan sistem untuk mengidentifikasi mahasiswa yang menunjukkan tanda-tanda kesulitan finansial **sebelum** mereka menunggak. Tawarkan skema pembayaran yang lebih fleksibel, konseling keuangan, atau program bantuan dana darurat bagi mereka yang paling membutuhkan.

  * **Program Mentoring Akademik Dini:**

      * **Masalah:** Mahasiswa dengan nilai penerimaan yang lebih rendah memiliki risiko lebih tinggi.
      * **Aksi:** Membuat program mentoring wajib di semester pertama bagi mahasiswa yang masuk dalam kuartil bawah nilai penerimaan. Pasangkan mereka dengan mahasiswa senior berprestasi atau dosen wali untuk bimbingan akademik dan adaptasi kampus.

  * **Evaluasi Kurikulum pada Program Studi Berisiko:**

      * **Masalah:** Beberapa program studi secara konsisten menghasilkan angka *dropout* yang lebih tinggi.
      * **Aksi:** Melakukan evaluasi mendalam terhadap kurikulum, metode pengajaran, dan sistem dukungan mahasiswa pada program-program studi yang teridentifikasi berisiko tinggi untuk menemukan dan mengatasi akar permasalahannya.

-----

## 3\. Cara Menjalankan Sistem

Sistem ini terdiri dari dua bagian: *notebook* untuk analisis dan aplikasi Streamlit untuk *prototype* model prediktif.

### Prasyarat

  * Python 3.12.0 atau lebih baru
  * Pip

### Langkah-langkah Instalasi

1.  **Clone atau Unduh Proyek**
    Buka terminal atau Git Bash dan jalankan:

    ```bash
    git clone https://github.com/Rifky813/Submission-Akhir_Penerapan-Data-Science.git
    cd Submission-Akhir_Penerapan-Data-Science
    ```

2.  **Buat Lingkungan Virtual**
    Sangat disarankan untuk membuat lingkungan virtual agar tidak mengganggu instalasi Python utama.

    ```bash
    python -m venv venv
    ```

3.  **Aktifkan Lingkungan Virtual**

      * **Windows:**
        ```cmd
        .\venv\Scripts\activate
        ```
      * **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependensi**
    Install semua *library* yang dibutuhkan dari file `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

### Menjalankan Aplikasi Streamlit

Setelah instalasi selesai, jalankan aplikasi dengan perintah berikut di terminal:

```bash
python -m streamlit run app.py
```

Aplikasi akan otomatis terbuka di browser.

### Mengakses Dasbor Looker Studio dan Streamlit app

* Link streamlit: https://rifkyyudistiansyah-dashboard-jayajaya.streamlit.app/ 
* Link Looker Studio: https://lookerstudio.google.com/s/m61s1HhPiOs
