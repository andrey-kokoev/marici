# The total-energy thimble does not link the v_alg dlog divisor generically

The source-selected quotient line represented by \(v_{\rm alg}\) has logarithmic divisor

\[
D=(E^2-X_1X_2)(E^2+X_1X_2)
=E^4-X_1^2X_2^2.
\]

Restricting to the total-energy cusp gives

\[
D|_{E=0}=-X_1^2X_2^2.
\]

Therefore, on the generic cusp locus

\[
X_1X_2\ne0,
\]

both components of the \(v_{\rm alg}\) divisor are disjoint from \(E=0\):

\[
(E^2-X_1X_2)|_{E=0}=-X_1X_2\ne0,
\]

\[
(E^2+X_1X_2)|_{E=0}=X_1X_2\ne0.
\]

Equivalently,

\[
\operatorname{Res}_{E=0}d\log D=0,
\]

and a sufficiently small loop around \(E=0\) has zero winding around either \(D\)-component.

Hence a total-energy thimble localized at a generic cusp point has zero geometric linking number with the \(v_{\rm alg}\) dlog divisor.

If the integral dual \(v_{\rm alg}^\vee\) is the integral linking functional associated with this source-proved divisor, this gives the second parity directly:

\[
\langle2m,v_{\rm alg}^\vee\rangle\equiv0\pmod2.
\]

Combined with the odd \(e_6\) component, the resulting ordered class would be

\[
(a,b)=(1,0).
\]

One comparison statement remains necessary before promoting this to an unconditional integral answer: the rational identity \(\nabla(v_{\rm alg}\bmod e_6)=d\log D\) must be upgraded to an integral Betti statement identifying \(v_{\rm alg}^\vee\) with divisor linking. The support and local winding are now exact; only that integral normalization is not yet proved.

Certificate:

- `research/voevodsky/checkers/total_energy_vs_valg_divisor_linking.py`;
- `research/voevodsky/results/total_energy_valg_divisor_linking.json`.
