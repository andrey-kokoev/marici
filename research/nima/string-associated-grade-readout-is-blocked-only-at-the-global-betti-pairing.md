# The String Associated-Grade Readout Is Blocked Only at the Global Betti Pairing

## Audit result

The first three-normal string line is not merely a local rank coincidence.
Entries 913--914 show that it is globally untwisted under its labelled
(D_3) orbit.  The local loaded boundary complex is also algebraically
controlled:

- Pochhammer regularization cancels every declared occurrencewise boundary
  factor;
- the localized two-term loaded complex is contractible;
- no additional pole support appears.

These facts do not yet construct a physical readout.  The six loaded factors
are occurrence-labelled tubular boundaries on four source walls, whereas the
native chamber hexagon has three inverse monodromy pairs.  Their total
holonomies differ.  Consequently one cannot glue the local regularizations
by pretending that they are the six facets of one associahedron.

Likewise, the available matrices

[
M_{m block},qquad
mathcal S^T,qquad
M_{m block}mathcal S^T
]

have chain-to-chain or cycle-basis variance.  None is the required
cochain-to-dual-Betti regularization map.  A bare transpose would silently
choose the missing pairing.

## Cellular reduction

Entries 1013--1016 nevertheless construct a canonical cellular candidate
(D_\bullet), up to one global Laurent unit.  It:

- commutes with both differentials of the complete hexagon complex;
- extends through the chamber two-cell;
- is Laurent-unimodular of index one;
- contributes only a flat, trivial-monodromy relative gauge.

Therefore

\[
\Omega_D=\partial_{u^{-1}}D-D\partial_u=0
\]

exactly.  Multiplying (D) by the remaining global unit cannot change this
static vanishing when that unit is constant for the boundary differential.
Thus scalar normalization is irrelevant to the selected-readout obstruction.
The only live static failure mode is that the source-normalized twisted
pairing forces a genuinely nondiagonal comparison rather than (D) up to
unit gauge.

## Exact frontier

After deriving the source-normalized twisted cycle/cochain pairing, let (S)
be its forced adjoint comparison and let (ell) be the physical Pochhammer
readout.  Compute

[
Omega=partial_HS-Spartial_G,
qquad
delta_{m phys}=ellOmega.
]

The physical question is exactly whether

[
oxed{delta_{m phys}=0}
]

on the complete maximal-flag associated-grade packet.

Thus the string lane is neither yet a third confirmation nor a
counterexample to coherence without physical rank.  It is a clean unresolved
case whose only remaining static gate is whether the global,
source-normalized Betti pairing identifies its adjoint with (D_\bullet) up
to unit gauge.  If it does, selected-readout descent follows without another
rank computation.

## Contract

`research/nima/contracts/string-associated-grade-readout-falsifier.v1.json`
