# Iskalnik nepremicnin
Skripta napisana v Selenium-u, po želji partnerice(nepremičninske agentke) za lažje iskanje in vrednotenje nepremičnin.

Skripta izvozi podatke iskanja iz nepremicnine.net in ovrednoti nepremeičnino po povprečni vrednosi nepremičnin na trgu. Vse skupaj izvozi v excell.

## Instalacija in uporaba
Predpogoji: instaliran python in pip, ter chromedriver.exe
Pred prvo uporabo zaženite `requirements.txt`:
```
pip install requirements.txt
```
in v `main.py` spremenite `PATH` na lokacijo datoteke `chromedriver.exe`

1. Pojdite na nepremicnine.net in v iskalniku in filtru uredite iskalne pogoje
2. Kopirajte link, ki se vam je ustvaril
3. Zaženite skripto z ukazom `py main.py PRILEPITE LINK`
4. Počakajte, da se skripta zaključi. Vmes se vam bojo odpirala okna brskalnika - brez straha.
5. Izvoz podatkov je v datoteki `export.xlsx` v mapi skripte

*Skripta je namenjena kot pomoč agentom. Ne odogovorjam v kolikor zaidete v težave z zakonom.
