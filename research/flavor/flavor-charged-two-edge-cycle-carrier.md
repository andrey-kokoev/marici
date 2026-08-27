# Charged two-edge cycle carrier

## Bounded question

What is the smallest gauge-legal source extension that closes one genuine
rephasing-invariant cycle in the WP634 messenger incidence?

## Minimal carrier

The up- and down-type messenger hypercharges differ by one. Add one complex
color- and weak-singlet scalar

\[
\chi\sim(1,1,1)
\]

and two renormalizable cross-sector vertices,

\[
C_A\bar A_L^u\chi A_R^d,
\qquad
C_B\bar B_L^u\chi B_R^d,
\]

together with their Hermitian conjugates. Both have zero total hypercharge and
preserve the row or port representation at their respective stages.

One cross-edge is insufficient because \(\chi\) remains an incidence leaf.
With both edges, the enlarged signed incidence has twelve rows, seventeen
field labels, and exact rank eleven. Its continuous left kernel is
one-dimensional. In the canonical row ordering, a primitive kernel vector
selects the invariant

\[
\mathcal I_\chi=
{Y_S^u Z_A^d C_B\over Y_S^d Z_B^u C_A}.
\]

The modulo-two cycle kernel is also one-dimensional, so the sign of the same
closed product survives all field sign redefinitions.

## Physical typing

The carrier is electrically charged. A nonzero \(\chi\) vacuum expectation
value would break electromagnetism, so the admitted vacuum must keep
\(\langle\chi\rangle=0\) with positive charged-scalar mass squared. The cycle
is therefore a coupling/interference resource, not another vacuum sign.

This extension changes the source census. It adds charged-scalar thresholds,
new messenger transitions, loop corrections, and possible decay channels.
The complete scalar potential must forbid charge breaking on its full domain,
and the charged pole must be included in matching and widths.

## Selector boundary

WP635 repairs WP634's zero-cycle capacity and supplies a genuine internal
relative probe. It does not select the phase or magnitude of
\(\mathcal I_\chi\): the six participating coupling normalizations remain
independent source coordinates. Setting their ratio from the desired flavor
answer would be target encoding.

The next gate is to derive the lowest matched `physical16` or threshold
amplitude containing \(\mathcal I_\chi\), verify that its interference survives
finite masses and widths, and identify a calibrated charged-channel
instrument. Only then can the new cycle be classified as executable rather
than algebraically distinguishing.

## Reproduction

Run:

    python research/flavor/checkers/wp635_charged_two_edge_cycle_carrier.py

The generated result is
`research/flavor/results/wp635_charged_two_edge_cycle_carrier.json`.

