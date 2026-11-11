import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    # Envanteri tutacağımız boş bir sözlük (dictionary)
    # Anahtarlar (eşya isimleri) metin, değerler (miktarlar) tam sayı olacak
    inventory: dict[str, int] = {}

    # sys.argv[1:] ile betik adını atlayıp doğrudan parametreleri alıyoruz
    for arg in sys.argv[1:]:
        # Gelen argümanı ':' karakterinden ikiye bölüyoruz
        parts: list[str] = arg.split(':')
        
        # Eğer parametre içinde ':' yoksa veya formata uymazsa (örn: "hello")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name: str = parts[0]
        qty_str: str = parts[1]

        # Eşya zaten envanterde var mı kontrolü (Mükerrerlik)
        if item_name in inventory.keys():
            print(f"Redundant item '{item_name}' - discarding")
            continue

        # Miktarı tam sayıya (integer) çevirmeyi dene
        try:
            quantity: int = int(qty_str)
            inventory[item_name] = quantity
        except ValueError as e:
            # Örneğin harf girildiyse ('value' gibi), hatayı yakala ve yazdır
            print(f"Quantity error for '{item_name}': {e}")

    # 1. Envanteri olduğu gibi ekrana yazdır
    print(f"Got inventory: {inventory}")

    # 2. Envanterdeki tüm eşya isimlerinin bir listesini oluştur ve yazdır
    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    # 3. Tüm eşyaların sayısını ve toplam miktarını hesapla
    num_items: int = len(inventory)
    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {num_items} items: {total_qty}")

    # Toplam miktar 0'dan büyükse, her eşyanın yüzdesini hesapla
    # (Sıfıra bölünme - ZeroDivisionError - hatasını engellemek için kontrol ekliyoruz)
    if total_qty > 0:
        for item in item_list:
            qty: int = inventory[item]
            # Miktarı toplam değere bölüp 100 ile çarpıyoruz. 
            # 1 ondalık basamağa kadar (örnekteki gibi) round ile yuvarlıyoruz
            percent: float = round((qty / total_qty) * 100, 1)
            print(f"Item {item} represents {percent}%")

    # Envanter boş değilse en az ve en çok olan eşyaları bul
    if num_items > 0:
        most_item: str = item_list[0]
        least_item: str = item_list[0]
        most_qty: int = inventory[most_item]
        least_qty: int = inventory[least_item]

        for item in item_list:
            item_qty: int = inventory[item]
            
            if item_qty > most_qty:
                most_qty = item_qty
                most_item = item
                
            if item_qty < least_qty:
                least_qty = item_qty
                least_item = item

        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")

    # Son olarak update() metodu ile envantere yeni bir öğe ekle
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()