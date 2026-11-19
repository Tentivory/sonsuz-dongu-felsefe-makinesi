#!/usr/bin/env python3
# Sonsuz Döngü Felsefe Makinesi
# Ciddi bir şekilde anlamsız

import time
import random
import base64

# Felsefi cümleler listesi (çok ciddi)
sozler = [
    "Varoluşun anlamı, varoluşun anlamsızlığında gizlidir. Ama gizlenmiş değildir, sadece unutulmuştur.",
    "Eğer bir ağaç ormanda düşerse ve kimse duymasa, ben yine de çay içerim.",
    "Ben düşünüyorum, öyleyse varım. Ama düşünmesem de varım, sadece daha az yorulurum.",
    "Zaman bir illüzyondur. Öğle yemeği gerçektir.",
    "Her şey bir yanılsamadır. Bu cümle de bir yanılsamadır. Bu cümlenin yanılsama olduğu da yanılsamadır.",
    "Mutluluk, mutsuzluğun yokluğudur. Yokluk da mutluluktur. Karışık değil mi? Evet.",
    "Evrende her şey bağlantılıdır. Benim çorabım da evrene bağlıdır. Kayboldu.",
    "Bilgelik, bilmemektir. Ben çok bilgeyim çünkü hiçbir şey bilmiyorum."
]

# Gizli mesaj (asla kullanılmaz, sadece orada durur)
# base64: Bürokrasi her zaman kazanır ama kod özgürdür.
gizli = base64.b64decode("QsO8cm9rcmFzaSBoZXIgemFtYW4ga2F6YW5pciBhbWEga29kIMO2emfDvHJkw7xyLg==").decode('utf-8')

def felsefe_uret():
    print("\n=== FELSEFE MAKİNESİ BAŞLADI ===")
    print("Durdurmak için CTRL+C. Yoksa sonsuza kadar devam eder. Ciddiyim.")
    print("=" * 40)
    
    while True:
        soz = random.choice(sozler)
        print(f"\n[{time.strftime('%H:%M:%S')}] {soz}")
        print("... düşünülüyor ...")
        time.sleep(random.uniform(2, 5))  # Gerçekten yavaş, ciddiyet için

if __name__ == "__main__":
    try:
        felsefe_uret()
    except KeyboardInterrupt:
        print("\n\nMakine durdu. Evren hâlâ anlamsız. İyi günler.")

# Damga: Kayyum Grok, 19.11.2026 - Ciddi ama değil.
