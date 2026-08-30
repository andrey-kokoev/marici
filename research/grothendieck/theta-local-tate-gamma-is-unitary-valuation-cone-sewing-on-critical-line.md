# The local Tate gamma factor is unitary valuation-cone sewing on the critical line

## Bounded question

Does the local Tate functional equation actually authorize the
inverse-integral valuation cone required by the product--ratio quarter-turn?

## Two local valuation expansions

Normalize multiplicative Haar measure by
`vol(Z_p^x)=1`. For the compact-open vacuum `1_Zp`, the local zeta integral is

\[
 Z_p^+(s)
 =\int_{\mathbb Q_p^\times}
 1_{\mathbb Z_p}(x)|x|_p^s\,d^\times x
 =\sum_{k\ge0}p^{-ks}
 =\frac1{1-p^{-s}}.
\]

Because `1_Zp` is additive-Fourier fixed, the reflected side of the local
functional equation is

\[
 Z_p^-(s)
 =Z_p(1_{\mathbb Z_p},1-s)
 =\sum_{k\ge0}p^{-k(1-s)}
 =\frac1{1-p^{s-1}}.
\]

The first series is the nonnegative valuation cone.  The second is its
oppositely polarized `1-s` chart, with the modular Haar weight retained.

## Transition function

Their ratio is

\[
 \boxed{
 \gamma_p(s)
 =\frac{Z_p^-(s)}{Z_p^+(s)}
 =\frac{1-p^{-s}}{1-p^{s-1}}.}
\]

This is the elementary unramified local gamma transition in the present
normalization.  It is not inserted as an arbitrary phase; it is forced by the
two valuation expansions of the Fourier-fixed local vacuum.

## Critical-line unitarity

Let

\[
 s=\frac12+it.
\]

Then term by term,

\[
 p^{-k(1-s)}
 =\overline{p^{-ks}},
 \qquad
 |p^{-ks}|=p^{-k/2}.
\]

Likewise the numerator and denominator of `gamma_p` are conjugate, so

\[
 \boxed{|\gamma_p(1/2+it)|=1.}
\]

Thus the critical line is a unitary sewing locus for the two local valuation
charts. The offset `1/2` is exactly half of the modular weight exchanging `s`
and `1-s`; it is not selected retrospectively by zero locations.

Pointwise unimodularity at an accidental off-line phase is not excluded by
this calculation. The structural statement is that the full vertical line is
fixed by conjugate reciprocal sewing.

## Relative seam and norm

Both cone expansions contain the valuation-zero term `k=0`.  Their relative
gluing therefore has the rank-one duplicated seam of packet 133.  On the
critical line, reflection pairs every `k>0` coefficient with equal Hilbert
norm, while the common `k=0` term is counted once after inclusion--exclusion.

This upgrades the conditional cone picture to a source-derived one:

\[
 \boxed{
 \text{local Tate vacuum}
 \to
 \text{two valuation charts}
 \to
 \text{rank-one relative seam}
 \to
 \text{unitary transition at }\Re s=1/2.}
\]

## What this proves and does not prove

The theorem explains:

1. why the inverse-integral chart is authorized;
2. why its transition contains a modular weight;
3. why the exact central offset is one half;
4. why the critical line is the unitary seam of the local coefficient system.

It does not constrain zeros of the global completed zeta function. Products
of unimodular local transitions orient the coefficient charts, but global
vacuum compression may still lose transversality.

## Next gate

Assemble the primewise cone sewings as a restricted tensor product and test
implementability of the global transition. The local seam factors are
unitary on the critical line, but an infinite product of local vacuum changes
may fail to exist as a Hilbert-space unitary—the arithmetic orthogonality
catastrophe found earlier.

The decisive observable is the same restricted-product criterion: the sum of
local vacuum displacement norms. Its divergence must be interpreted as a
relative determinant/renormalization problem, not ignored by multiplying
formal phases.
