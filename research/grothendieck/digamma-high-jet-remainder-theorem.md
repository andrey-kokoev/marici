# Deep recurrence controls every gamma derivative needed by the interval jet

For positive real `z`, the digamma asymptotic remainder after the `B_16` term
has the classical Stieltjes-integral form obtained by geometrically expanding
the kernel in

\[
 \psi(z)=\log z-\frac1{2z}
 -2\int_0^\infty\frac{t}{t^2+z^2}
 \frac{dt}{e^{2\pi t}-1}.
\]

The first omitted term is `B_18/(18 z^18)`. To control derivatives safely,
use Cauchy's estimate on the disk of radius `z/2`. Factoring
`w^2+t^2=(w-it)(w+it)` bounds the complex remainder there by `2^18` times the
positive-real first-omitted value. Hence

\[
 |R^{(j)}(z)|\le
 \frac{|B_{18}|}{18z^{18}}\frac{j!2^{18+j}}{z^j}.
\]

In the completed source the argument is `z=s/2+M`, so differentiation in `s`
adds `2^-j`, cancelling the last `2^j`. Choosing recurrence target `M=1000`
yields bounds through order six all below `8.01e-49`.

This recurrence is computationally cheap—only rational reciprocal corrections
are added—and avoids relying on cancellation between gamma and eta remainder
intervals. Together with the depth-300 eta Cauchy theorem, it supplies the
analytic tails required for a directed interval jet through the continuum
oscillation order.

This theorem controls truncation only. The directed interval Taylor algebra
still has to propagate these tails on each cell; RH is not proved.

## Durable verification

- Checker: `checkers/digamma_high_jet_remainder_bound.py`
- Result: `results/digamma-high-jet-remainder-bound.json`
