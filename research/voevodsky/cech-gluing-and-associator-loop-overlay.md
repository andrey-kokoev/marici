# Cech gluing and the associator-loop probe

## Question

How does Kitaev's four-copy associator-loop construction interact with the Alexandrov/Grothendieck model of partial pyramid representations?

## Claim boundary

The ordered Bargmann trace is treated as an exact representation-theoretic probe reported in Kitaev's packet. This packet does not promote the proposed controlled four-copy permutation to a source-authorized physical operation and does not identify every nontrivial loop value with a categorical obstruction.

## Nerve of a representation cover

Let \(U_i\) be certificate opens carrying local pyramid representations \(F_i\). On pairwise overlaps, a gluing attempt requires typed comparison cells

\[
\alpha_{ij}:F_i|_{U_{ij}}\Rightarrow F_j|_{U_{ij}}.
\]

On triple overlaps, two composites must agree. Their residual is the associator defect

\[
\omega_{ijk}
=\alpha_{ik}^{-1}(\alpha_{jk}\circ\alpha_{ij}),
\]

when all terms and inverses are typed. On fourfold overlaps, these defects must satisfy the corresponding tetrahedral/pentagon compatibility. Thus the coherence pyramid can be read as descent data on the nerve of the certificate-open cover:

- vertices are local representations;
- edges are comparison cells;
- triangular faces test associator residuals;
- tetrahedral boundaries test coherence among those residuals.

This is a diagnostic organization, not a claim that the coefficient objects are abelian Cech cohomology classes.

## Kitaev's loop as a face-holonomy probe

Kitaev constructs four rank-one channel projectors and an ordered four-copy cyclic shift whose control expectation is the ordered Bargmann trace. In the frozen electric `D(S3)` representation fragment, the reported exact quadratures are

\[
\langle X\rangle=-\frac18,
\qquad
\langle Y\rangle=0.
\]

The important overlap is structural: the cyclic permutation measures an ordered composite around a coherence loop without replacing it by disconnected pairwise transition probabilities. It is therefore a candidate probe of gluing holonomy on a closed path in the nerve.

A nontrivial trace alone is not an obstruction. It becomes an obstruction test only relative to a preregistered value predicted by the proposed comparison cells, with orientation, normalization, and gauge conventions fixed. Reversing the cycle gives complex conjugation and supplies an orientation check.

## Layered certificate factorization

Kitaev's source audit splits the proposal into independent layers:

1. Carrier geometry supplies four labelled copies, cyclic port order, whole-copy permutation, and ordered-cycle combinatorics.
2. The quantum coefficient lens supplies coherent identity/cycle superposition, control phase and quadratures, fusion-channel projectors, and Bargmann interpretation.
3. A physical constructor must supply controlled permutation, coherent control, preparations, and readout.
4. Fault certification must exclude shared-control common-mode errors that can corrupt multiple route segments while preserving local target preparations.

These are not a linear chain. The geometric loop may be represented while coherent control is absent; the algebraic trace may be exact while physical generation is unauthorized; local preparation checks may pass while shared-control holonomy is corrupted.

## New pyramid insight

The partial-representation registry should distinguish three kinds of coherence evidence:

- `local_cell`: a comparison on one overlap;
- `loop_probe`: an ordered closed composite testing holonomy;
- `global_gluing`: a coherent family satisfying all face and higher compatibility laws.

A loop probe is strictly stronger than disconnected edge probabilities because it retains order and phase. It is strictly weaker than global gluing because it samples one closed composite and can share a correlated control fault.

This creates a useful filtration of representation strength without making it temporal:

\[
\text{local cells}
\;<\;
\text{specified loop probes}
\;<\;
\text{cover-wide coherent gluing}.
\]

The relation is evidential strength, not logical implication: each promotion needs coverage and fault certificates.

## Disposition

Kitaev's four-copy construction supplies the first explicit candidate observable for a nontrivial coherence-loop face in the certificate nerve. Its exact algebraic value belongs in the partial-representation projection as a `loop_probe`; its physical realization remains blocked. The overlay suggests tracking loop coverage and shared-control independence separately from local cell verification.

## Verification

- `research/voevodsky/checkers/check_cech_associator_loop_overlay.py`
- `research/voevodsky/results/cech_associator_loop_overlay.json`
