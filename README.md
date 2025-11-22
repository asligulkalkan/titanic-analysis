# Titanic Veri Analizi Raporu 🚢📊  

Projem, Tech İstanbul Python Bootcamp bitirme projesidir.
Bu proje, **Pandas**, **NumPy** ve **Seaborn** kullanılarak Titanic veri seti üzerinde temel veri analizi, veri temizleme ve görselleştirme işlemlerini içermektedir.  
Amaç; cinsiyet ve yolcu sınıfına göre hayatta kalma oranlarını incelemek ve bilet ücretleri ile Pclass arasındaki ilişkiyi ortaya koymaktır.

## 🔧 Kullanılan Teknolojiler
- Python   
- Pandas  
- NumPy  
- Seaborn  
- Matplotlib  

## 📥 1. Veri Seti Hazırlama  
`data/` klasöründe Kaggle lisansı nedeniyle veri bulunmaz. Projeyi denerken bu klasöre ilgili datseti ekleyebilirsiniz.

##  2. Veri Temizleme  
Kod içinde:

- Eksik **Age** değerleri **median** ile doldurulur.
- Gerekli sütunlar kontrol edilir.
- Veri özet istatistikleri `summary_stats.csv` olarak kaydedilir.

## 📊 3. Cinsiyet & Pclass’a Göre Hayatta Kalma Oranları

Titanic veri setinde her yolcu için:
- Sex: erkek / kadın
- Pclass: 1, 2 veya 3. sınıf
- Survived: 1 = hayatta kaldı, 0 = kalamadı
bilgileri bulunuyor.

Bu proje, **“Hangi cinsiyet ve hangi sınıfta hayatta kalma oranı daha yüksek?”** sorusunu cevaplamak için yapılmıştır.

Bunun için şu işlem yapıldı:
df.groupby(["Sex", "Pclass"])["Survived"].mean()

Bu kodun yaptığı şeyi açıklayacak olursam :

1. Yolcuları önce **cinsiyete göre** ayırır  
2. Sonra her grubu **sınıfına göre** tekrar ayırır  
3. Her grupta **Survived değerlerinin ortalamasını alır**

**Neden ortalamayı alıyoruz?**  
  Çünkü Survived sütunu sadece 0 ve 1 değerlerinden oluşuyor. Bu yüzden ortalama, hayatta kalma oranı anlamına geliyor.


## 📈 4. Üretilen Grafikler
Seaborn ile grafikler üretilir. Sonuçlar `outputs/` klasörüne otomatik kaydedilir.

- **Cinsiyete Göre Hayatta Kalma** — Countplot  
  Kadın ve erkeklerin kaçının hayatta kaldığını gösteren bir grafik.

- **Pclass – Fare** — Boxplot  
  Yolcu sınıfı ile bilet fiyatlarının nasıl değiştiğini gösteren bir grafik.  
  Genelde 1. sınıf daha pahalı , 3. sınıf daha ucuz.

## 🧠 5. Grafiklere Göre Yorumlar

Bu iki grafikten şunlar çıkarılabilir:

- Kadınlar erkeklere göre çok daha fazla kurtulmuş.

- 1.sınıf yolcuların biletleri en pahalı; 3. sınıf yolcularınki ise en ucuz.

Bu da Titanic gemisindeki:

- toplumsal kurtarma önceliğini (“kadınlar ve çocuklar önce”)

- sınıfsal farkları (zengin–fakir ayrımı)

görsel olarak anlamamızı sağlar.

