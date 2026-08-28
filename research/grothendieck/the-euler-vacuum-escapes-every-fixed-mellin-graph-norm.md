# The Euler Vacuum Escapes Every Fixed Mellin Graph Norm

## Logarithmic generator at finite cutoff

On \(\mathcal H=\ell^2(\mathbb P)\), let

\[
Qe_p=(\log p)e_p.
\]

For the normalized Euler cutoff

\[
v_X=H_X^{-1/2}
\sum_{p\le X}p^{-1/2}e_p,
\qquad
H_X=\sum_{p\le X}\frac1p,
\]

the first two \(Q\)-moments are

\[
m_X=\langle v_X,Qv_X\rangle
=\frac1{H_X}\sum_{p\le X}\frac{\log p}{p}
\]

and

\[
s_X=\langle v_X,Q^2v_X\rangle
=\frac1{H_X}\sum_{p\le X}\frac{(\log p)^2}{p}.
\]

Prime-number-theorem partial summation gives

\[
H_X=\log\log X+O(1),
\]

\[
\sum_{p\le X}\frac{\log p}{p}
=\log X+O(1),
\]

and

\[
\sum_{p\le X}\frac{(\log p)^2}{p}
=\frac12(\log X)^2+O(\log X).
\]

Hence

\[
m_X\sim\frac{\log X}{\log\log X}
\]

and

\[
s_X\sim\frac{(\log X)^2}{2\log\log X}.
\]

## Centering does not repair the graph norm

The optimal scalar subtraction is \(Q-m_XI\).  Its squared norm on the source
vacuum is the variance

\[
\sigma_X^2
=\left\|(Q-m_XI)v_X\right\|^2
=s_X-m_X^2.
\]

Since \(m_X^2\) is lower order than \(s_X\),

\[
\sigma_X^2
\sim
\frac{(\log X)^2}{2\log\log X}.
\]

Therefore

\[
\left\|(Q-m_XI)v_X\right\|
\longrightarrow\infty.
\]

The normalized Euler vacuum is not bounded in the graph norm of \(Q\), even
after removing its best cutoff-dependent scalar drift.  Thus the missing
first-order Mellin germ from Entry 3938 cannot be restored by adjoining the
ordinary logarithmic generator to the Haar-corona Hilbert space.

## Cutoff rescaling is not an all-order repair

One can force unit variance with

\[
\widetilde Q_X=\sigma_X^{-1}(Q-m_XI),
\]

but this changes the unit of vertical differentiation with the cutoff.  More
decisively, it does not stabilize the higher jet tower.

For the third raw moment,

\[
\frac1{H_X}
\sum_{p\le X}\frac{(\log p)^3}{p}
\sim
\frac{(\log X)^3}{3\log\log X}.
\]

After centering and division by \(\sigma_X^3\), the third standardized moment
grows on the order of

\[
\sqrt{\log\log X}.
\]

Hence a normalization chosen to retain the first derivative makes the next
jet singular.  No single cutoff rescaling produces a stable all-order Mellin
derivative module.

## Typed conclusion

The completion hierarchy now has three sharply distinct layers:

1. finite Mellin shifts survive as the discrete Haar-corona algebra;
2. the first logarithmic generator escapes every fixed Hilbert graph norm;
3. higher logarithmic jets escape at increasingly incompatible scales.

The missing primitive channel must therefore be a rigged, filtered, or
distributional boundary object that retains the whole scale tower.  It cannot
be a single Hilbert-Sobolev correction.

This explains why the primitive \(k=1\) current could not be absorbed into the
Hilbert seam state.  It is not merely larger in norm; it carries a different
regularity type.

## Relation to the finite seam module

Nima's finite module theorem remains intact.  Mellin conjugation of the
rank-one seam carrier is exact, and Haar conditional expectation sends it to
the diagonal prime-square current.  That is a zeroth-order statement about
finite shifts.

The present obstruction begins only when one differentiates that action.  The
conditional expectation closes, but its infinitesimal logarithmic module does
not survive Euler-vacuum completion.

## Falsifier and next gate

Any proposed fixed graph norm for the primitive corona channel must keep

\[
\|(Q-a_XI)v_X\|
\]

bounded for some scalar counterterm \(a_X\).  The minimum occurs at
\(a_X=m_X\) and still diverges as

\[
\frac{\log X}{\sqrt{2\log\log X}}.
\]

This rules out every scalar-renormalized fixed Hilbert graph norm.

The next gate is to construct a filtered jet object whose \(r\)-th level uses
the source-derived moment scale

\[
\sum_{p\le X}\frac{(\log p)^r}{p},
\]

and whose transition maps preserve Mellin translation, primitive finite-part
data, and theta--Tate sewing simultaneously.
