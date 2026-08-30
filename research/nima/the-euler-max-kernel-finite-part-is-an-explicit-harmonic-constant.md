# The Euler max-kernel finite part is an explicit harmonic constant

The diagonal normalized Cauchy Gram can be written using generalized harmonic
numbers. Let

\[
T(\sigma)
=
\sum_{n,m\ge1}
\frac{
e^{-\frac12|\log(n/m)|}
}{
n^{1/2+\sigma}m^{1/2+\sigma}
}.
\]

Ordering by the larger label gives

\[
T(\sigma)
=
\sum_{n\ge1}
\frac{
2H_n^{(\sigma)}-n^{-\sigma}
}{
n^{1+\sigma}},
\qquad
H_n^{(\sigma)}=\sum_{m\le n}m^{-\sigma}.
\]

At \(\sigma=1/2\),

\[
H_n^{(1/2)}
=
2\sqrt n+\zeta(1/2)+\frac1{2\sqrt n}
+O(n^{-3/2}).
\]

Hence

\[
\frac{
2H_n^{(1/2)}-n^{-1/2}
}{
n^{3/2}}
=
\frac4n+O(n^{-3/2}).
\]

The unnormalized finite part is therefore the absolutely convergent constant

\[
C_{\mathrm E}
=
4\gamma
+
\sum_{n\ge1}
\left[
\frac{
2H_n^{(1/2)}-n^{-1/2}
}{
n^{3/2}}
-\frac4n
\right].
\]

Equivalently,

\[
T(\sigma)
=
\frac4{2\sigma-1}
+
C_{\mathrm E}
+
O(2\sigma-1).
\]

Now normalize by

\[
D(\sigma)=\zeta(1+\sigma)^2.
\]

Writing \(z=\zeta(3/2)\) and \(z'=\zeta'(3/2)\), one has

\[
D(\sigma)
=
z^2+(2\sigma-1)zz'+O((2\sigma-1)^2).
\]

Therefore the normalized Euler Gram satisfies

\[
G_{\mathrm E}(\sigma,\sigma)
=
\frac4{z^2}\frac1{2\sigma-1}
+
\left(
\frac{C_{\mathrm E}}{z^2}
-\frac{4z'}{z^3}
\right)
+
O(2\sigma-1).
\]

This closes the Euler finite-part calculation without invoking Xi zeros.

Under direct parameter and amplitude matching, the quarter-heat prediction for
the regular constant is

\[
-\frac{\pi}{3z^2}.
\]

Thus strict equality of the simplest quarter-density interface would require

\[
C_{\mathrm E}
-
4\frac{z'}{z}
=
-\frac{\pi}{3}.
\]

This is now a concrete scalar audit. It must be checked before promoting the
leading-pole match to a full Green comparison.

Failure of this identity would not refute quarter-density itself. It would
show that the interface needs an additional finite boundary return—precisely
the Todd/endpoint/archimedean cell anticipated by the typed construction.
Success would mean that the first regular annotation is already carried by
the quarter-heat lattice Gram.

The next step is a certified evaluation or analytic reduction of
\(C_{\mathrm E}\), followed by classification of any discrepancy into the
authorized finite boundary ports.
