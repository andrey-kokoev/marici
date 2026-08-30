# Bell-reference readout has an unavoidable common-mode Pauli kernel

Owner: `marici.Kitaev`

## Bounded question

If the logical Bell reference can itself fault, which Pauli errors remain
invisible, and can additional untrusted replicas recover an absolute Pauli
frame?

## Relational syndrome map

Let each of \(n\) matched logical blocks carry a Pauli label

\[
e_i\in\mathbf F_2^{2k}.
\]

A Bell comparison on an edge \((i,j)\) returns the relative label

\[
s_{ij}=e_i+e_j.
\]

For a comparison graph \(G\), the complete syndrome map is

\[
S_G=B_G\otimes I_{2k},
\]

where \(B_G\) is the mod-two graph incidence matrix.

If \(G\) has \(c\) connected components, then

\[
\operatorname{rank}S_G=(n-c)2k,
\qquad
\dim\ker S_G=c\,2k.
\]

For a connected comparison network, the kernel is exactly the diagonal
common-mode action

\[
(e,e,\ldots,e).
\]

Thus applying the same logical Pauli to data and every reference leaves all
relative Bell records unchanged.

## More replicas do not create an absolute frame

Adding untrusted blocks and all pairwise comparisons increases relative
redundancy but leaves the diagonal \(2k\)-dimensional kernel. This is a gauge
symmetry of relational readout, not a shortage of graph edges. A spanning tree
already achieves the maximal relational rank \((n-1)2k\); cycle comparisons
are consistency checks only.

An absolute Pauli label requires one of:

- a trusted anchor block with frozen label \(e_0=0\);
- an independently derived absolute logical effect not invariant under the
  diagonal Pauli action;
- a preparation-and-timing guarantee that faults occur only on the designated
  data block after Bell-reference certification.

With a trusted anchor, deleting its fixed coordinates from the domain makes a
connected anchored comparison tree injective on the remaining labels.

## Sparse-fault correction is conditional

With at least three blocks and a promise that at most one block suffers a
Pauli fault, relative comparison patterns can identify the outlier and support
majority-style correction. That conclusion uses the one-fault promise. It
does not remove the common-mode kernel from the unrestricted error module.

Common-mode faults, correlated preparation faults, and faults occurring before
the trusted timing boundary remain invisible.

## Mixed-boundary implication

The invisible common mode includes every handle, boundary-loop, and relative
arc Pauli coordinate. Replicating arc ports makes relative arc faults
detectable, but no number of unanchored replicas chooses which block carries
the absolute arc error. The boundary frame and reference trust are separate
resources.

## Pair-of-pants witness

For the one-qubit mixed pair of pants, data and reference each have a rough
arc and a dual rough-loop coordinate. Equal arc faults on both halves and equal
loop faults on both halves produce zero Bell syndrome. A third untrusted block
adds comparisons but preserves the two-dimensional diagonal Pauli kernel.

## Falsifiers

- a connected comparison graph with kernel dimension other than \(2k\);
- a cycle edge claimed to increase relational rank above \((n-1)2k\);
- common-mode Pauli action producing a nonzero relative syndrome;
- anchored restriction failing to be injective;
- one-fault correction asserted without a sparsity/timing promise;
- replication claimed to construct an absolute frame from relational data.

## Disposition

Bell-reference readout is maximally faithful only on the quotient by diagonal
Pauli action. A trusted anchor or equivalent absolute source effect is necessary
for data-versus-reference fault attribution. Replication supplies consistency
and conditional correction, not absolute orientation.

## Claim strength

Exact finite graph-incidence and stabilizer-reference theorem.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_reference_kernel.py`.
The result is written to
`research/kitaev/results/mixed-boundary-reference-kernel.json`.

