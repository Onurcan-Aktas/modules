import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """
    Sonsuz bir üreteç (generator) oluşturur. Her next() çağrısında 
    rastgele bir oyuncu ve rastgele bir eylem seçip tuple olarak döndürür.
    """
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "use", "release"
    ]

    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        # yield, return'den farklı olarak fonksiyonun durumunu hafızada tutar
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    """
    Verilen listeyi alır, içinden rastgele bir eleman seçip listeden çıkartır 
    ve yield ile döndürür. Liste tamamen boşalana kadar devam eder.
    """
    while len(events) > 0:
        # Listeden rastgele bir indeks belirle ve o indeksteki elemanı çıkart (pop)
        idx: int = random.randrange(len(events))
        event: tuple[str, str] = events.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    # Üreteci başlatıyoruz (henüz hiçbir şey üretmedi, sadece hazırda bekliyor)
    stream = gen_event()

    # 1. 1000 kez döngüye gir ve next() ile on-demand (isteğe bağlı) veri çek
    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    # 2. Üreteçten 10 yeni event daha çekerek sabit bir listeye (memory) kaydet
    event_list: list[tuple[str, str]] = []
    for _ in range(10):
        event_list.append(next(stream))

    print(f"Built list of 10 events: {event_list}")

    # 3. İkinci üreteci doğrudan 'for .. in ..' yapısı içinde kullan
    for consumed_event in consume_event(event_list):
        print(f"Got event from list: {consumed_event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()