from book import Book
from library import Library

def menu():
    print("\n--- Kütüphane Yönetim Sistemi ---")
    print("1. Kitap Ekle (Manuel)")
    print("2. Kitap Ekle (ISBN ile - API'den çek)")
    print("3. Kitap Sil")
    print("4. Kitapları Listele")
    print("5. Kitap Ara")
    print("6. Çıkış")

def main():
    lib = Library()

    while True:
        menu()
        choice = input("Seçiminiz: ")

        if choice == "1":
            title = input("Kitap adı: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            try:
                lib.add_book(Book(title, author, isbn))
                print("✅ Kitap eklendi.")
            except ValueError as e:
                print(f"⚠️ {e}")

        elif choice == "2":
            isbn = input("ISBN: ")
            try:
                book = lib.add_book_by_isbn(isbn)
                print(f"✅ Eklendi: {book}")
            except ValueError as e:
                print(f"⚠️ {e}")

        elif choice == "3":
            isbn = input("Silinecek ISBN: ")
            lib.remove_book(isbn)
            print("✅ Kitap silindi.")

        elif choice == "4":
            for b in lib.list_books():
                print(b)

        elif choice == "5":
            isbn = input("Aranacak ISBN: ")
            book = lib.find_book(isbn)
            print(book if book else "❌ Kitap bulunamadı.")

        elif choice == "6":
            print("👋 Çıkış yapılıyor...")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()
