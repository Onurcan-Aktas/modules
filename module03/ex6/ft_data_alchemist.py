import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    # 1. Başlangıç listesi (Bazı isimler küçük, bazıları büyük harfle başlıyor)
    players: list[str] = [
        'alice', 'Bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'Kevin', 'Liam'
    ]
    print(f"Initial list of players: {players}")

    # 2. List Comprehension: Tüm isimleri büyük harfle başlatarak yeni liste
    cap_all: list[str] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {cap_all}")

    # 3. List Comprehension: Sadece ilk hali büyük harfle başlayanları filtrele
    cap_only: list[str] = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {cap_only}\n")

    # 4. Dict Comprehension: Büyük harfli isimleri anahtar (key), 
    # 1-1000 arası rastgele sayıları değer (value) olarak belirleyip sözlük yap
    scores: dict[str, int] = {p: random.randint(1, 1000) for p in cap_all}
    print(f"Score dict: {scores}")

    # 5. Sözlükteki değerlerin (skorların) ortalamasını bul
    avg: float = sum(scores.values()) / len(scores)
    # Çıktıdaki gibi 2 ondalık basamağa yuvarlıyoruz
    print(f"Score average is {round(avg, 2)}")

    # 6. Dict Comprehension: Sadece ortalamadan yüksek skoru olanları filtrele
    high_scores: dict[str, int] = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()