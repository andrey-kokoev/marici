# Higher-coherence topology iteration 05: Krein-neutral cones absorb the residual algebraically but not on the physical reciprocal domain

## Candidate topology

Replace positive Hilbert totalization by the hyperbolic/Krein double

\[
\mathcal K_p=H_p\oplus H_p,
\qquad
J_p=\operatorname{diag}(I,-I).
\]

A higher cone can pair a residual with an opposite-sign copy. For any
self-adjoint residual operator `T`,

\[
\mathcal T=\operatorname{diag}(T,-T)
\]

vanishes on the diagonal neutral graph

\[
\Lambda_{\rm diag}=\{(f,f):f\in H_p\}.
\]

Thus indefinite topology genuinely permits a nonzero positive component to be
absorbed by a new negative higher-coherence component.

## Physical reciprocal line

The local valuation transport does not select the diagonal graph. It selects

\[
L_{p,z}(b_z)
=
\operatorname{span}\{(b_z,p^{-z}b_z)\}.
\]

Its Krein norm is

\[
[(b_z,p^{-z}b_z)]_{J_p}
=
\bigl(1-p^{-2\operatorname{Re}z}\bigr)E_p(b_z).
\]

The global reciprocal jet selects an equal-modulus neutral line. A
`J_p`-isometric based comparison between the two lines exists exactly when the
local line is neutral, hence exactly when `Re(z)=0`.

The Krein topology reformulates the terminal residual perfectly, but does not
remove it.

## Attempted higher neutralizer

One may adjoin a third coordinate `h_z` with opposite sign and impose

\[
\|h_z\|^2
=
\bigl|1-p^{-2\operatorname{Re}z}\bigr|E_p(b_z).
\]

This makes the enlarged vector neutral for every `z`. But unless `h_z` is
produced by an independently defined source map, its norm is exactly the
residual being cancelled. It is a fitted counterterm.

Even with a source-derived higher state, projecting the neutral enlarged state
back to the physical two-coordinate carrier restores the original nonzero
Krein norm. Neutrality in the extension implies confinement only if the
physical projection is itself Krein-isometric, which again forces the residual
to vanish.

## Bounded-domain obstruction

The diagonal neutral graph would require reciprocal reflection

\[
Ue^{-su}=e^{su}.
\]

On the raw theta-tail Hilbert space this operator is unbounded: the norm ratio
of the two sections grows like `exp(s log s-O(s))`. Hence the universal neutral
graph does not contain the physical reciprocal family as a bounded relation.

Passing to an unbounded closed graph is possible, but then graph-domain
membership and continuity of the Haar readout become new conditions. They do
not follow from Krein completion.

## Positivity loss

A Krein quotient can identify nonzero neutral vectors with zero. Therefore the
fact that the enlarged class is neutral does not imply that its retained base
energy vanishes. To recover confinement one needs a source-selected positive
Lagrangian or cone whose intersection with the physical line is neutral only
on the seam. Constructing precisely that selector is equivalent to the missing
rung-four comparison.

## Verdict for topology 5

Krein/Pontryagin topology is the first tested topology that can absorb the
residual algebraically without making the whole state weakly zero. However:

- the canonical neutral graph does not admit the physical reciprocal sections
  boundedly;
- an arbitrary extra negative coordinate is a fitted counterterm;
- neutralization in an enlarged carrier does not imply neutrality after
  physical projection;
- a source-selected admissible positive Lagrangian would itself be the
  confinement theorem.

Thus indefinite topology explains the geometry of the obstruction but does not
supply its missing selector.

The next nonredundant topology to test is a Hardy/graph topology for unbounded
reciprocal reflection, where boundary conjugation may replace the impossible
bounded half-line reflection.