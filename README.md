![](https://github.com/s18943/Trash_detection_ZTM/blob/main/raw/pjatk_logo.png)

# Detekcja składowisk odpadów na podstawie zdjęć z dronów z użyciem modeli uczenia maszynowego
*PJATK - ZTM - Wykorzystanie ML/AI w Multimediach*

Autorzy:
- Valeria Arovina (s19316)
- Witold Kurpiewski (s16687)
- Jan Masny (s23453)
- Patryk Pajączkowski (s17009)
- Serhii Krasnoiarskyi (s18943)
- Jacek Spaliński (s26557)

Elementy wchodzące w skład projektu:
- Dokumentacja prototypu projektu
- Demo PoC (pokazanie część funkcjonalności prototypu)
- Prezentacja wyników projektu

### Dokumentacja prototypu projektu

Dokumentacja projektu zawierająca:
- opis problemu
- proponowane rozwiązanie
- opis użytkowników, rynku i konkurencji
- uzasadnienie inwestycji
- spis wymaganych komponentów i ich kosztu
- kryteria sukcesu

znajduje się w pliku `Dokumentacja_Trash.pdf` w folderze `documentation`.

### Demo PoC
W ramach demo funkcjonalności prototypu dobrze by było, gdyby udało się zrobić:
- detekcję zanieczyszczeń ze zdjęć za pomocą DL
- zapis dodatkowych informacji o znalezionym zanieczyszczeniu
  - rodzaj np. puszka, opona, plastik
  - liczba znalezionych zanieczyszczeń
  - dokładność predykcji
  - (+ inne atrybuty, które poda sieć DL)
- wizualizację wyników np. mapę wyświetlającą miejsce znalezionego zanieczyszczenia
- prosty interfejs graficzny np. do wrzucania zdjęć do analizy

Potrzebne będą na pewno:
- zdjęcia śmieci na terenach zielonych. Wystarczy kilka.
  - najlepiej, gdyby były to zdjęcia 'od góry' z wysokości ok. 3m, no tak jakby z drona.
  
#### Detekcja zanieczyszczeń ze zdjęć za pomocą DL
Do detekcji możemy użyć np. Microsoft Azure Vision API, Google Cloud Vision lub innego rozwiązania open source.

Fajnie by było pokazać zdjęcie przed i po detekcji tzn. z tą ramką detekcji.

![](https://github.com/s18943/Trash_detection_ZTM/blob/main/raw/eg_trash_detection.jpg)

Prototyp rozwiązania został zrobiony przez Patryka w Google Cloudzie.

#### Zapis dodatkowych informacji o znalezionym zanieczyszczeniu
To samo co w Demo PoC. Fajnie by przechwycić i zapisać gdzieś znalezione informacje.

#### Mapa zawierająca miejsce znalezionego zanieczyszczenia
W wersji podstawowej mapę można wygenerować po prostu w notatniku .ipynb.

W wersji bardziej interaktywnej mapę można dodać do interfejsu graficznego.

#### Interfejs graficzny
W tym celu wykorzystać możemy:
- Streamlit - https://streamlit.io/
- Dash - https://dash.plotly.com/

### Prezentacja wyników projektu

Prezentacja wyników projektu znajduje się w pliku `Prezentacja_Trash.pdf` w folderze `documentation`.

*Enjoy!*
