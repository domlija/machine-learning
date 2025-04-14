### 1. zadatak — Implementacija funkcije log-sum-exp

Implementirajte funkciju `logsumexp` koja se često koristi u statistici i strojnom učenju zbog numeričke stabilnosti:

$$
\text{logsumexp}(\bold{x}) = \log\left(\sum_{i=1}^n e^{x_i}\right)
$$

Radi numeričke stabilnosti, koristi se tzv. "trik s maksimumom":

$$
\text{logsumexp}(\bold{x}) = a + \log\left(\sum_{i=1}^n e^{x_i - a}\right), \quad a = \max(\bold{x})
$$

Implementirajte ovu funkciju pomoću NumPy-ja za ulazni vektor `x` i testirajte je na primjeru:

```python
x = np.array([1000, 1001, 1002])
```

Bez trika s maksimumom, rezultat može ispasti `inf`, dok s trikom ostaje stabilan.

---

### 2. zadatak — Normalizacija parnih elemenata

Generirajte nasumičnu `4x4` matricu cijelih brojeva od `0` do `20`. Potom pronađite sve **parne** brojeve u matrici i normalizirajte ih tako da svaki podijelite s najvećim parnim brojem u matrici.

Ispišite matricu prije i poslije normalizacije.

---

### 3. zadatak — Agregacija po dijagonali i obradi elemenata

Generirajte matricu dimenzije `5x5` s elementima iz intervala `[0, 50)`. Zatim:

- Izdvojite glavnu dijagonalu.
- Pomnožite svaki element glavne dijagonale s 2.
- Izračunajte:
  - zbroj svih elemenata matrice,
  - srednju vrijednost elemenata sporedne dijagonale (od gornjeg desnog do donjeg lijevog kuta),
  - standardnu devijaciju svih elemenata.

