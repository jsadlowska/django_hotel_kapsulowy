## OPIS PROJEKTU

Aplikacja rezerwacyjna hotelu kapsułowego stworzona jako projekt dyplomowy studiów podyplomowych na kierunku Python Developer 
w WSB Merito Gdańsk. Umożliwia użytkownikom rejestrację, logowanie oraz rezerwację kapsuł w hotelu kapsułowym.
Autorem projektu jest Justyna Sadłowska, a promotorem Igor Klepuszewski.

## FUNKCJONALNOŚCI:

        - Rejestracja użytkowników
        - Logowanie i wylogowywanie użytkowników
        - Przeglądanie dostępnych kapsuł
        - Rezerwacja kapsuł przez zalogowanych użytkowników
        - Anulowanie rezerwacji

## TECHNOLOGIE:

        - Python
        - Django
        - SQLite 
        - HTML/CSS

## INSTALACJA:

1. Sklonuj repozytorium:
   
        git clone https://github.com/jsadlowska/django_hotel_kapsulowy.git
        cd django_hotel_kapsulowy
    
3. Stwórz wirtualne środowisko i zainstaluj zależności:

        python -m venv venv
        source venv/bin/activate  # Na Windows: venv\Scripts\activate
        pip install -r requirements.txt

4. Wykonaj migracje bazy danych:

        python manage.py migrate

5. Uruchom serwer deweloperski:

        python manage.py runserver
  
## KONFIGURACJA

1. Stwórz plik `.env` w głównym katalogu projektu i dodaj poniższe ustawienia:

        SECRET_KEY='twoj_sekret_klucz'
        DEBUG=True
        ALLOWED_HOSTS=localhost, 127.0.0.1
        DATABASE_URL=sqlite:///db.sqlite3
 

2. Skonfiguruj inne ustawienia w pliku `settings.py` według własnych potrzeb.

## URUCHAMIANIE:

1. Upewnij się, że wirtualne środowisko jest aktywne:
    
       source venv/bin/activate  # Na Windows: venv\Scripts\activate
    

2. Uruchom serwer deweloperski:
    
        python manage.py runserver
    

3. Otwórz przeglądarkę i przejdź na adres `http://localhost:8000`.

   
