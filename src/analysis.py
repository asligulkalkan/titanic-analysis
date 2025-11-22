import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Klasör yolları
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "titanic.csv")
OUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    # 1) Veri yükleme
    if not os.path.exists(DATA_PATH):
        print(f"[HATA] Veri dosyası bulunamadı: {DATA_PATH}")
        print("Lütfen 'data/titanic.csv' dosyasını yerleştirip tekrar deneyin.")
        sys.exit(1)

    df = pd.read_csv(DATA_PATH)

    # Gerekli sütunlar kontrolü
    required = {"Survived", "Sex", "Pclass", "Age", "Fare"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Gerekli sütun(lar) eksik: {missing}\n"
                         f"Mevcut sütunlar: {list(df.columns)}")

    # 2) Eksik Age değerlerini medyan ile doldurma
    age_median = df["Age"].median()
    df["Age"] = df["Age"].fillna(age_median)

    # 3) Cinsiyet & Sınıfa göre hayatta kalma oranları (groupby)
    survival_rates = (
        df.groupby(["Sex", "Pclass"])["Survived"]
          .mean()
          .reset_index()
          .sort_values(["Sex", "Pclass"])
    )
    survival_rates.to_csv(os.path.join(OUT_DIR, "survival_rates_by_sex_pclass.csv"), index=False)

    # 4) Özet istatistikleri kaydet (isteğe bağlı ama faydalı)
    df.describe(include="all").to_csv(os.path.join(OUT_DIR, "summary_stats.csv"))

    # 5) Görseller — Seaborn ile
    # A) Cinsiyete göre hayatta kalma (countplot)
    plt.figure()  # her grafik için ayrı figür
    sns.countplot(data=df, x="Sex", hue="Survived")
    plt.title("Cinsiyete Göre Hayatta Kalma (Seaborn Countplot)")
    plt.xlabel("Cinsiyet")
    plt.ylabel("Kişi Sayısı")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "countplot_sex_survived.png"))
    plt.close()

    # B) Pclass ve Fare ilişkisi (boxplot)
    plt.figure()
    sns.boxplot(data=df, x="Pclass", y="Fare")
    plt.title("Pclass - Fare (Seaborn Boxplot)")
    plt.xlabel("Yolcu Sınıfı (Pclass)")
    plt.ylabel("Bilet Ücreti (Fare)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "boxplot_pclass_fare.png"))
    plt.close()

    # 6) Kısa rapor
    lines = []
    lines.append("# Titanic Veri Analizi Raporu\n")
    lines.append(f"- Gözlem sayısı: **{len(df)}**")
    lines.append(f"- Age median doldurma değeri: **{age_median:.2f}**\n")
    lines.append("## Cinsiyet & Sınıfa Göre Hayatta Kalma Oranları (İlk satırlar)\n")
    lines.append(survival_rates.head().to_markdown(index=False))
    lines.append("\n## Gözlemler (Örnek)\n")
    lines.append("- Countplot: Kadınların hayatta kalma oranı genelde daha yüksektir.")
    lines.append("- Boxplot: Sınıf yükseldikçe (1 daha iyi sınıf), bilet ücretlerinin medyanı yükselir.")
    with open(os.path.join(OUT_DIR, "report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("[OK] Analiz tamamlandı. Çıktılar 'outputs/' klasörüne kaydedildi.")

if __name__ == "__main__":
    main()

