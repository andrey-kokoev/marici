# The prime moment ellipse is strictly interior at every nonzero character

The current noncircular frontier is Grothendieck’s Gaussian first-contact
reduction. At a hypothetical double contact, the prime value and slope obey

\[
\frac{R(t,\xi)^2}{M_0(t)^2}
+
\frac{I_1(t,\xi)^2}{M_0(t)M_2(t)}
\le1.
\]

The inequality is actually strict whenever \(\xi\ne0\).

Recall

\[
R=\sum_n c_n\cos(\xi\log n),
\qquad
I_1=\sum_n c_n\log n\,\sin(\xi\log n),
\]

with \(c_n>0\) on prime powers, and

\[
M_j=\sum_n c_n(\log n)^j.
\]

Equality in the ellipse requires equality in both steps used to derive it.

First, equality in the weighted Jensen inequality requires

\[
\cos(\xi\log n)=C
\]

for every prime power \(n\).

Second, equality in weighted Cauchy–Schwarz requires

\[
\sin(\xi\log n)=\lambda\log n
\]

for every prime power \(n\).

Because the prime-power support has unbounded \(\log n\) while the sine is
bounded, necessarily

\[
\lambda=0.
\]

Thus

\[
\sin(\xi\log n)=0
\]

for every prime power, and the common-cosine condition forces all phases to
the same parity. In particular,

\[
\xi\log2\in\pi\mathbb Z,
\qquad
\xi\log3\in\pi\mathbb Z.
\]

Since \(\log2/\log3\) is irrational, this is possible only for

\[
\xi=0.
\]

Therefore

\[
\frac{R(t,\xi)^2}{M_0(t)^2}
+
\frac{I_1(t,\xi)^2}{M_0(t)M_2(t)}
<1
\qquad(\xi\ne0).
\]

## Compact strict margin

For fixed \(t>0\), the ellipse ratio is continuous in \(\xi\). Hence on every
compact character set

\[
K\subset\mathbb R\setminus\{0\},
\]

there exists

\[
\delta_{t,K}>0
\]

such that

\[
\frac{R(t,\xi)^2}{M_0(t)^2}
+
\frac{I_1(t,\xi)^2}{M_0(t)M_2(t)}
\le1-\delta_{t,K}.
\]

On a compact \(t\)-interval bounded away from zero, joint continuity gives a
common margin \(\delta_{C,K}>0\).

The margin need not remain uniform as \(|\xi|\to\infty\): simultaneous
Diophantine approximation can drive finitely many prime phases close to
alignment. Thus character coercivity is still required to confine any first
contact to a compact region.

## Contact consequence

At a double contact,

\[
R=2\sqrt{\pi t}\,A,
\qquad
I_1=-2\sqrt{\pi t}\,\partial_\xi A.
\]

Therefore every nonzero-character contact in a compact region must satisfy
the sharpened necessary inequality

\[
\left(\frac{2\sqrt{\pi t}A}{M_0}\right)^2
+
\frac{
\left(2\sqrt{\pi t}\,\partial_\xi A\right)^2
}{
M_0M_2
}
\le1-\delta_{C,K}.
\]

This identifies a genuine source-derived local margin: it comes from the
incompatibility of the \(2\)- and \(3\)-adic character phases, not from RH or
zero data.

The remaining first-contact attack now separates cleanly:

1. zero character \(\xi=0\): scalar heat-positivity gate;
2. compact nonzero characters: strict prime ellipse plus archimedean bounds;
3. large characters: coercivity preventing escape to infinity.

This is more concrete than the terminal strict-peak Weil localization, which
only verifies the equivalence once positivity is known.
