# The quarter-heat regular part begins with the Todd coefficient \(-1/12\)

The quarter-density heat Gram admits a sharper boundary expansion than its
leading Hankel pole.

Set

\[
Q(u)=\sum_{n\ge1}n e^{-\pi u n^2}.
\]

Euler--Maclaurin applied to \(f_u(x)=x e^{-\pi u x^2}\) gives

\[
\sum_{n\ge1}f_u(n)
=
\int_0^\infty f_u(x)\,dx
-\frac{B_2}{2!}f_u'(0)
-\frac{B_4}{4!}f_u'''(0)
+\cdots.
\]

Since

\[
\int_0^\infty x e^{-\pi u x^2}\,dx=\frac1{2\pi u},
\qquad
f_u'(0)=1,
\qquad
f_u'''(0)=-6\pi u,
\]

one obtains

\[
Q(u)
=
\frac1{2\pi u}
-\frac1{12}
-\frac{\pi u}{120}
+O(u^2)
\]

as an asymptotic expansion at \(u\downarrow0\).

For the polarized heat Gram, \(u=(r+t)/2\), hence

\[
\langle g_r,g_t\rangle
=
\frac1{\pi(r+t)}
-\frac1{12}
-\frac{\pi(r+t)}{240}
+O((r+t)^2).
\]

Thus after removing the continuum Hankel pole, the first regular coefficient
is exactly

\[
-\frac1{12}.
\]

This is the Bernoulli/Todd coefficient already appearing in the additive
lattice boundary calculus. The quarter-density heat lift therefore does not
merely match the Euler pole exponent; its first regular return lands in a
previously authorized arithmetic boundary coordinate.

After applying the amplitude normalization

\[
c_{\mathrm{ET}}=\frac{2\sqrt\pi}{\zeta(3/2)},
\]

the normalized regular constant becomes

\[
-\frac{c_{\mathrm{ET}}^2}{12}
=
-\frac{\pi}{3\zeta(3/2)^2}.
\]

The Euler-side max-kernel should now be expanded to the same order. A valid
quarter-density naturality cell must match:

1. the pole coefficient \(4/\zeta(3/2)^2\);
2. the regular Todd coordinate, including the scale-change contribution;
3. the remaining bounded kernel as a typed relative form.

This is much stronger than matching the leading divergence. It tests the
first finite boundary annotation after continuum elimination.

One warning remains. The appearance of \(-1/12\) does not itself prove that
the source Todd port is this coefficient: Euler--Maclaurin naturally produces
Bernoulli numbers in many unrelated sums. Authority requires the two-axis
additive/multiplicative comparison cell to identify the coefficient.

The minimal hostile matches the pole exactly but changes the lattice sampling
by a half-shift. Its leading integral is unchanged, while the Bernoulli
boundary constant changes. Such a hostile passes the continuum Hankel audit
and fails the endpoint/Todd audit.

The next calculation is therefore the Euler max-kernel finite part at
\(\sigma+\tau=1\), in the same frozen normalization and parameter frame.
