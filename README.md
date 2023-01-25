# Projekt ZTM - Detekcja zanieczyszczeń na obszarach zielonych ze zdjęć wykonanych dronem
*PJATK - ZTM - Wykorzystanie ML/AI w Multimediach*

Autorzy:
- Serhii Krasnoiarskyi (s18943)
- Witold Kurpiewski (s16687)
- Jan Masny (s23453)
- Patryk Pajączkowski (s17009)
- Jacek Spaliński (s26557)

Elementy wchodzące w skład projektu:
- Dokumentacja prototypu projektu
- Demo PoC (pokazanie część funkcjonalności prototypu)
- Prezentacja wyników projektu

### Dokumentacja prototypu projektu

#### Opis problemu
Zanieczyszczenie środowiska jest realnym problemem, z którym obecnie musi mierzyć się społeczeństwo. Problem ten w 
jakimś stopniu dotyka każdego państwa na świecie. Co więcej, jest to problem z kategorii problemów 'wspólnych', ponieważ
zanieczyszczenie środowiska nie zna granic i w długiej perspektywie może wpływać na obniżenie się jakości życia 
wszystkich ludzi na świecie, niezależnie od płci, wieku czy kultury, z której pochodzą. Temat ten jest ściśle związany z
tak dobrze nam znaną ekologią.

Jednym z częstych problemów występujących w Polsce jest nielegalne pozbywania się odpadów komunalnych w miejscach
do tego nieprzeznaczonych. Śmieci często trafiają na teren obszarów zielonych, takich jak lasy, łąki czy 
miejskie trawniki. Powoduje to zanieczyszczenie środowiska, ponieważ większość śmieci rozkłada się w naturze przez setki
lat. Tworzy to szereg zagrożeń dla klimatu takich jak...

#### Proponowane rozwiązanie
W celu zredukowania zanieczyszczenia środowiska chcielibyśmy zaproponować rozwiązanie w postaci algorytmu detekcji
śmieci na podstawie wideo/zdjęć przesłanych przez drona skanującego obszary zielone. Wykorzystując bardzo wysoką 
mobilność dronów można by przeskanować wiele obszarów zielonych w poszukiwaniu pozostawionych tam śmieci. Następnie na
podstawie lokalizacji śmieci, odpowiednie ekipy sprzątającej mogłby zostać tam wysłane w celu uprzątniecia śmieci
zanim zanieczyszczenia przedostaną się do środowiska.


#### Opis użytkowników, rynku i konkurencji
Użytkownikami byłoby całe społeczeństwo, ponieważ rozwiązania z obszaru ekologii wpływają pozytywnie na jakość życia
wszystkich z nas.

Rynek i konkurencja:
...



#### Uzasadnienie inwestycji (np. innowacyjność i oszczędność)
Oszczędność:
- skanowanie terenów zielonych przez drona jest szybsze niż w wykonaniu człowieka, a zatem oszczędza się czas. 
Zaoszczędzony czas to zaoszczędzone pieniądze.

Innowacja:
- automatyzacja procesu sprzątania obszarów zielonych

#### Wymagane komponenty i ich koszt
Komponenty:
- Wykorzystanie algorytmu DL do detekcji dronów
- 'Armia' dronów
- Stacje dokujące i serwisowe
- Po przeskanowaniu obszaru: zatrudnienie firmy mogącej posprzątać odpady
Koszt:
<należy policzyć koszt komponentów - dodać jakieś założenia>
#### Kryteria sukcesu
- rozpoznawanie śmieci ze zdjęć (a później z filmów)
- mniej zanieczyszczeń na obszarach zielonych
- poprawa kondycji środowiska naturalnego
- znalezienie częstych punktów nielegalnego składowania śmieci (można zniwelować instalując kamery)

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
![]()

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

<placeholder na link do końcowej prezentacji>

### Bibliografia i publikacje w prasie
- https://www.matec-conferences.org/articles/matecconf/pdf/2018/91/matecconf_eitce2018_01056.pdf
- https://www.rmf24.pl/fakty/polska/news-walka-z-nielegalnymi-wysypiskami-smieci-fotopulapki-w-nadarz,nId,5465495#crp_state=1
- https://www.lasy.gov.pl/pl/informacje/aktualnosci/smieci-ciaglym-problemem-w-lasach
