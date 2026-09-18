# qRB microstep 127: endpoint pair summability falsifier

The endpoint row satisfies

$$
0\le e_{nm,b}
\le\int_0^\infty e^{-\pi(n^2+m^2)x^2}\,dx
=\frac1{2\sqrt{n^2+m^2}}.
$$

This bound is not summable over all ordered pairs: the number of pairs with `sqrt(n^2+m^2)` of size `r` is proportional to `r`, while each bound is of order `1/r`.

Therefore the endpoint pair channel cannot be represented by a naive unweighted absolute sum. It must remain projective, weighted, or relative after boundary aggregation.

Status: unweighted global endpoint pair summability rejected; projective endpoint typing is necessary.
