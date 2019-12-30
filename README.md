# Turnaj
Turnaj v Pythonu pro herní témátko 26. ročníku korespondenčního semináře M&M.

Turnaj byl zadaný v čísle [26.3](https://mam.mff.cuni.cz/media/cislo/pdf/26/26-3.pdf)

## Shrnutí použití

- `player.py` specifikuje rozhraní hráče `Player`. Vzorové programy `mirror.py`, `always_cooperate.py`, `unforgiving.py, `score_counting.py` a `always_deceive.py` jej implementují (a dědí).
	+ `Player` obsahuje tři metody: `author_name` (jen vrací celé jméno autora hráče), `next_move` (vrací následující tah, který má umělý hráč hrát) a `reward` (umožňuje zpracování právě proběhlého kola)
	+ Zároveň je v tomto souboru definován výčet možných tahů `Move`
- `result.py` definuje třídu `Result`, která popisuje jedno kolo (tedy dvojici vlastního a soupeřova tahu a zisky z této dvojice plynoucí)
	+ Atributy `.my_move` a `.opp_move` obsahují volené strategie v tomto kole
	+ Metody `.get_my_score()` a `.get_opp_score()` vrací počty bodů, které jednotliví hráči získali v tomto kole
- `testing.py` je skript, pomocí kterého je možné interaktivně testovat hru proti naprogramované strategii, viz níže
- `README.md` je tohle README
- souborů `.gitignore` a `.gitattributes` si nemusíte všímat, zajišťují jen to, že tenhle repozitář funguje správně.

## Testování strategií

Skript `testing.py` se volá s jedním nebo dvěma parametry:

První parametr je "jméno souboru bez '.py' na konci _tečka_ jméno třídy, proti které se hraje", např. `unforgiving.Unforgiving`

Druhý parametr umožňuje určit počet kol, která se budou hrát, výchozí hodnota je 10 kol.

### Příklad

```
$ python3 testing.py always_cooperate.AlwaysCooperate 3
Pick your next move: C
Your move was: C
Your opponent's move was: C
You scored 10 , total: 10
Your opponent scored 10 , total: 10
--------------------------->
Pick your next move: B
Your move was: B
Your opponent's move was: C
You scored 8 , total: 18
Your opponent scored 0 , total: 10
--------------------------->
Pick your next move: B
Your move was: B
Your opponent's move was: C
You scored 8 , total: 26
Your opponent scored 0 , total: 10
--------------------------->
THE GAME HAS ENDED
--------------------------->
You scored in total 26 points.
AI player scored in total 10 points.
```