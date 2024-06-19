### Problemski zadatak 3

U ovom problemskom zadatku potrebno je napraviti model koji će klasificirati novčanice iz datoteke `banknote.csv` kao prave ili falsificirane. Više informacija o skupu podataka možete pronaći[ovdje](https://archive.ics.uci.edu/dataset/267/banknote+authentication). Ovo je standardni pristup realnim problemima bez korištenja dubokih modela. Naime svaka od ovih značajki je ručno konstruirana na temelju nekih svojstava slike lažne novčanice. 

Vaš je zadatak učitati podatke na način prikladan obradi uz sklearn biblioteku. Zatim stvorite skup za treniranje i skup za testiranje te implementirajte algoritam logističke regresije. Potrebno je ispisati matricu zabune. Možete koristiti polinomijalna preslikavanja. 

Savjetujem korištenje standardne `csv` bibliotke za čitanje datoteke.