# Salam--Sezgin fixes relative orientation and Minkowski descent but leaves scale and charge fibers: WP791

## Question

Does six-dimensional chiral gauged supergravity supply the unified
gauge--gravity source requested by WP790?

The Salam--Sezgin theory admits a supersymmetric
\(M_4\mathbin{\times}S^2\) vacuum and an exact consistent Pauli reduction to
four-dimensional \(N=1\) supergravity, an \(SU(2)\) vector multiplet, and a
scalar multiplet. The complete reduction is given by
[Gibbons and Pope](https://arxiv.org/abs/hep-th/0307052).

## The BPS source fixes relative orientation

The supersymmetric flux is

\[
F=\frac{1}{2g}\Omega_2,
\qquad
\int_{S^2}\Omega_2=4\pi.
\]

For the minimally charged fermions,

\[
\frac{g}{2\pi}\int_{S^2}F=1.
\]

The gauge-covariantly constant internal spinor obeys the positive chirality
projector

\[
\sigma_3\eta=+\eta.
\]

Reversing the monopole requires the opposite internal chirality. Once the
six-dimensional \(N=(1,0)\) source is admitted, the mirror flux is not another
BPS state of that same chiral sector. This is the first genuine
non-mirror-completable orientation selector in the current branch.

The sign remains relational: reversing the entire six-dimensional chirality
would produce the mirror theory. The construction does not reveal an
orientation independent of the chiral source.

## Gauge--gravity parallelization is real

The same coupling \(g\) appears in the fermion charge, scalar potential,
monopole, sphere curvature, and reduction ansatz. The round sphere is
normalized by

\[
R_{mn}=8g^2g_{mn}.
\]

Unlike WP790's generic Einstein--Maxwell packet, the curvature, flux, and
uplift coefficients are no longer independent. The vacuum is Minkowski and
preserves four-dimensional \(N=1\) supersymmetry.

## The scale fiber survives as a massless scalar

The exact reduction retains a scalar multiplet. Its constant mode \(\phi_0\)
has no classical potential, while the physical Kaluza--Klein scale is
proportional to

\[
M_K=g e^{\phi_0/2}.
\]

Changing \(\phi_0\) at fixed \(g\) changes the physical threshold. The
simultaneous reparameterization

\[
g\longmapsto\rho g,
\qquad
\phi_0\longmapsto\phi_0-2\log\rho
\]

leaves \(M_K\) invariant, confirming that only the combination is physical;
it does not select its numerical value. Gibbons and Pope explicitly identify
this scale freedom and the retained scalar.

## Unit flux does not derive three families

For a matter field of integer charge \(q\), the two-dimensional index is

\[
\operatorname{ind}D_q=q.
\]

The same unit BPS monopole therefore gives one family for \(q=1\) and three
for \(q=3\). Salam--Sezgin quantizes the monopole but does not by itself select
the matter charge three. The generation input has moved from flux magnitude
to the charge lattice.

Higher-derivative extensions also distinguish the unit supersymmetric
monopole from nonunit nonsupersymmetric backgrounds; see
[Pang, Pope, and Sezgin](https://arxiv.org/abs/1204.1060). This protects the
unit BPS statement but does not fix the flavor charge.

## Global-vacuum and instrument gates

The \(M_4\mathbin{\times}S^2\) solution is not the only supersymmetric vacuum
of the six-dimensional theory. A continuously squashed
\(AdS_3\mathbin{\times}S^3\) family exists, and the Minkowski vacuum is a
limit within that larger family; see
[Guven, Liu, Pope, and Sezgin](https://arxiv.org/abs/hep-th/0306201).

The consistent reduction is exact classical transport, but its massless
sector is not a flavor detector. No map from its \(SU(2)\) vector/scalar
records to physical16 production and decay channels has been derived.

## Classification

Salam--Sezgin supplies:

- a non-mirror-completable relative orientation selector;
- unit flux;
- gauge--gravity coefficient parallelization;
- a supersymmetric Minkowski compactification;
- exact consistent classical reduction.

It does not yet supply:

- charge three rather than another integer matter charge;
- a selected dilaton or Kaluza--Klein scale;
- a strict full vacuum or quantum RG basin;
- completed localized thresholds;
- a calibrated physical16 instrument.

The next source must use the anomaly-complete chiral matter packet to derive
charge three and lift \(\phi_0\), without destroying the BPS monopole or
consistent reduction.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp791_salam_sezgin_chirality_scale_charge_fiber.py

Generated result:
research/flavor/results/wp791_salam_sezgin_chirality_scale_charge_fiber.json
