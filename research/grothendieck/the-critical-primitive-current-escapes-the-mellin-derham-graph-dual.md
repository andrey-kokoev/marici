# The critical primitive current escapes the Mellin–de Rham graph dual

## Scope correction

Ledger 3876 constructed a strictly positive finite pairing between relative
prime flux and the Mellin position row. It did not establish that the complete
critical primitive current is continuous on the polynomial `(Q,D)` graph
domain. That extension is false.

## Critical primitive current

On the positive logarithmic scale, consider

\[
T_1
=
\sum_p(\log p)p^{-1/2}\delta_{\log p}.
\]

Its reflected relative version has an identical continuity obstruction, so it
is enough to test this positive arm.

Choose one fixed smooth bump `chi`, supported in `(0,1)` and equal to one on a
smaller interval, and translate it:

\[
\chi_R(q)=\chi(q-R).
\]

For the phase-space graph norm

\[
\lVert f\rVert_{QD}^2
=\lVert f\rVert_2^2
+\lVert Qf\rVert_2^2
+\lVert Df\rVert_2^2,
\]

one has

\[
\lVert\chi_R\rVert_{QD}=O(R).
\]

The prime number theorem gives, on any fixed interior subinterval of the
translated shell,

\[
T_1(\chi_R)
\asymp
\sum_{e^{R+a}\le p\le e^{R+b}}
(\log p)p^{-1/2}
\asymp e^{R/2}.
\]

Consequently

\[
\frac{|T_1(\chi_R)|}
{\lVert\chi_R\rVert_{QD}}
\longrightarrow\infty.
\]

Thus `T_1` is not a continuous functional on the Mellin–de Rham graph space.
Adding the reflected arm does not repair this: an odd translated test isolates
the relative current with the same exponential lower bound.

## Exact recovery of the three grades

At prime-power depth `k`, the logarithmic-derivative current is

\[
T_k
=
\sum_p(\log p)p^{-k/2}\delta_{k\log p}.
\]

Prime density in logarithmic position shows the three distinct regimes.

For `k=1`, shell mass grows exponentially, as above. This is the primitive
distributional wall.

For `k=2`, the local shell mass is asymptotically constant:

\[
\sum_{e^{R/2}\le p\le e^{(R+1)/2}}
\frac{\log p}{p}=O(1).
\]

This is compatible with continuity in the position-weighted graph dual but
not with trace-class summation.

For `k>=3`,

\[
\sum_p(\log p)p^{-k/2}<\infty,
\]

so the current has finite total variation and belongs to the ordinary
connected tail.

The graph-dual test therefore reconstructs rather than removes the exact
primitive, square, and connected filtration.

## Compatibility with smooth synthesis

The smooth prime-synthesis theorem maps arithmetic packets with decay exponent
strictly greater than `1/2` into the common `(Q,D)` graph domain. The critical
primitive current has exponent exactly `1/2`. It lies on the excluded boundary,
and the translated-shell witness proves that the strict inequality cannot be
closed by continuity.

There is no contradiction:

- finite prime packets admit the positive `Q` pairing from ledger 3876;
- rapidly decaying completed packets enter the phase-space graph domain;
- the undamped critical primitive completion does not define a graph-dual
  covector.

## Surviving architecture

The completed observer must retain a typed sum

\[
\mathcal B_{\mathrm{prim}}^{\mathrm{exp}}
\oplus
\mathcal B_{\mathrm{sq}}^{\mathrm{graph}}
\oplus
\mathcal B_{\ge3}^{\mathrm{tv}}.
\]

The `(Q,D)` phase-space observer governs the square and connected channels and
every finite primitive packet. The primitive completion requires either an
independent exponential boundary torsor or a properly supported comoving
prime-scale correspondence. It cannot be absorbed into a polynomial graph
norm.

## Result

The first real completion obstacle has been found. The finite relative-flux
observer is correct, but its critical primitive limit escapes the
Mellin–de Rham graph dual exponentially. The square current is the borderline
graph-grade wall, and higher currents are ordinary tails. Any RH construction
must sew these three grades without forcing the primitive current into the
wrong topology.
