### Problemski zadatak

U ovom problemskom zadatku ispitati će se vaše razumijevanje numpy-a. Svi materijali s predavanja i dokumentacija su dopušteni.
Za rješavanje ove vježbe morate imati biblioteku numpy. Možete je instalirati pomoću ove naredbe u terminalu:
```
    pip install numpy --user
```

## 1. zadatak

Pomoću numpy biblioteke implementirajte funkciju $softmax$ za vektore. Funkcija softmax definirana je na sljedeći način:

$$
    softmax: \mathbb{R}^n \to \mathbb{R}^n
$$
$$
    softmax_i(\bold{x}) = \frac{e^{x_i}}{\sum_{j = 1}^n e^{x_j}}
$$

To jest funkcija softmax prima vektor dimenzije $n$ te vraća vektor dimenzije $n$. Svaku komponentu $i$ tog vektora računamo pomoću funkcije $softmax_i$. Pogledajmo primjer:

$$
    \bold{x} = [2 \; 1]^T
$$

$$
    \sum_{j = 1}^n e^{x_j} = e^2 + e^1 = 10.107
$$

$$
    softmax(\bold{x}) = \left[\frac{e^{x_1}}{\sum_{j = 1}^2 e^{x_j}} \; \frac{e^{x_2}}{\sum_{j = 1}^2 e^{x_j}}\right]^T = \left[\frac{7.389}{10.107} \; \frac{2.718}{10.107}\right]^T = [0.731 \; 0.269]^T
$$

## 2. zadatak

Generirajte matricu dimenzija $3x3$ prirodnih brojeva od $0$ do $10$. Svakom neparnom broju dodajte jedan. Ispišite matricu prije i poslije ove operacije.

## 3. zadatak 

Generirajte nasumičnu matricu $3x3$. Izračunajte zbroj svih elemeneta, zbrojeve po svim redcima i zbrojeve po svim stupacima. 