# The Reciprocal Weighted Sectors Form a Canonical Dual Pair but Augmentation Remains an External Port

## Complementary sector spaces

Put

\[
a=\Re(s-\tfrac12)>0.
\]

On finite prime packets define

\[
H_a=\ell^2(P,p^{2a}),
\qquad
H_{-a}=\ell^2(P,p^{-2a}).
\]

The coefficient pairing

\[
\langle c,d\rangle=\sum_p\overline{c_p}d_p
\]

extends continuously and perfectly from `H_a x H_-a`, because

\[
|\langle c,d\rangle|
\le
\left(\sum_pp^{2a}|c_p|^2\right)^{1/2}
\left(\sum_pp^{-2a}|d_p|^2\right)^{1/2}.
\]

No Riesz identification has been inserted.  The direct and reciprocal
valuation sectors supply each other's continuous duals.  Reciprocal
reflection sends `a` to `-a` and exchanges the factors.  Mellin translation
acts by `p^(it)` on both factors and preserves the sesquilinear pairing.

At `a=0`, both factors become the same unweighted `l2` space.  Thus the
critical line is also the self-dual locus of the arithmetic coefficient pair,
not merely the unitary locus of each local Tate multiplier.

## Boundary-current census

The primitive coefficient row

\[
b_p^{(1)}=\frac{\log p}{\sqrt p}
\]

belongs to `H_-a` for every positive `a`, since

\[
\sum_p p^{-2a}|b_p^{(1)}|^2
=
\sum_p\frac{(\log p)^2}{p^{1+2a}}<\infty.
\]

The prime-square row

\[
b_p^{(2)}=\frac{\log p}{p}
\]

also belongs to `H_-a` for every positive `a`.  Hence both currents become
ordinary cross-sector vectors and define continuous functionals on `H_a`
through the canonical reciprocal pairing.

The augmentation row is different.  Its coefficient sequence is `1`, and

\[
\sum_p p^{-2a}<\infty
\]

holds exactly when `a > 1/2`.  Throughout the RH-relevant range
`0 < a <= 1/2`, augmentation is not represented by a vector in the reciprocal
weighted sector.

This is a structural result: primitive and square boundary currents are
internal to the two-sector Tate duality, while augmentation remains an
external control/seam port near the critical line.

## Multi-tower interpretation

The result explains why the architecture did not close as two mirrored
`3+2+1` packets alone.  Reciprocal weighted duality supplies the comparison
between their arithmetic state and current towers, but the common
augmentation/control object is not absorbed by either side in the critical
strip.  It is the final shared `+1` in

`2(3+2+1)+1`.

Trying to replace that port by the formal constant vector recreates the
divergent dual-times-dual pairing from the previous result.  Retaining it as
an independent incidence coordinate is not bookkeeping overhead; it is forced
by the sharp prime-summability threshold.

## Remaining theorem

Tensor the dual pair `H_a x H_-a` with the reciprocal `H1` trace pullback and
adjoin the augmentation port explicitly.  The next target is to show that:

1. the direct and reciprocal completed theta zero-state components land in
   the complementary weighted graph domains;
2. the primitive and square Green currents use the canonical cross pairing;
3. augmentation enters only through its declared incidence map;
4. the full mapping-cone Green identity has no remaining typed residual.

The sharp falsifier is now a completed zero-state coefficient packet that
fails its predicted `H_a` membership at a fixed off-seam `s`, or a Green term
that pairs two same-side dual currents rather than reciprocal partners.

## Result

The two open half-planes are shadows of a genuine pair of complementary
arithmetic coefficient sectors.  Their pairing is canonical, Mellin
covariant, and reciprocal.  Primitive and prime-square currents internalize
for every nonzero distance from the seam.  Augmentation does not, and its
failure occurs precisely across the critical strip.  The independent seam
control port is therefore forced rather than optional.

