# Election-scraper
Tretí projekt v rámci Engeto akadémie.

# Popis projektu
Projekt slúži k extrahovaniu dát z volieb do parlamentu v roku 2017 v ČR z webovej stránky volby.cz za jednotlivé okresy. Odkaz na stránku [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

# Inštalácia knihoven 
Knihovny ktoré sú použité v kóde sú uložené v súbore `requirements.txt`. Pre inštaláciu doporučujem použiť nové virtuálne prostredie a s nainštalovaným manažérom spustiť následovne:

```
$ pip3 --version                           # overím verziu manažéra
$ pip3 install -r requirements.txt         # nainštalujeme knihovny
```

# Spúštanie programu
Spúštanie programu vyžaduje 2 argumenty. Prvý je odkaz na okres z ktorého chceme extrahovať dáta a druhý je názov súboru s príponou csv do ktorého chceme dáta uložiť.

```
python election.py <odkaz na okres> <meno súboru>
```
# Ukážka projektu
Výsledky hlasovania pre okres Nymburk.

1.argument:  `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108`

2.argument:  `nymburk.csv`

Spúštanie programu:
```
python election.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108" "nymburk.csv"
```
Priebeh sťahovania:
```
Sťahujem data z: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2108

Ukládam data do súboru: nymburk.csv

Ukončuji: election.py
```
Čiastočný výstup:
```
Number of City,City,Voters in the list,Released envelopes,Valid votes,Občanská demokratická strana,...
537021,Běrunice,690,382,382,27,3,0,40,1,28,30,7,4,7,0,0,25,0,6,8,136,1,0,14,0,1,0,1,42,1
537039,Bobnice,666,389,387,37,0,0,33,0,42,31,5,2,3,0,0,27,0,0,23,124,0,1,7,0,0,1,1,50,0
537047,Bříství,268,193,190,26,1,0,18,0,13,12,2,2,1,0,0,16,1,0,3,66,0,0,4,0,3,0,0,22,0
...
```
