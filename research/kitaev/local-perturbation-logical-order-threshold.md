# Local perturbations: exact logical-order threshold

Status: exact finite code-distance theorem for `L=2,3,4`; formal
perturbative-path interpretation, not a convergence theorem.

## Perturbation class

Let

\[
V=\sum_e(a_eX_e+b_eZ_e+c_eY_e)
\]

with arbitrary coefficients.  An order-`r` monomial in local perturbation
terms is a Pauli supported on at most `r` edges.  The toric CSS centralizer
conditions separate its `X` and `Z` components.

## Exact threshold

For each checked lattice, no nontrivial residue-free `X` or `Z` logical has
weight below `L`, while exactly `2L` straight representatives first appear at
weight `L` in each channel.  Consequently any Pauli monomial of order
`r<L`, after projection to the code space, is either zero or a scalar
stabilizer action.  It cannot split or rotate logical sectors.

Order `L` is the first combinatorially permitted logical contribution.  The
source quantity controlling this threshold is code distance, not the local
syndrome rank.  This gives an exact explanation for why logical splitting is
high order without asserting a perturbation-series coefficient or bound.

## Constructor obstruction

A marked `Z` Wilson loop overlaps `L` terms of a uniform local `X` field and
therefore does not commute with the perturbed Hamiltonian.  Its homology class
and controlled-string constructor remain definable, but the bare operation is
not a conserved QND port.

A physical continuation requires a source-derived dressed operator and
dressed pointer coupling, plausibly through quasi-adiabatic/spectral-flow
transport.  The present source packet supplies neither.  Substituting the
bare Wilson projector would preserve the desired effect algebra by decree
while failing the dynamical instrument gate.

## Falsifiers and limits

The exact theorem fails if a nontrivial centralizer class occurs below weight
`L` or no class occurs at weight `L`.  Its perturbative interpretation fails
if the admitted local terms have support larger than one edge without the
order bound being adjusted.

No convergence radius, gap bound, coefficient of the order-`L` term,
exponential splitting estimate, or dressed instrument is claimed.

