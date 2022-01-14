"""Python 1 összefoglaló"""
# A kód bizonyos helyen történő megállításához írj az adott kódrész után egy üres input() parancsot.

"""Dolgok kiírása konzolra"""
# Szövegek kiírása
print("Hello World!") # Kiírja a paraméterként megadott szöveget, vagy szöveggé konvertált más típusú változót egy új
# sorba. Eredmény: Hello World! kiírva a konzolra

print("Szövegek " + "összefűzve " + "+ " + "jellel.") # Szöveges értékek összefűzhetőek a + számtani operátorral.
# Eredmény: Szövegek összefűzve + jellel. kiírva a konzolra

print("Idézőjelek: \"Kétszeres\", \'Egyszeres\'") # Idézőjeleket konzolra feloldójel segítségével lehet kiírni. Az
# idézőjel elé be kell egy fordított perjelet írni (Alt Gr + Q). Eredmény: Idézőjelek: "Kétszeres", 'Egyszeres' kiírva
# a konzolra.

print() # Üres sor, hogy olvashatóbbb legyen a konzolon

# Sortörés print() parancsban
print("Sortörés, első módszer:")
print("1.sor")
print("2.sor") # Külön print() parancsok használatával. Sok helyet foglal, és nem elegáns. Eredmény: 1.sor 2.sor külön
# sorokba kiírva

print()

print("Sortörés, második módszer:")
print("""1.sor
2.sor""") # Tripla idézőjelek között a sortörések megmaradnak. Eredmény: 1.sor 2.sor külön sorokba kiírva

print()

print("Sortörés, harmadik módszer:")
print("1.sor\n2.sor") # A \n ("new line", azaz új sor) segítségével új sort tudunk kezdeni a megadott helyen.
# Eredmény: 1.sor 2.sor külön sorokba kiírva

print()

print("\tBehúzott szöveg") # A \t (tabulátor) kifejezéssel behúzhatjuk jobbra a kinyomtatott szövegünket.

"""Változók"""
# Ha egy értéket később újrahasználnánk, vagy módosítanánk, változóban fogjuk tárolni. A Pythonban létrehozáskor kell
# neki egy nevet és egy értéket adni. Ez alapján be fogjuk tudni pket azonosítani, a programfordító pedig meg tudja
# mondani, milyen a típusuk. A nevet és értéket az = (értékadás) operátorral kötjük össze. Nem összekeverendő az
# == (összehasonlítás) operátorral.

"""Eddig használt változótípusok"""
# int: "integer", azaz egész szám. Egész számok tárolására képes.
my_int = 121
print("Ilyen a my_int:", my_int)

# float: "floating point", azaz lebegőpontos ábrázolású szám. Tizedestört-számok tárolására képes.
my_float = 1.618
print("Ilyen a my_float:", my_float)

# str: "string", azaz szöveget tartalmaz, fontos rá úgy gondolni, mint írásjelek listája. A Pythonban használhatunk
# jelölésükre egyszeres (') vagy dupla idézőjelet ("), nincs különbség.
my_str = "Hello world!"
print("Ilyen a my_str:", my_str)

# bool: "boolean", azaz logikai változó. Igaz (True), vagy hamis (False) értéket vehet fel.
my_bool = False
print("Ilyen a my_bool:", my_bool)

# list: lista, azaz elemek sorozata. Az elemeket elérhetjük az értékük, vagy sorszámuk (index) alapján. A sorszámozás
# (indexelés) 0-tól indul. Tehát ezen a listán a my_int indexe 0, a my_float-é 1, a my_string-é 2, stb. Bármilyen elemet
# tehetünk bármilyen listába, nincs meghatározva, hogy adott listába csak float, vagy int, vagy egyéb objektum mehet.
# Viszont, hogyha végigmegyünk az összes elemén, és valamit csinálni szeretnénk velük, akkor fontos észben tartani,
# milyen fajta elemekről van szó. Pl. egy bool-t nem fog engedni eosztani 2-vel.
my_list = [my_int, my_float, my_str, my_bool]
print("Ilyen a list:", my_list)

print()

"""Típusokkal kapcsolatos függvények"""
# Változó típusának lekérdezése
print("A my_int változó típusa:", type(my_int)) # Eredmény: <class 'int'>
print("A my_float változó típusa:", type(my_float)) # Eredmény: <class 'float'>
print("A my_str változó típusa:", type(my_str)) # Eredmény: <class 'str'>
print("A my_bool változó típusa:", type(my_bool)) # Eredmény: <class 'bool'>
print("A my_list változó típusa:", type(my_list)) # Eredmény: <class 'list'>

print()

# Konvertálás
int_to_float = float(my_int)
print("my_int floattá alakítva:", int_to_float) # Bármiyen int változó átalakítható floattá, hisz csak egy tizedes 0-t
# kell hozzárakni. Eredmény: 121.0

float_to_int = int(my_float) # Bármilyen float átlakítható intté, ilyenkor lekerekíti a legközelebbi magánál kisebb
# egészhez. Eredmény: 1
print("my_float intté alakítva:", float_to_int)

my_str = "123456789"
str_to_int = int(my_str) # Ez különösen számok input()-tal beolvasásakor jön kapóra. Eredmény: 123456789
print("Beolvasott 123456789 értékű string intté átalakítva:", str_to_int)

my_str = "123456789"
str_to_float = float(my_str)
print("Beolvasott 123456789 értékű string intté átalakítva:", str_to_float) # Eredmény: 123456789.0

int_to_str = str(my_int) # Ez különösen akkor hasznos, ha számokat szövegként akarunk kezelni, pl. számjegyekre bontani.
# A print() ugyanúgy nyomtatja ki a stringet és az intet konzolra, de fontos a kettő közti különbség. Eredmény: "121"
print("my_int stringgé alakítva:", int_to_str)

float_to_str = str(my_float)
print("my_float stringgé alakítva:", float_to_str)

"""Változók kiírása print()-tel"""
# Nyers kinyomtatás
print("Változók nyers kinyomtatása:")
my_str = "Hello world!"
print(my_str)
my_int = 121
print(my_int)
my_float = 1.618
print(my_float)

print()

# Összefűzés szöveggel
print("Összefűzés + jellel:")
print("A my_str értéke: " + my_str) # Ezzel a módszerrel csak string objektumokat tudunk alapból összefűzni, mert számok
# esetén nem lenne egyértelmű, hogy összeadást, vagy összefűzést akarunk-e végezni, ezárt hibaüzenetet kapunk.
print("A my_int értéke: " + str(my_int))
print("A my_float értéke: " + str(my_float)) # Konvertáló függvény használatával számok is összefűzhetőek.
print("A my_str értéke " + my_str + ", a my_int értéke " + str(my_int) + ", a my_float értéke " + str(my_float) + ".")

print()

# Százalékjeles behelyettesítés
print("Változók behelyettesítése % jellel:")
print("A my_str értéke: %s" % my_str) # Az idézőjelen belüli %s helyére bekerül a külső % jel után meghívott változó
# értéke. Léteznek egyéb behelyettesítési jelzők (%d, %f, %x, stb.) de ezek nem fontosak jelenlegi céljainkra.
print("A my_int értéke: %s" % my_int) # A %s magában foglalja a stringgé alakítást, nem szükséges külön konvertáló
# függvényt használnunk.
print("A my_float értéke: %s" % my_float)
print("A my_str értéke %s, a my_int értéke %s, a my_float értéke %s." % (my_str, my_int, my_float)) # Több változó
# behelyettesítésekor a külső % jel után a változókat zárójelbe kell tenni. A behelyettesítés abban a sorrendben
# történik, ahogy a zárójelben megjelennek. A %s-ek és behelyettesítendő változók számának egyeznie kell. Ha több, vagy
# kevesebb, hibát dob a program.

print()

# Többparaméteres print()
print("Kinyomtatandó részek vesszővel elválasztva:")
print("A my_str értéke:", my_str) # Több paraméter esetén hasonlóan működik a parancs, mint a + jeles verzió, viszont
# automatikusan rak a kinyomtatott paraméterek közé szóközt, és nem kell konvertáló függvényt használnunk itt sem.
print("A my_int értéke:", my_int)
print("A my_float értéke:", my_float)
print("A my_str értéke", my_str, ", a my_int értéke", my_int, ", a my_float értéke", my_float, ".") # Itt behelyezett
# fölösleges szóközöket ez a módszer.
# Eredmény: A my_str értéke Hello world! , a my_int értéke 121 , a my_float értéke 1.618 . kinyomtatva
print("A my_str értéke", my_str, "\b, a my_int értéke", my_int, "\b, a my_float értéke", my_float, "\b.") # A fölös
# szóközöket a \b ("backslash", azaz törlés) kifejezéssel lehet eltávolítani.
# Eredmény: A my_str értéke Hello world!, a my_int értéke 121, a my_float értéke 1.618. kinyomtatva

print(my_str, "EXAMPLE", my_int, my_float, sep=" x ") # Ennek a fajta print()-nek a végére behelyezhetűnk egy sep=
# paramétert, amelynek a megadott értéke be fog kerülni az előtte álló kinyomtatott paraméterek közé.
# Eredmény: Hello world! x EXAMPLE x 121 x 1.618 kinyomtatva

print(my_str, "EXAMPLE", my_int, my_float, end=" x\n ") # Az end= paraméter a kinyomtatott sor végére helyezi el a
# megadott értéket. Ez különösen ciklusokkal van használatban. Ha az end végére nem teszünk \n-t, vagy üresen hagyjuk,
# akkor nem ugrunk a következő sorra a kiírás után, hanem maradunk az eddigin.
# Eredmény: Hello world! EXAMPLE 121 1.618 x kinyomtatva

print()

# f-stringek
print("f-stringek használatával:")
print(f"A my_str értéke: {my_str}") # Egy f-et (mint formátum) teszünk az idézőjel elé, és kapcsos zárójelek
# (Alt Gr + B, Alt Gr + N) segítségével könnyedén tudunk változókat elhelyezni a szövegünkben.
print(f"A my_int értéke: {my_int}")
print(f"A my_float értéke: {my_float}")
print(f"A my_str értéke {my_str}, a my_int értéke {my_int}, a my_float értéke {my_float}.")

print()

"""Műveletek számokkal"""
# Itt int-ekkel mutatom be a műveleteket, de floattal is minden ugyanúgy működik, csak ott mindem eredmémy float lesz.

print()
print("x = 2, y = 3")

"""Számtani operátorok"""
x = 2
y = 3

# Összeadás
total = x + y # Eredmény: 5
print("x és y összege: " + str(total))

# Kivonás
difference = x - y # Eredmény: -1
print("x és y különbsége: " + str(difference))

# Szorzás
product = x * y # Eredmény: 6
print("x és y szorzata: " + str(product))

# Osztás
quotient = x / y # Eredmény: 0.6666666666666666 (Az osztás eredménye mindig float, még akkor is, ha egészben megvan!)
print("x és y hányadosa: " + str(quotient))

# Osztás alsó egészrésze (A legnagyobb egész szám, ahányszor az osztó megvan az osztandóban. Más szóval,
# az osztás eredményének egészrésze.)
floored_quotient = x // y # Eredmény: 0 (Egészrész, tehát mindig int!)
print("y ennyiszer van meg x-ben: " + str(floored_quotient))

# Osztás maradéka. Ha az eredmény 0, azt jelenti, hogy x osztható y-nal.
remainder = x % y # Eredmény: 2
print("x y-nal leosztásának maradéka: " + str(remainder))

# Hatványozás
x_pow_y = x ** y # Eredmény: 8 (2 a köbön, azaz 2*2*2)
print("x az y-odikon: " + str(x_pow_y))

print()
print("x = 10")

"""Értékadó operátorok (Az eredmények itt az x-be kerülnek)"""
# Hozzáadás
x = 10
x += 1 # Eredmény: 11
print("x += 1:", x)

# Kivonás változóból
x = 10
x -= 1 # Eredmény: 9
print("x -= 1:", x)

# Változó felszorzása
x = 10
x *= 2 # Eredmény: 20
print("x *= 2:", x)

# Változó leosztása
x = 10
x /= 2 # Eredmény: 5.0 (Még ha egész is az eredmény, akkor is float!)
print("x /= 2:", x)

# Változó számmal leosztásának egészrésze
x = 10
x //= 4 # Eredmény: 2 (10-ben 2-szer van meg a 4 teljesen, más szóval 10/4, azaz 2.5 egészrésze)
print("x //= 4:", x)

# Változó számmal osztásának maradéka
x = 10
x %= 4 # Eredmény: 2 (Ha 0: x osztható az adott számmal)
print("x %= 4:", x)

# Változó hatványra emelése
x = 10
x **= 3 # Eredmény: 1000 (10*10*10)
print("x **= 3:", x)

print()

"""Bináris számok"""
my_bin = bin(100) # Bináris számmá alakítja megadott decimális int (azaz 10-es számrendszerbeli egész) számot. Float
# értékekkel nem működik. A bináris megfelelőt egy string formájában adja vissza, egy 0b előtaggal. Eredmény: 0b1100100
print("100 bináris megfelelője:", my_bin)

my_bin = my_bin[2:] # Ahhoz, hogy az előtagot elhagyjuk, le kell vágnunk a szöveges bináris szám elejét az alábbi módon.
# Eredmény: 1100100
print("100 bináris megfelelője az előtag nélkül:", my_bin)

print()
print("Példaszöveg: abc. Abc. ABC! AbC-aBc.")

"""Szövegmódosító műveletek"""
# Szövegrész lecserélése
example = "abc. Abc. ABC! AbC-aBc."
example = example.replace('b', 'x') # Első paraméter: mit cserélnél le, második paraméter: mire cserélnéd le. Érzékeny
# kicsi- és nagybetűre. Eredmény: "axc. Axc. ABC! AxC-aBc."
print("b, x cseréje:", example)

example = "abc. Abc. ABC! AbC-aBc."
example = example.replace("abc", "xyz") # Nem csak betűket, de egész szövegrészeket lecserélhetünk így.
# Eredmény: "xyz. Abc. ABC! AbC-aBc."
print("abc, xyz cseréje:", example)

example = "abc. Abc. ABC! AbC-aBc."
example = example.replace("123", "xyz") # Ha nincs benne a stringben az, amit kicserélnénk, nem dob hibát. Csak nem
# csinál semmit. Eredmény: "abc. Abc. ABC! AbC-aBc."
print("123 és xyz cseréje:", example)

# Nagybetűssé alakítás
example = "abc. Abc. ABC! AbC-aBc."
example = example.upper() # Az egész szöveget nagybetűssé teszi. Eredmény: "ABC. ABC. ABC! ABC-ABC."
print("upper() függvény:", example)

# Kisbetűssé alakítás
example = "abc. Abc. ABC! AbC-aBc."
example = example.lower() # Az egész szöveget kisbetűssé teszi. Eredmény: "abc. abc. abc! abc-abc."
print("lower() függvény:", example)

# Cím-jellegű formázás
example = "abc. Abc. ABC! AbC-aBc."
example = example.title() # Minden szó nagybetűvel kezdődik. Eredmény: "Abc. Abc. Abc! Abc-Abc."
print("title() függvény:", example)

# Nagybetűs kezdés
example = "abc. Abc. ABC! AbC-aBc."
example = example.capitalize() # A teljes szöveg első szava nagybetűs, minden más kicsi.
# Eredmény: "Abc. abc. abc! abc-abc."
print("capitalize() függvény:", example)

# Szöveg elválasztása
example = "abc. Abc. ABC! AbC-aBc."
example = example.split(' ') # Egy listáb szétszedi a szöveget a megadott szövegrész (itt: egy szóköz) mentén. Maga a
# szövegrész nem kerül bele a listába, csak ami előtte és utána van, egészen a következő azonos szövegrészig, vagy a
# lista határaiig. Eredmény: ['abc.', 'Abc.', 'ABC!', 'AbC-aBc.']
print("split() függvény szököz mentén:", example)

example = "abc. Abc. ABC! AbC-aBc."
example = example.split("ABC!") # Lehet hosszabb szöveg mentén is bontani. Ilyenkor is eltűnik a szövegrész maga.
# Eredmény: ['abc. Abc. ', ' AbC-aBc.']
print("split() függvény \"ABC!\" mentén:", example)

example = "abc. Abc. ABC! AbC-aBc."
lower, capital, upper, mixed = example.split(' ') # A split függvénnyel lehet élből változókba pakolni az egyes
# elemeket. Ehhez viszont a bal oldalon a változók számának egyeznie kell a jobb oldalon lévő függvény által létrehozott
# lista elemeinek számával. Tehát, ahány felé osztod a szöveget, annyi változót kell létrehoznod bal oldalt. Ha több,
# vagy kevesebb, hibát fog dobni.
print("Első változó:", lower)
print("Második változó:", capital)
print("Harmadik változó:", upper)
print("Negyedik változó:", mixed)

print()
print("Példaszöveg: 123456789")

"""Szöveg vizsgálata"""
# Szöveg hossza
example = "123456789"
example_length = len(example) # Eredmény: 9
print("Szöveg hossza:", example_length)

# Szövegrész keresése
example = "123456789"
index_of_3 = example.find('3') # Megkeresi, hanyadik helyen bukkan fel először (és csak először!) az adott szövegrész.
# Fontos, hogy itt írásjelek listájaként van kezelve a szöveg, így 0-tól kezdődik az indexelés! Eredmény: 2
print("3 írásjel indexe a szövegben:", index_of_3)

example = "123456789"
index_of_456 = example.find("456") # Hosszabb szöveget is meg tudunk benne keresni, ilyenkor az elejének helyét adja meg
# eredményként. Eredmény: 3
print("456 szövegrész indexe a szövegben:", index_of_456)

example = "123456789"
index_of_x = example.find('x') # Ha a keresett szövegrész nem szerepel a szövegben, -1-et ad vissza. Eredmény: -1
print("x írásjel indexe a szövegben:", index_of_x)

print()
print("Példaszöveg: A mitokondrium a sejt erőműve.")

# Kezdőbetű ellenőrzése
example = "A mitokondrium a sejt erőműve."
starts_with_A = example.startswith('A') # Megnézi, hogy az első betű az-e, amit megadsz. Logikai állítás, tehát vagy
# igaz, vagy hamis, bool értéket fog felvenni. Eredmény: True
print("Nagy A-val kezdődik a mondat?", starts_with_A)

example = "A mitokondrium a sejt erőműve."
starts_with_a = example.startswith('a') # Érzékeny kis- és nagybetűre! Eredmény: False
print("Kis a-val kezdődik a mondat?", starts_with_a)

example = "A mitokondrium a sejt erőműve."
starts_with_string = example.startswith('A mitok') # Lehet hosszabb szövegre is kérdezni. Eredmény: True
print("Azzal kezdődik a mondat, hogy \"A mitok\"?", starts_with_string)

print()
print("Példaszöveg: 123456789")

# Tartalom ellenőrzése
example = "123456789"
example_is_decimal = example.isdecimal() # Ellenőrzi, hogy minden írásjel 0 és 9 közötti szám-e, azaz, hogy egész számot
# ad-e ki a szöveg. Eredmény: True
print("A példaszöveg egész számot ad ki:", example_is_decimal)

example = "123456789"
example_is_numeric = example.isnumeric() # Ellenőrzi, hogy minden írásjel numerikus-e. Ez jelentheti a 0 és 9 közötti
# arab számokat, illetve egyéb szám-jellegű Unicode karaktereket. Más írásrendszerek számait, egykarakteres törteket,
# római számoknak fenntartott írásjeleket, stb. Pl. ½, ५, ௮, ൬, 𝟡, Ⅹ, 億 Eredmény: True
print("A példaszöveg összes írásjele hordoz számértéket:", example_is_numeric)

example = "123456789"
example_is_alpha = example.isalpha() # Ellenőrzi, hogy minden írásjel betű-e a szövegben. A szóköz nem számít betűnek,
# ezért csak szavak ellenőrzésére alkalmas. Nem érzékeny kis- és nagybetűre. Idegen nyelvű írásjelek nem zavarják.
# Eredmény: False
print("A példaszöveg csakis betűkből áll:", example_is_alpha)

print()
print("Példaszöveg: A mitokondrium a sejt erőműve.")

example = "A mitokondrium a sejt erőműve."
example_is_decimal = example.isdecimal()
print("A példaszöveg egész számot ad ki:", example_is_decimal)

example = "A mitokondrium a sejt erőműve."
example_is_numeric = example.isnumeric()
print("A példaszöveg összes írásjele hordoz számértéket:", example_is_numeric)

example = "A mitokondrium a sejt erőműve."
example_is_alpha = example.isalpha()
print("A példaszöveg csakis betűkből áll:", example_is_alpha)

print()
print("Példaszöveg: MacGyver")

example = "MacGyver"
example_is_decimal = example.isdecimal()
print("A példaszöveg egész számot ad ki:", example_is_decimal)

example = "MacGyver"
example_is_numeric = example.isnumeric()
print("A példaszöveg összes írásjele hordoz számértéket:", example_is_numeric)

example = "MacGyver"
example_is_alpha = example.isalpha()
print("A példaszöveg csakis betűkből áll:", example_is_alpha)

print()
print("Példaszöveg: 一億二千三百四十五万六千七百八十九") # 123456789 hagyományosan leírva hagyományosan sino-japánul

example = "一億二千三百四十五万六千七百八十九"
example_is_decimal = example.isdecimal()
print("A példaszöveg egész számot ad ki:", example_is_decimal)

example = "一億二千三百四十五万六千七百八十九"
example_is_numeric = example.isnumeric()
print("A példaszöveg összes írásjele hordoz számértéket:", example_is_numeric)

example = "一億二千三百四十五万六千七百八十九"
example_is_alpha = example.isalpha()
print("A példaszöveg csakis betűkből áll:", example_is_alpha)

print()
print("Példaszöveg: MITOKONDRIUM")

# Kisbetű-nagybetű ellenőrzés
example = "MITOKONDRIUM"
example_is_upper = example.isupper() # Ellenőrzi, hogy minden betű a szövegben nagy-e. Olyan írásjelek, amelyeknél a
# kis- és nagybetűsség nem értelmezhető (pl. számok, külföldi írásjelek), ott se kicsinek, se nagynak nem fognak
# számítani. Eredmény: True
print("A példaszöveg csakis nagybetűkből áll:", example_is_upper)

example = "MITOKONDRIUM"
example_is_lower = example.islower() # Ellenőrzi, hogy minden betű a szövegben kicsi-e. Eredmény: False
print("A példaszöveg csakis kisbetűkből áll:", example_is_lower)

print()
print("Példaszöveg: mitokondrium")

example = "mitokondrium"
example_is_upper = example.isupper()
print("A példaszöveg csakis nagybetűkből áll:", example_is_upper)

example = "mitokondrium"
example_is_lower = example.islower()
print("A példaszöveg csakis kisbetűkből áll:", example_is_lower)

print()
print("Példaszöveg: Mitokondrium")

example = "Mitokondrium"
example_is_upper = example.isupper()
print("A példaszöveg csakis nagybetűkből áll:", example_is_upper)

example = "Mitokondrium"
example_is_lower = example.islower()
print("A példaszöveg csakis kisbetűkből áll:", example_is_lower)

print()
print("Példaszöveg: 123456789")

example = "123456789"
example_is_upper = example.isupper()
print("A példaszöveg csakis nagybetűkből áll:", example_is_upper)

example = "123456789"
example_is_lower = example.islower()
print("A példaszöveg csakis kisbetűkből áll:", example_is_lower)

print()
print("my_list = ['Anna', 'Béla', 'Cecília', 'Dani', 'Ernő']")

"""Listák"""
my_list = ['Anna', 'Béla', 'Cecília', 'Dani', 'Ernő']

# Lista elemeinek száma (hossza)
print("A my_list hossza:", len(my_list)) # A len(list) fügvénnyel le tudjuk kérdezni a listánk hosszát. Eredmény: 5

# Lista egyes elemeinek elérése
print("A my_list első eleme:", my_list[0]) # A listák 0-tól indexelnek! Eredmény: Anna
print("A my_list második eleme:", my_list[1]) # Eredmény: Béla
print("A my_list utolsó eleme:", my_list[-1]) # Negatív indexszel hátulról is tudunk a listán visszafele haladni. Így a
# -1 indexű elem a lista utolsója lesz. Fontos, hogy hátulról -1-től kezdve indexelünk, mert -0 = 0 lenne.
# Eredmény: Ernő
print("A my_list utolsó előtti eleme:", my_list[-2]) # Eredmény: Dani

print()

# Listán több elem elérése
first_3_elements = my_list[0:3] # Ezzel egy listába ki tudjuk választani a listánk egy összefüggő részét két index
# között. A négyzetes zárójel bal oldali eleme a kezdő index, a jobb oldali pedig a végső index. A kezdő index által
# jelölt elem még bekerül a listába, de a végső index eleme már nem. Eredmény: ['Anna', 'Béla', 'Cecília']
print("A my_list első 3 eleme:", first_3_elements)

last_3_elements = my_list[-3:len(my_list)] # Itt a hátulról harmadik elemtől kezdve vesszük a kiválasztott elemeket, és
# a lista végéig megyünk. Eredmény: ['Cecília', 'Dani', 'Ernő']
print("A my_list utolsó 3 eleme:", last_3_elements)

first_3_elements = my_list[:3] # Ha a bal oldali elem 0 (azaz a lista első elemétől kezdünk), akkor elhagyható. Ez
# ugyanazt csinálja, mint az első példánk. Eredmény: ['Anna', 'Béla', 'Cecília']
print("A my_list első 3 eleme:", first_3_elements)

last_3_elements = my_list[-3:len(my_list)] # Ha pedig a jobb oldali elem a listánk hossza (azaz a listánk végéig
# megyünk), akkor elhagyható. Ez ugyanazt csinálja, mint a második példánk. Eredmény: ['Cecília', 'Dani', 'Ernő']
print("A my_list utolsó 3 eleme:", last_3_elements)

middle_3_elements = my_list[1:4]
print("A my_list középső 3 eleme:", middle_3_elements) # Eredmény: ['Béla', 'Cecília', 'Dani']

print()
print("my_list = ['Anna', 'Béla', 'Cecília', 'Dani', 'Ernő']")

"""Listafüggvények"""
# Elemek hozzáadása listákhoz
my_list = ['Anna', 'Béla', 'Cecília', 'Dani', 'Ernő']
print("Feri hozzáadása a my_listhez")
my_list.append("Feri") # Hozzácsatolja a lista végére a megadott elemet.
# Eredmény: ['Anna', 'Béla', 'Cecília', 'Dani', 'Ernő', 'Feri']
print("my_list:", my_list)

print("False a lista 3.helyére")
my_list.insert(2, False) # Egy meghatározott indexre beilleszti az adott elemet. Első paraméter: új elem indexe,
# második paraméter: új elem értéke. Ha az index nagyobb, mint a lista hossza, akkor a lista végére kerül az elem.
# Negatív index használható itt is, és akkor hátulról fog visszafele számolni.
# Eredmény: ['Anna', 'Béla', False, 'Cecília', 'Dani', 'Ernő', 'Feri']
print("my_list:", my_list)

print("extend_list = [1, 2, 3]")
print("my_list bővítése extend_list-tel")
extend_list = [1, 2, 3]
my_list.extend(extend_list) # Bővíti a gyűjteményt a paraméterként megadott gyűjteménnyel. Itt egy listát lényegében
# rácsatolunk a már meglévő listánkra. Egyes elemekkel nem lehet csak úgy ezt használni (kivéve stringgel, mert az
# írásjelek gyűjteménye, és így az egyes írásjelek listaként hozzá lesznek adva a régi listához).
# Eredmény: ['Anna', 'Béla', False, 'Cecília', 'Dani', 'Ernő', 'Feri', 1, 2, 3]
print("my_list:", my_list)

print()
print("my_list = ['Anna', 'Béla', False, 'Cecília', 'Dani', 'Ernő', 'Feri', 1, 2, 3]")

# Elemek eltávolítása listáról
print("2-es indexű elem etávolítása listáról")
my_list.pop(2) # Eltávolítja a megadott indexen lévő elemet. Negatív indexek működnek. Haa túl nagy a megadott index,
# hibát dob a kód. Eredmény: ['Anna', 'Béla', 'Cecília', 'Dani', 'Ernő', 'Feri', 1, 2, 3]
print("my_list:", my_list)

print("Ernő értékű elem eltávolítása listáról")
my_list.remove("Ernő") # Eltávolítja az első egyező értékű elemet a listáról. Ha nincs egyező elem a listán, hibát dob.
# Eredmény: ['Anna', 'Béla', 'Cecília', 'Dani', 'Feri', 1, 2, 3]
print("my_list:", my_list)

print()
print("my_list = ['Anna', 'Béla', 'Cecília', 'Dani']")

# Elemek cseréje
my_list = ['Anna', 'Béla', 'Cecília', 'Dani']
print("Első és harmadik elem megcserélése")
my_list[0], my_list[2] = my_list[2], my_list[0] # Indexeik alapján megcserélhető ilyen módon kettő vagy több elem. A
# baloldalt megadott elemek számának egyeznie kell jobboldaliakkal.
print("my_list:", my_list)

print()
print("list_1 = ['C', 'D', 'Á', 'A', 'B', 'Cs']\nlist_2 = [4, 5, 2, 1, 3]"
      "\nlist_3 = [True, False]\nlist_4 = [3.1416, 1.618, 94.23, 5, 0.673, 2]")

# Lista automatikus rendezése
print("A listák rendezése sort() függvénnyel")
list_1 = ['C', 'D', 'Á', 'A', 'B', 'Cs']
list_2 = [4, 5, 2, 1, 3]
list_3 = [True, False]
list_4 = [3.1416, 1.618, 94.23, 5, 0.673, 2]

list_1.sort() # Az elemek Unicode-azonosítója alapján rendezi a string elemeket. Az angol ABC betűt korrektül sorrendbe
# helyezi, de más betűkkel bajban van. Eredmény: ['A', 'B', 'C', 'Cs', 'D', 'Á']
print("list_1:", list_1)

list_2.sort() # Eredmény: [1, 2, 3, 4, 5]
print("list_2:", list_2)

list_3.sort() # A False logikai értéke 0, a True logikai értéke 1. Ezek alapján rendezi a bool-okat.
# Eredmény: [False, True]
print("list_3:", list_3)

list_4.sort() # Az int és float típusú számok szabadon összehasonlíthatóak egymás között.
# Eredmény: [0.673, 1.618, 2, 3.1416, 5, 94.23]
print("list_4:", list_4)

print()
print("list_1 = ['C', 'D', 'Á', 'A', 'B', 'Cs']\nlist_2 = [4, 5, 2, 1, 3]"
      "\nlist_3 = [True, False]\nlist_4 = [3.1416, 1.618, 94.23, 5, 0.673, 2]")

# Listák maximuma, minimuma
# A rendezés elvei ugyanazok, mint a rendezésnél
print("Listák maximumának megkeresése")
list_1 = ['C', 'D', 'Á', 'A', 'B', 'Cs']
list_2 = [4, 5, 2, 1, 3]
list_3 = [True, False]
list_4 = [3.1416, 1.618, 94.23, 5, 0.673, 2]

list_1_max = max(list_1)
list_1_min = min(list_1)
print(f"list_1 maximuma: {list_1_max}, minimuma: {list_1_min}")

list_2_max = max(list_2)
list_2_min = min(list_2)
print(f"list_2 maximuma: {list_2_max}, minimuma: {list_2_min}")

list_3_max = max(list_3)
list_3_min = min(list_3)
print(f"list_3 maximuma: {list_3_max}, minimuma: {list_3_min}")

list_4_max = max(list_4)
list_4_min = min(list_4)
print(f"list_4 maximuma: {list_4_max}, minimuma: {list_4_min}")

print()
print("list_1 = list_1 = [1, 3, 5, 8, 3]\nlist_2 = [3.23, 2.12, 1.76, 2.89]")

# Lista elemeinek összege
print("Számlisták összege")
list_1 = [1, 3, 5, 8, 3]
list_2 = [3.23, 2.12, 1.76, 2.89]
list_1_sum = sum(list_1) # Eredmény: 20
print("list_1 összege:", list_1_sum)
list_2_sum = sum(list_2) # Eredmény: 10.0
print("list_2 összege:", list_2_sum)

print()
print("my_list = ['Anna', 'Béla', 'Cecília', 'Dani']")

# Elem indexének megkeresése tartalom alapján
my_list = ['Anna', 'Béla', 'Cecília', 'Dani']
print("Béla értékű elem indexének megkeresése")
index_of_Bela = my_list.index("Béla") # Visszaadja az első olyan elem indexét, amelynek a tartalma egyezik a megadott
# értékkel. Ha nincs benne a listában a keresett érték, hibát dob. Eredmény: 1
print("Béla értékű elem indexe:", index_of_Bela)

print()
print("my_list = ['Anna', 'Béla', 'Cecília', 'Dani']")

# Lista elegáns kiírása, stringgé alakítása
my_list = ['Anna', 'Béla', 'Cecília', 'Dani']
print("Lista összekapcsolása csillaggal")
star_joined_my_list = "*".join(my_list) # Összekapcsolja a lista elemeit egy stringgé. Az elemeket az elöl megadott string
# fogja elválasztani egymástól. Eredmény: Anna*Béla*Cecília*Dani
print("Csillaggal összekapcsolt string:", star_joined_my_list)

print("Szépen tagolt kiírás")
comma_joined_my_list = ", ".join(my_list) # Eredmény: Anna, Béla, Cecília, Dani
print("Vesszővel és szóközzel összekapcsolt string:", comma_joined_my_list)

print()
print("x = 2, y = 3, z = 2")

"""Logika"""
# Összehasonító operátorok (relációs jelek)
x = 2
y = 3
z = 2

# Számok értékét(!) haasonlítjuk össze
x_less_than_y = x < y # Itt az újonnan létrehozott változónak az x < y logikai állítás eredményét adjuk meg értéknek.
# Tehát, ha x kisebb, mint y, akkor a változó True értéket kap, ha pedig nagyobb, akkor False-ot. Eredmény: True
print("Kisebb x y-nál?", x_less_than_y)

x_greater_than_y = x > y # Eredmény: False
print("Nagyobb x y-nál?", x_greater_than_y)

x_equals_y = x == y # A == összehasonlítás, a = pedig érték-hozzárendelés. Ha a 2 változó egyezik, True, amúgy False.
# Eredmény: False
print("Egyezik x és y?", x_equals_y)

x_greater_than_or_equals_z = x >= z # Nagyobb, vagy egyenlő operátor. Eredmény: True
print("x nagyobb-e, vagy egyenlő z-vel?", x_greater_than_or_equals_z)

x_greater_than_or_equals_y = x >= y # Eredmény: False
print("x nagyobb-e, vagy egyenlő y-nal?", x_greater_than_or_equals_y)

x_less_than_or_equals_z = x <= z # Eredmény: True
print("x kisebb-e, vagy egyenlő z-vel?", x_less_than_or_equals_z)

x_less_than_or_equals_y = x <= y # Eredmény: True
print("x kisebb-e, vagy egyenlő y-nál?", x_less_than_or_equals_y)

x_equals_z = x == z # Ha a 2 egyezik, True, egyébként False. Eredmény: True
print("Egyezik x és z?", x_equals_z)

x_not_equals_z = x != z # Ha a 2 eltér, True, ha egyeznek, False. Eredmény: False
print("Eltér x és z?", x_not_equals_z)

x_not_equals_y = x != y # Eredmény: True
print("Eltér x és y?", x_not_equals_y)

print()
print("list_1 = [1, 2, 3, 4, 5], list_2 = [1, 2, 3, 4, 5]")

# Azonossági operátor (is)
list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5]

list_1_equals_list_2 = list_1 == list_2 # Ha a 2 lista értéke egyezik, True, ha nem, False. Eredmény: True
print("Egyezik a 2 lista tartalma?", list_1_equals_list_2)

list_1_same_object_as_list_2 = list_1 is list_2 # is: azonossági operátor. Ha a 2 lista ugyanaz az objektum (azaz
# ugyanazon a helyen van a memórián belül), akkor True, egyébként False. Egyszerűbb objektumokkal adhatja ugyanazt az
# eredményt, mint a == operátor, de rossz gyakorat. Eredmény: False
print("Azonos objektum a 2 lista?", list_1_same_object_as_list_2)

list_1_is_list = type(list_1) is list # Változó típusának ellenőrzésére is alkalmas az azonossági operátor. Ha a változó
# típusa egyezik a jobb oldalt megadott típussal, True, egyébként False. Eredmény: True
print("A list_1 egy lista?", list_1_is_list)

list_1_is_int = type(list_1) is int # Eredmény: False
print("A list_1 egy int?", list_1_is_int)

list_1_is_not_float = type(list_1) is not float # Ha a változó típusa eltér a jobb oldalt megadott típustól, True,
# egyébként False. Eredmény: True
print("A list_1 nem float objektum?", list_1_is_not_float)

list_1_is_not_list = type(list_1) is not list # Eredmény: False
print("A list_1 nem lista objektum?", list_1_is_not_list)

print()
print("example: MITOKONDRIUM, my_list = [1, 2, 3, 4, 5]")

# Tagsági operátor (in)
example = "MITOKONDRIUM"
my_list = [1, 2, 3, 4, 5]

in_my_list_3 = 3 in my_list # Ha a keresett érték szerepel a gyűjteményben (itt: lista) True, amúgy False.
# Eredmény: True
print("Szerepel a 3 a my_list-en?", in_my_list_3)

in_my_list_42 = 42 in my_list # Eredmény: False
print("Szerepel a 42 a my_list-en?", in_my_list_42)

not_in_my_list_0 = 0 not in my_list # A sima in ellentéte. Ha a keresett érték nincs benne a gyűjteményben, True,
# egyébként False. Eredmény: True
print("Nem szerepel a 0 a my_list-en?", not_in_my_list_0)

in_example_I = 'I' in example # A string írásjelek gyűjteménye, így azzal is működik. Ha a megadott szövegrész szerepel
# a stringben, True, egyébként False. Eredmény: True
print("Szerepel az I az example-ben?", in_example_I)

in_example_i = 'i' in example # Eredmény: False
print("Szerepel az i az example-ben?", in_example_i)

# Logikai operátorok
print()
print("bool_a = False, bool_b = False")
bool_a = False
bool_b = False

a_and_b = bool_a and bool_b # and: "és" operátor. Ha mindkettő állítás igaz, True, egyébként False. Eredmény: False
print("bool_a és bool_b is igaz:", a_and_b)

a_or_b = bool_a or bool_b # or: "vagy" operátor. Ha legalább az egyik állítás igaz, True, egyébként False.
# Eredmény: False
print("bool_a és bool_b közül valamelyik igaz:", a_or_b)

print()
print("bool_a = False, bool_b = True")
bool_a = False
bool_b = True

a_and_b = bool_a and bool_b # Eredmény: False
print("bool_a és bool_b is igaz:", a_and_b)

a_or_b = bool_a or bool_b
# Eredmény: True
print("bool_a és bool_b közül valamelyik igaz:", a_or_b)

print()
print("bool_a = False, bool_b = True")
bool_a = True
bool_b = False

a_and_b = bool_a and bool_b # Eredmény: False
print("bool_a és bool_b is igaz:", a_and_b)

a_or_b = bool_a or bool_b
# Eredmény: True
print("bool_a és bool_b közül valamelyik igaz:", a_or_b)

print()
print("bool_a = False, bool_b = True")
bool_a = True
bool_b = True

a_and_b = bool_a and bool_b # Eredmény: True
print("bool_a és bool_b is igaz:", a_and_b)

a_or_b = bool_a or bool_b
# Eredmény: True
print("bool_a és bool_b közül valamelyik igaz:", a_or_b)

print()
print("bool_a = False")
bool_a = False
not_bool_a = not bool_a # not: "nem", azaz negációs operátor. Az ellentétes értéket adja vissza. Eredmény: True
print("bool_a ellentéte:", not_bool_a)

"""Elágazások"""
print("x = 2, y = 3")
x = 2
y = 3
if x == 2: # Ha az if mögötti feltétel teljesül, az alatta behúzott kódrészlet le fog futni, egyébként nem.
    print("Az x 2.") # Lefut.
else: # "Különben", tehát ha az if utáni feltétel nem fut le, akkor ez le fog. Csak egy lehet belőle, az állítás végén.
    print("Az x nem 2.") # Nem fut le.

if x == 2 and y == 3:
    print("Az x 2.")
    print("És az y 3.") # Fontos a behúzás fenntartása minden állításban szereplő elem előtt.
else:
    print("Az x nem 2 és/vagy az y nem 3.")

if x != 2 and y != 5:
    print("Az x nem 2, és az y nem 5.")
elif x == 1 or y == 3: # "else if", azaz különben hogyha. Ha az első állítás nem teljesül, de ez igen, akkor belépünk az
    # alatta behúzott kódba, és az utána lévőket már nem ellenőrizzük, mert így processzorkímélőbb. Bármennyi elif lehet
    # egymás után.
    print("Vagy az x 1, vagy az y 3.")
else:
    print("Az x nwm 1, az y nem 3.")

print()

"""Ciklusok"""
# while ciklus
current_reps = 1
while current_reps < 5: # Addig ismétli az utána behúzott kódrészletet, ameddig csak igaz a mögötte szereplő állítás.
    print(str(current_reps) + ".ismétlés")
    current_reps += 1
    # Eredmény: 4-szer lesz a kódrészlet megismételve. Mikor a current_reps eléri az 5 értéket, az állítás már nem lesz
    # igaz, így kilépünk a ciklusból.

print()
current_reps = 1
while current_reps <= 5: # Itt kisebb vagy egyenlő operátor van. Amikor a current_reps eléri az 5-öt, akkor is lefut az
    # alábbi behúzott kód.
    print(str(current_reps) + ".ismétlés")
    current_reps += 1
    # Eredmény: 5-ször lesz ismételve a kódrészlet.

print()

# for ciklus
print("Számok range(4)-gyel:")
for i in range(4): # Egyváltozós range: 0 és a megadott szám között (magát a számot nem beleértve) fut le a lenti
    # behúzott kódrészlet.
    print(i)
    # Eredmény: 0 1 2 3 külön sorokba kinyomtatva

print()
print("Számok range(3, 6)-tal:")
for i in range(3, 6): # Kétváltozós range: az első szám az i kezdőértéke (0 helyett), a második pedig a felső határ
    # (amely maga továbbra sem lesz felvéve).
    print(i) # Eredmény: 3 4 5 külön sorokba kinyomtatva

print()
print("Számok range(4, 19, 5)-tel:")
for i in range(4, 19, 5): # Háromváltozós range: az első szám az i kezdőértéke (0 helyett), a második a felső határ, a
    # harmadik pedig a lépések mértéke (az alap 1 helyett).
    print(i) # Eredmény: 4 9 14 külön sorokba kinyomtatva

print()
print("my_list = ['Anna', 'Béla', 'Cecília']")
my_list = ['Anna', 'Béla', 'Cecília']
print("my_list elemei végigiterálva:")
for element in my_list: # Át tudunk menni a lista összes elemén, és végrehajtani egyesével mindegyiken műveleteket.
    print(element)

print()
print("my_str = Hello")
my_str = "Hello"
print("Szövegen végigiterálás:")
for letter in my_str: # A szövegek is gyűjtemények, így végig lehet a bennük szereplő írásjeleken iterálni.
    print(letter)

print()
print("my_list = ['Anna', 'Béla', 'Cecília']")
my_list = ['Anna', 'Béla', 'Cecília']
print("my_list elemeinek index-alapú végigiterálása:")
for i in range(len(my_list)): # Előfordulhat, hogy kell az éppen vizsgált listaelem indexe valamihez. A sima
    # in my_list-es megoldás ezt nem támogatja, ezért ilyenkor a range-el elmegyünk a lista utolsó indexéig. Az adott
    # elemet a my_list[i]-vel érjük ilyenkor el.
    print(my_list[i])

print()

# Beágyazott ciklusok
# Egymáson belül is szerepelhetnek ciklusok, azonban ez exponenciálisan (értsd: nagyon és gyorsan) növeli a
# végrehajtandó műveletek számát.
my_str = ""
for i in range(3):
    for j in range(5):
        my_str += str(j)
        # Eredmény: 01234-el bővíti a my_str-t, minden alkalommal, amikor meghívódik.
    print(my_str)
    # Eredmény: Kinyomtatja a bővült my_str-t, minden alkalomml, amikor meghívódik.
# Végeredmény: 01234 0123401234 012340123401234 külön sorokba kinyomtatva

"""Felhasználói adatbevitel"""
# Az input() függvény segítségével be tudunk kérni adatokat a felhasználótól, és el tudjuk azt változóba menteni. A
# felhasználó képes lesz írni a konzolba, és a program addig nem fut tovább, míg az Enter billentyűt meg nem nyomja. Az
# input függvénnyel bekért adatok mindig string típusban kezdődnek, konvertáló függvény kell ahhoz, hogy más típusként
# tudjunk velük dolgozni.
input("Add meg a neved: ")

input() # A sima input függvény az Enter megnyomásáig gátolja a program továbbfutását.

print("Ezzel a dokumentum végére értél.")

"""PythonTurtle parancsok"""
# go(): A teknős előre megy
# turn(): A teknős bizonyos fokot fordul
# width(): A toll szélességét állítja
# color(""): A toll színét állítja (vagy előre meghtározott nevezetes színek neve, vagy 3 int értékű RGB kód)
# reset(): Törli az eddig rajzokat, és visszaküldi a teknőst a kezdőhelyére
# clear(): Törli az eddigi rajzokat
# invisible(): Láthatatlanná teszi a teknőst
# visible(): Láthatóvá teszi a teknőst
# pen_up(): Felemeli a tollat (nem rajzol mozgás közben)
# pen_down(): Leteszi a tollat (rajzol mozgás közben)
