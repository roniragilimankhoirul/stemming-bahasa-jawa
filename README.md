# Stemming Bahasa Jawa

Aplikasi berbasis Python ini dirancang untuk melakukan _stemming_ pada teks Bahasa Jawa. _Stemming_ adalah proses yang digunakan untuk mencari kata dasar dari sebuah kata dengan menghilangkan afiks dan infleksi yang ada. Aplikasi ini memanfaatkan library PySastrawi dan Deep-Translator untuk memastikan hasil stemming yang akurat dan efisien dalam konteks Bahasa Jawa.

## Cara Kerja

Aplikasi ini berkerja dengan cara, inputan pengguna dalam Bahasa Jawa akan diubah menjadi Bahasa Indonesia dengan Deep-Translator. Kemudian Pysastrawi akan melakukan _stemming_ pada hasil dari terjemahan tadi. Setelah itu, hasil _stemming_ tersebut akan diubah kembali menjadi Bahasa Jawa menggunakan Deep-Translator

## Petunjuk Penggunaan

1. Download _repository_

   ```
   git clone https://github.com/roniragilimankhoirul/stemming-bahasa-jawa.git
   ```

2. Pindah _directory_

   ```
   cd stemming-bahasa-jawa/
   ```

3. Buat _virtual environmet_. Untuk lebih lengkapnya bisa klik kunjungi link [ini](https://www.petanikode.com/python-virtualenv/)

   ```
   python -m env nama-folder
   ```

4. Mengaktifkan _virtual environment_

   - linux
     ```bash
     source nama-folder/bin/activate
     ```
   - windows

     ```bash
     nama-folder/bin/activate
     ```

5. Install _dependencies_

   ```
   pip install -r requirements.txt
   ```

6. Menjalankan aplikasi

   - GUI
     ```bash
     python gui.py
     ```
   - non-GUI

     ```bash
     python non-gui.py
     ```
