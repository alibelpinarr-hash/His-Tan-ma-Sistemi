import streamlit as st
from transformers import pipeline

# 1. SAYFA AYARLARI VE BAŞLIK
st.set_page_config(page_title="Yapay Zeka Destekli Emoji Önerici", page_icon="🧠", layout="centered")

st.title("🧠 Cümle Anlamına Göre Emoji Öneri Sistemi")
st.write("Yazdığınız cümlenin duygusunu analiz eden ve ona en uygun emojileri öneren yapay zeka uygulaması.")
st.markdown("---")

# 2. YAPAY ZEKA MODELİNİN YÜKLENMESİ (Önbelleğe alınıyor ki her seferinde tekrar yüklenmesin)
@st.cache_resource
def model_yukle():
    # Türkçe duygu analizi (sentiment analysis) için eğitilmiş hazır bir BERT modeli kullanıyoruz
    return pipeline("text-classification", model="savasy/bert-base-turkish-sentiment-analysis")

try:
    classifier = model_yukle()
except Exception as e:
    st.error("Yapay zeka modeli yüklenirken bir hata oluştu. Lütfen internet bağlantınızı kontrol edin.")
    classifier = None

# 3. KULLANICI GİRİŞ ALANI
user_input = st.text_input(
    label="Analiz edilecek cümleyi giriniz:", 
    placeholder="Bugün hava harika, içim kıpır kıpır...",
    max_chars=200
)

# 4. DUYGUYA GÖRE EMOJİ EŞLEŞTİRME SÖZLÜĞÜ
# Yapay zekadan gelen 'positive' veya 'negative' sonucuna göre gösterilecek emojiler
emoji_sozlugu = {
    "positive": {
        "Duygu": "Pozitif / Mutlu 😊",
        "Emojiler": ["😊", "✨", "☀️", "🎉", "🔥", "🚀", "💖", "🍀"],
        "Mesaj": "Harika! Cümleniz pozitif ve enerji dolu bir anlam taşıyor."
    },
    "negative": {
        "Duygu": "Negatif / Üzgün 😔",
        "Emojiler": ["😔", "🌧️", "💔", "🥀", "🔋", "⌛", "🩹", "💭"],
        "Mesaj": "Cümlenizde biraz hüzün, yorgunluk veya negatif bir hava sezdim."
    },
    "notr": {
        "Duygu": "Nötr / Belirsiz 😐",
        "Emojiler": ["😐", "📝", "🔍", "💼", "☕", "📌", "🌐"],
        "Mesaj": "Cümleniz net bir duygu içermiyor, daha çok bilgi verici veya stabil."
    }
}

# 5. BUTONA BASILDIĞINDA ÇALIŞACAK MANTIK
if st.button("Uygula ve Emoji Öner"):
    if not user_input.strip():
        st.warning("Lütfen boş bırakmayınız, bir cümle yazınız.")
    elif classifier is None:
        st.error("Yapay zeka modeli şu anda aktif değil.")
    else:
        with st.spinner("Yapay zeka cümleyi analiz ediyor..."):
            # Yapay zeka modeline cümleyi gönderiyoruz
            sonuc = classifier(user_input)[0]
            etiket = sonuc['label'].lower()      # 'positive' veya 'negative' döner
            skor = sonuc['score']                # Yapay zekanın kendine olan güven oranı (0-1 arası)
            
            # Eğer yapay zeka %60'ın altında bir güven verdiyse cümleyi nötr kabul edelim
            if skor < 0.60:
                etiket = "notr"
                
            duygu_verisi = emoji_sozlugu[etiket]
            
            # Sonuçları ekrana basıyoruz
            st.success(f"**Tespit Edilen Duygu:** {duygu_verisi['Duygu']} (Doğruluk Payı: %{skor*100:.1f})")
            st.info(duygu_verisi['Mesaj'])
            
            # Emojileri büyük ve şık butonlar halinde yan yana listeleme
            st.write("### ⬇️ Sizin İçin Önerilen Emojiler ⬇️")
            st.markdown(f"<p style='font-size:40px; letter-spacing: 15px;'>{' '.join(duygu_verisi['Emojiler'][:5])}</p>", unsafe_allow_html=True)
            
            # Eğlenceli bir detay: Kopyalama kolaylığı
            st.text_input("Kopyalamak için tıklayın:", value=' '.join(duygu_verisi['Emojiler'][:5]))