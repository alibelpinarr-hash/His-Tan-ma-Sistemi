# His-Tan-ma-Sistemi
Yazdığım cümlenin anlamına göre bir emoji üreten uygulama.

Bu proje, kullanıcının girdiğinde yazdığı Türkçe cümlelerin duygu analizini (Sentiment Analysis) doğal dil işleme modelleriyle yaparak, cümlenin anlamına ve ruh haline en uygun emojileri öneren bir web uygulamasıdır.

**Dönem Projesi Geliştiricisi:** [Adınız Soyadınız]  
**Ders:** Yapay Zeka Destekli Yazılım Geliştirme (Vize Dönem Projesi)

---

## 🚀 Projenin Amacı ve Özellikleri
- **Doğal Dil İşleme (NLP):** Arkada çalışan `savasy/bert-base-turkish-sentiment-analysis` BERT tabanlı yapay zeka modeli sayesinde Türkçe cümleleri yüksek doğrulukla analiz eder.
- **Dinamik Emoji Eşleştirme:** Cümlenin pozitif, negatif veya nötr olma durumuna göre kullanıcıya kopyalanabilir hazır emojiler sunar.
- **Kullanıcı Dostu Arayüz:** Streamlit kütüphanesi kullanılarak sade, modern ve hızlı bir web arayüzü tasarlanmıştır.

## 🛠️ Kullanılan Teknolojiler
- **Programlama Dili:** Python 3.9+
- **Yapay Zeka Kütüphaneleri:** Hugging Face (Transformers), PyTorch
- **Arayüz (Frontend/Backend):** Streamlit

## 💻 Kurulum ve Çalıştırma

Projeyi yerelde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Bu depoyu bilgisayarınıza indirin veya klonlayın.
2. Terminali açarak gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
