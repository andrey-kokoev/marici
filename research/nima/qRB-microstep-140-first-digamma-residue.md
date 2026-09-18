# qRB microstep 140: first digamma-pole residue

The nearest pole occurs when

$$
1/4+iu/2=0,
\qquad u=i/2.
$$

Since the digamma residue in its argument is `-1` and `d(1/4+iu/2)/du=i/2`, the residue in the `u` variable is

$$
\operatorname{Res}_{u=i/2}\psi(1/4+iu/2)=2i.
$$

Consequently, shifting the Gaussian contour across this pole adds a finite term proportional to

$$
 e^{-t(i/2-\xi)^2},
$$

with the sign determined by the direction of contour crossing and the global `1/(4 pi)` normalization. The opposite crossing supplies the reflected term.

These residues must be combined with the endpoint polar evaluations; they are not additional free spectral contributions.

Status: first residue coefficient in the contour variable computed; orientation sign and complete endpoint cancellation remain to be checked.
