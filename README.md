Plik solution_public.py zawiera kod programu opartego na API OpenAI, który pobiera treść podaną w pliku .txt, obudowuje ją w tagi HTML zgodnie z instrukcjami przekazanymi mu w zmiennej prompt oraz zapisuje powstały kod HTML w pliku artykul.html.
Program został skalibrowany dla przypadku szczegółowego, który dotyczył pliku dostępnego online, w związku z czym nie jest uniwersalny. Wykorzystanie go dla pliku .txt offline wymagałoby zmiany kodu sekcji odczytu treści pliku, np. na instrukcję open.
Plik zadanie dla JJunior AI Developera - tresc artykulu.txt stanowi kopię treści domyślnego pliku wejściowego programu solution_public.py, którym pozostaje plik .txt dostępny online o tej samej nazwie.
Ze względów bezpieczeństwa, z kodu usunięto klucz do API OpenAI. Przed uruchomieniem programu należy wprowadzić klucz do kodu jako wartość zmiennej api_key.
Program wyznacza w treści dwa miejsca najwłaściwsze dla zamieszczenia ilustracji w wypadku, gdyby treść miała zostać opublikowana jako artykuł, i oznacza je znacznikami <img src="image_placeholder.jpg" />. Każdy ze znaczników otrzymuje atrybut alt - ich wartości przechowują odpowiednio zmienne prompt1 i prompt2.
Są to przykładowe prompty ilustracji, które można by wygenerować w celu zamieszczenia w budowanym artykule. Oba prompty zostały wygenerowane przez ChatGPT na podstawie treści akapitów z pliku domyślnego, stąd oczywiście raczej nie będą właściwe, jeśli program zostanie zastosowany dla innego pliku. Inna może być również liczba miejsc, które program w takim wypadku oznaczy. W udostępnionej formie zmienne te należy traktować jako część domyślnego przypadku użycia.
Byłoby możliwe rozbudowania programu solution_public.py, aby generował te prompty samodzielnie. Nie zostało to zrobione, aby uniknąć przesadnej złożoności aplikacji, która mogłaby odbić się na jej efektywności.
Program dołącza do ilustracji również podpisy przechowywane w zmiennych podpis1 i podpis2. Podpisy sformułował autor kodu, gdyż próby wygenerowania w ramach programu obniżały jego efektywność i zwracały wyniki zbyt podobne do nagłówków z treści pliku domyślnego. Jest to logiczna konsekwencja metodyki działania programu CLIP, który kojarzy tekst z obrazem - jeżeli tekst powstał na podstawie obrazu, który powstał na podstawie tekstu, optymalnym użyciem zasobów jest wykorzystanie tej samej ścieżki skojarzenia, która już zadziałała, tylko w przeciwną stronę.
Plik artykul.html zawiera wynik pracy programu uzyskany przez jego autora. Uruchomienie programu dla domyślnego pliku (po uzupełnieniu klucza) powinno utworzyć plik o tożsamej nazwie i identycznej lub zbliżonej treści - przykładowo program może wykorzystać tag article zamiast tagu section obecnego w udostępnionym pliku.
