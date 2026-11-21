# Název hry: PySnake

## O čem hra je (1–2 věty)
* Jednoduchá arkádová hra Snake v 2D prostředí. Hráč ovládá hada na herní mřížce, sbírá potravu pro růst a získávání bodů, a vyhýbá se nárazům do stěn, překážek a vlastního těla.

## Žánr, pohled, grafický styl
* **Žánr:** Arkádová hra
* **Pohled:** 2D pohled shora (top-down) na čtvercovou mřížku
* **Grafický styl:** Minimalistická 2D grafika s výraznými barvami a vlastními texturami (sprity) pro hada, jídlo a zdi

## Hlavní herní smyčka
Pohyb hada po mřížce → sbírání potravy → prodlužování těla a zvyšování skóre → vyhýbání se překážkám, zdím a vlastnímu tělu → postupné zrychlování hry.

## Ovládání
* **Šipky / WASD:** Změna směru pohybu hada (nahoru, dolů, vlevo, vpravo)
* **Esc:** Pozastavení hry (pauza)
* **Enter / Mezerník:** Potvrzení v menu a restart hry po prohře

## Cíl hry, výhra a prohra
* **Cíl:** Získat co nejvyšší skóre a překonat dosavadní rekord (High Score).
* **Výhra:** Vyplnění celé herní mřížky tělem hada (nezbývá žádné volné pole pro vygenerování další potravy).
* **Prohra (Game Over):** Náraz hlavy hada do okraje herní plochy, do překážky nebo do vlastního těla.

## Herní objekty (hráč, nepřátelé, předměty)
* **Hráč (Had):** Skládá se z hlavy a dynamicky se prodlužujícího těla uloženého v seznamu souřadnic.
* **Potrava (Jídlo):** Objevuje se na náhodných volných polích mřížky (nejsou zaplněné hlavou, ani tělem, ani překážkou); po snědení přidá skóre a prodlouží hada.
* **Okraje herní plochy** Ohraničení herní plochy(obdelník), po nárazu prohra. 
* **Překážky (Zdi):** Statické bloky v herním poli, kterým se hráč musí vyhnout.

## Obrazovky
* **Úvodní menu:** Název hry, tlačítko Start, zobrazení nejlepšího skóre, ukončení hry.
* **Herní obrazovka:** Samotná herní mřížka, aktuální skóre a čas v horní liště.
* **Pauza:** Překryvná obrazovka s možností pokračovat nebo se vrátit do menu.
* **Konec hry (Game Over):** Zobrazení dosaženého skóre, info o novém rekordu, tlačítko pro okamžitý restart a úvodní menu.

## Funkce

### Musí mít
* Plynulý pohyb hada po mřížce v 4 směrech (se zákazem otočení o 180° do sebe).
* Náhodné generování jídla v herní mřížce mimo tělo hada.
* Růst hada a počítání aktuálního skóre.
* Detekce kolizí se stěnami a vlastním tělem.
* Základní stavy hry (Menu, Hraní, Pauza, Game Over) a restart bez vypnutí programu.
* Ukládání a načítání nejvyššího skóre (High Score) ze souboru (např. JSON nebo TXT).

### Mělo by mít
* Postupné zrychlování hry s rostoucím skóre.
* Výběr obtížnosti (rychlost hada nebo mapa s překážkami).
* Základní zvukové efekty (snědení jídla, náraz) a hudba na pozadí.

### Bylo by fajn
* Speciální bonusové jídlo, které po pár sekundách zmizí (za více bodů).
* Vlastní grafika (sprity pro hlavu, tělo, zatáčky a jídlo místo obyčejných čtverců).

### Nebude
* Online žebříček hráčů.
* Režim pro více hráčů (multiplayer).

## Knihovna a nástroje
* **Jazyk:** Python 3.14
* **Herní knihovna:** Pygame CE
* **Vývojové prostředí a verzování:** VS Code, Git a GitHub