# Oriented relational frame cocycle

Pairwise overlaps close the metric and conditioning problem, but they leave a
reflection kernel. A qubit frame and its complex conjugate have identical
pairwise fidelities. On the Bloch sphere this is an improper orthogonal
reflection. It is not, in general, a common unitary gauge transport.

Therefore pairwise relational data do not yet establish that two probe
realizations belong to the same physical unitary orbit.

The smallest oriented witness is a triple Bargmann invariant

    B_ijk = inner(psi_i, psi_j)
            inner(psi_j, psi_k)
            inner(psi_k, psi_i).

It is unchanged by independent phase choices for each state and by a common
unitary. Complex conjugation sends it to its complex conjugate, reversing its
imaginary part. For a non-coplanar tetrahedral triple this imaginary part is
nonzero, so one triple cocycle separates the mirror hostile that every
pairwise fidelity misses.

This adds a categorical distinction:

1. pairwise overlaps reconstruct the frame up to the orthogonal group O(3);
2. one nonzero oriented triple cocycle selects an SO(3) component;
3. the qubit lift then identifies the common-unitary class up to its central
   phase.

Finite uncertainty must be preregistered. If every measured Hilbert--Schmidt
overlap differs from its target by at most delta, then every syndrome Gram
entry differs by at most 2 delta. For four probes the spectral perturbation is
at most 8 delta. Hence a target frame with smallest Gram eigenvalue lambda_min
remains certified full rank whenever

    delta < lambda_min / 8.

For the tetrahedron this gives delta less than 1/6. For the selector frame it
gives

    delta < (5 - sqrt(13)) / 16,

approximately 0.087153. The frozen working threshold delta equal to 0.01 lies
inside both gates. The corresponding conservative condition-number bound is

    sqrt((lambda_max + 8 delta) / (lambda_min - 8 delta)).

The pairwise overlap instrument and the oriented triple instrument have
different jobs. The former certifies metric conditioning; the latter rejects
antiunitary reflection. Neither instrument is claimed physically executed.
