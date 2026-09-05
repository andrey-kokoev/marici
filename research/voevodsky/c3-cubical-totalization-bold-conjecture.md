# C3-equivariant cubical totalization: bold conjecture and first falsifier

## Problem

Can the three RH coherence pyramids be recovered as coordinate projections of one categorically complete cubical object rather than as separately assembled structures?

## Bold conjecture

There is a \(C_3\)-equivariant cubical object with independent realization, underdetermination, and over-realization directions such that

\[
T_i:\mathsf{Over}_i\simeq\mathsf{Under}_{i+1}
\]

for every counterclockwise edge, the triple composite is homotopic to the identity, and the global coherence fiber is contractible. Its totalization recovers the analytic, arithmetic, and raw-probe pyramids without additional choices.

## Named rivals

1. adjacent over- and under-fibers have different local dimension or homotopy type;
2. the three proposed coordinates are dependent, so the cube degenerates;
3. pairwise equivalences exist but the three-cycle carries a nontrivial central residue;
4. the coherence fiber is inhabited but noncontractible;
5. completion is not preserved by a face map.

## Strongest falsification attempt

Test the edge \(C\to A\) on the atomic family. Let

\[
G_A(s)=K_s(t,z)=e^{-(t+s)a^2}\cos(az),
\qquad a>0.
\]

The derivative

\[
\partial_sG_A=-a^2e^{-(t+s)a^2}\cos(az)
\]

is nonzero, so \(G_A\) is locally injective in \(s\); the tangent dimension of \(\mathsf{Under}_A=\operatorname{hofib}(G_A)\) is zero.

For the signed probe family

\[
d\rho_\varepsilon=(1+\varepsilon\cos(ax))e^{-x^2}dx,
\]

the coherencer retains the obstruction coordinate \(C_C(\rho_\varepsilon)=\varepsilon\), whose derivative with respect to \(\varepsilon\) is one. Thus \(\mathsf{Over}_C\) has one local obstruction direction.

Any local equivalence \(T_C:\mathsf{Over}_C\simeq\mathsf{Under}_A\) would preserve tangent dimension, but the dimensions are one and zero. The checker verifies this exact Jacobian-rank mismatch.

## Exact residual

The mismatch refutes the unrestricted full conjecture on the present object choices. It does not refute the cyclic signature or the existence of a noninvertible transport \(T_C:R_C\to P_A\). Possible revisions must change a declared type rather than ignore the mismatch: enlarge \(P_A\) so the fiber of \(G_A\) has an obstruction direction, quotient \(R_C\), or weaken equivalence to a noninvertible map. Each revision changes the conjecture and requires its own test.

## Disposition

Rival 1 survives and falsifies the bold conjecture at the first counterclockwise edge. The categorically complete model should therefore retain typed noninvertible residue transports unless a source-derived enlargement or quotient equalizes the fibers. Contractibility of the global coherence fiber is not tested because its prerequisite edge equivalence already fails.

## Verification

- `research/voevodsky/checkers/check_c3_cubical_fiber_equivalence.py`
- `research/voevodsky/results/c3_cubical_fiber_equivalence.json`
