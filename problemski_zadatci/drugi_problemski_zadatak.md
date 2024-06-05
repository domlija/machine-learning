### Problemski zadatak

U ovom problemskom zadatku će se ispitivati vaše znanje `sklearn` bibliotike. Potrebno je pomoću funkcije `sklearn.datasets.make_classification` stvoriti dva skupa za treniranje. Argumenti funkcije su sljedeći

```py
from sklearn.datasets import make_classification

X_1, y_1 = make_classification(n_samples=30,
                          n_features=2,
                          n_informative=2,
                          n_redundant=0)

X_2, y_2 = make_classification(n_samples=120,
                          n_features=2,
                          n_informative=2,
                          n_redundant=0,
                          n_clusters_per_class=1)
```

Potrebno je naučiti algoritam logističke regresije BEZ polinomnih preslikavanja, nacrtati decizijske granice u oba slučaja i kratko komentirati rezultat. Također je potrebno izračunati `accuracy`. Slobodno iskoristite funkcije `plot_2d_clf_problem` s predavanja.