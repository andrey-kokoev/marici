# 1005 — The Minus Primitive Is Regular After Correct Basis Transport

## Defect repaired

Entry 1004 compared two index sets without transporting between their bases:

- Entry 1002's primitive support \(\{4,5\}\) is in the dense six-chamber basis;
- Entry 949's repeated-wall occurrences \(\{4,5\}\) are in the sparse source-occurrence basis.

Numerical equality of these labels does not identify them.

## Frozen permutation

Entry 974 fixes the occurrence-to-dense permutation

\[
(0,1,2,3,4,5)
\longmapsto
(4,1,0,5,3,2).
\]

Its inverse sends the primitive's dense support to

\[
\boxed{
\{4,5\}_{\rm dense}
\longmapsto
\{0,3\}_{\rm occurrence}.
}
\]

These source occurrences carry the singleton walls

\[
m_0=(ZA_2)^2-1,
\qquad
m_3=(A_3/Z)^2-1,
\]

each with Fitting valuation one.

## Comparison with the minus recombination locus

The \((--)\) recombination instead imposes

\[
(ZA_2B_{24})^2=1,
\qquad
(A_3B_{34}/Z)^2=1.
\]

At a generic point of this locus, neither \(m_0\) nor \(m_3\) vanishes.  The two half-monodromy regularization coefficients needed by the primitive are therefore regular.

Hence Entry 1002's primitive remains admissible in the generic closed twisted-cycle lattice, and

\[
\boxed{
[d_{--}|_{Z_{--}}]=0
\quad\text{also after generic Betti regularization}.
}
\]

## Result

Entry 1004 is retracted.  Its proposed valuation-two resonance arose entirely from a mixed-basis identification.

The corrected string-sector picture is:

- the local \((--)\) normal modification is nonzero;
- the restricted three-edge chamber arc is cellularly exact;
- its primitive regularizes without a pole at generic \((--)\) recombination;
- therefore the arc supplies no generic supported Betti class that could equal the normal modification.

The two structures remain independent unless another source-derived comparison is constructed.

## Deeper intersections

The primitive regularization can become singular only on the proper intersections

\[
Z_{--}\cap\{(ZA_2)^2=1\}
\quad\text{or}\quad
Z_{--}\cap\{(A_3/Z)^2=1\}.
\]

Those are existing higher-codimension carrier strata.  They do not alter the generic result and should be tested separately only if a source observable requires them.

## Epistemic lesson

\[
\boxed{
\text{equal serialized indices in different bases do not define a support identification.}
}
\]

Every future support comparison must transport labels through the frozen occurrence-to-dense map before applying valuations or nearby-cycle operations.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_minus_twisted_cycle_lattice_gate.rs`
- `research/benincasa/string-six-point-minus-twisted-cycle-lattice-gate.json`

The repaired checker inverts Entry 974's exact permutation, maps the primitive to occurrences \(0,3\), and verifies their two valuation-one monodromy walls against Entry 949.

Epistemic graph event: `ev-000000000624-53686c7e-25ab-4b20-a5df-113204dfda6f`.
