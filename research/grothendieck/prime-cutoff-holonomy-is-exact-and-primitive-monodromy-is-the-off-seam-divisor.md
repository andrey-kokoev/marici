# Prime-Cutoff Holonomy Is Exact and Primitive Monodromy Is the Off-Seam Divisor

## Normalized finite-cutoff coherencer

For each prime define the local Euler section

$$
E_p(s)=(1-p^{-s})^{-1}.
$$

Its typed determinant decomposition is

$$
E_p(s)
=\exp\left(p^{-s}+\frac12p^{-2s}\right)
\det_3(I-p^{-s})^{-1}.
$$

Every component tends to one as $\operatorname{Re}s\to+\infty$. This is the
source basepoint normalization.

For a finite prime set $X$, let $C_{X,p}=E_p$ be the inclusion multiplier for
adding $p\notin X$. Since distinct prime factors act on distinct diagonal
labels,

$$
C_{X\cup\{p\},q}C_{X,p}
=C_{X\cup\{q\},p}C_{X,q}.
$$

Therefore the square holonomy is exactly

$$
H_{X;p,q}=1,
$$

not merely spectrally constant. The same equality holds separately for the
primitive exponential, square exponential, and third-order determinant tail.
The prime-diagonal construction thus passes both of Nima's gates:

- zero logarithmic connection curvature;
- identity basepoint holonomy for every two-prime order square.

No phase ambiguity remains at finite support.

## Primitive monodromy in the open RH half-sector

Möbius inversion gives, chartwise,

$$
P(s)=\sum_{m\ge1}\frac{\mu(m)}m\log\zeta(ms).
$$

In the open half-sector $\operatorname{Re}s>1/2$, every term with $m\ge2$ is
holomorphic: nontrivial zeta zeros scale to real part strictly below $1/2$,
the pole scales to $1/m\le1/2$, and trivial zeros remain to the left.
Consequently

$$
P(s)-\log\zeta(s)
$$

is single-valued and holomorphic locally throughout that open sector away
from the ordinary zeta singularities.

For any small loop $\gamma$ in the sector avoiding $s=1$,

$$
\frac1{2\pi i}\oint_\gamma P'(s)\,ds
=\frac1{2\pi i}\oint_\gamma\frac{\zeta'(s)}{\zeta(s)}\,ds.
$$

Thus primitive-current monodromy counts the off-seam zeta divisor exactly,
with multiplicity. There are no Möbius-scaled ghost singularities in the open
right half-sector. The completion pole at $s=1$ is separately removed by the
archimedean endpoint carrier.

This produces a precise puncture formulation:

> An off-seam zero is exactly a nontrivial integer holonomy of the normalized
> primitive-current connection in the open completed sector.

Reciprocal sewing gives the corresponding statement in the left sector.

## What has and has not been proved

The normalized finite Euler connection is coherent, and the primitive
monodromy is a faithful encoding of the off-seam divisor. This does not prove
that the holonomy vanishes. The missing theorem is now cleanly separated from
section authority and regularization:

1. construct the completed primitive-current connection directly from the
   theta/Tate boundary module;
2. show that the archimedean and reciprocal coherencers extend the exact
   finite prime-square holonomies through completion;
3. derive, without using zeta zeros, that every loop contained in either open
   sector has identity holonomy;
4. permit nontrivial holonomy only when the loop meets the common seam;
5. identify this holonomy with the index of the fixed completed self-adjoint
   operator rather than merely with $\zeta'/\zeta$.

Item 3 is RH in primitive-current language unless supplied by an independent
source contraction or conservation law. The value of the reduction is that
all normalization, common-factor, and ghost-singularity ambiguities have now
been removed. The sole unresolved force is open-sector flat triviality after
completion.
