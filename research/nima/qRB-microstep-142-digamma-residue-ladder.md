# qRB microstep 142: digamma residue ladder

The digamma poles occur at

$$
1/4+iu/2=-k,
\qquad k=0,1,2,\ldots,
$$

so the corresponding contour poles are

$$
 u_k=i(2k+1/2).
$$

Each has the same residue in the `u` variable:

$$
\operatorname{Res}_{u=u_k}\psi(1/4+iu/2)=2i.
$$

A contour shift crossing the first `r` poles therefore adds a finite residue sum of Gaussian pole terms

$$
\sum_{k=0}^{r-1}\pm e^{-t(u_k-\xi)^2},
$$

with signs determined by the crossing orientation. The nearest term is related to the polar endpoint evaluation; higher terms are genuine gamma-pole corrections and must not be relabeled as endpoint data.

Status: complete residue locations and coefficients recorded; global contour assembly remains to be checked.
