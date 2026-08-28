# The RH defect is the gap between total infinity charge and seam-fold charge

## Two independently typed counts

Let `N_tot(T)` count all nontrivial zeros of the completed zeta function with

\[
0<\operatorname{Im}\rho\le T,
\]

including multiplicity. Let `N_seam(T)` count those zeros on
`Re(s)=1/2`, again including multiplicity through the complete seam germ rather
than sign changes alone. Finally, let `N_+(T)` count zeros with
`Re(s)>1/2` in the same height range.

These counts come from different observer towers:

- `N_tot` is the outer contour or projective-infinity divisor budget;
- `N_seam` is the indented-boundary fold budget of the seam germ;
- `N_+` is the forbidden interior charge in the right sector.

## Exact saturation identity

Reciprocal reflection pairs every zero strictly to the right of the seam with
a zero of equal multiplicity strictly to the left. Seam zeros are fixed.
Therefore

\[
N_{\mathrm{tot}}(T)
=
N_{\mathrm{seam}}(T)+2N_+(T),
\]

provided `T` is not itself a zero ordinate. Equivalently, define the
saturation defect

\[
\Delta_{\mathrm{sat}}(T)
=
N_{\mathrm{tot}}(T)-N_{\mathrm{seam}}(T).
\]

Then

\[
\Delta_{\mathrm{sat}}(T)=2N_+(T)\ge0.
\]

Thus RH is equivalent to

\[
\Delta_{\mathrm{sat}}(T)=0
\]

for every admissible height `T`.

## Relation to half-indices

In one open sector, every seam zero contributes half its multiplicity through
the indented contour, whereas every interior zero contributes its full
multiplicity. Reciprocal doubling restores the preceding integer identity.

The infinity-cap current of the sector phase law supplies the total budget;
the seam-germ indentation supplies the boundary half-budget. Their mismatch
is not an arbitrary analytic error. It is exactly the interior divisor count.

## Why this is a useful reformulation

The two sides can be constructed without searching the two-dimensional strip
for zeros:

1. the completed source and its outer contour determine `N_tot`;
2. the one-dimensional seam germ and its jets determine `N_seam`, including
   even multiplicities;
3. reciprocal symmetry proves that their difference is an even nonnegative
   integer.

This is stronger than comparing scalar signs but remains weaker than a proof.
The explanatory target is now a source-derived saturation map from the
projective-infinity current onto the seam-fold current.

Such a map must preserve multiplicity and orientation. Merely matching the
leading Riemann--von Mangoldt asymptotic is insufficient: a finite or sparse
off-seam packet changes `Delta_sat` while leaving the leading density
unchanged.

## Multi-tower interpretation

The minimal complete architecture is not one phase tower. It is:

1. an outer/infinity tower carrying total divisor supply;
2. a seam-germ tower carrying realized boundary folds;
3. a reciprocal control tower proving pairwise accounting;
4. a comparison tower whose readout is `Delta_sat`.

The comparison readout is nonnegative and integer-valued before any proposed
positivity theorem. The missing force is surjectivity: every unit of global
divisor supply must be realized as seam incidence.

## Hostile test

A reciprocal/conjugate multiplier inserting one generic off-seam quartet adds
four to `N_tot`, adds zero to `N_seam`, and therefore adds four to
`Delta_sat`. It preserves the scalar functional equation but fails saturation
immediately.

## Scope

This packet proves the exact counting identity and identifies the saturation
map required for an explanatory proof. It does not construct that map from
theta data, prove its surjectivity, or prove RH.
