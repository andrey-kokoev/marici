# Two-triplet faithful frame: WP649

WP661 correction: this packet is a tree-level construction. Its mixed vertex
generates the omitted \(|n|^2|m|^2\) counterterm at one loop. WP661 supplies
the minimal support-closed repair; the faithful-frame conclusion survives,
while the unit vacuum normalization and Hessian values below are not
RG-stable.

## Construction

Take two ordered real (SO(3)) triplets with the positive quartic action

\[
V=(|n|^2-1)^2+(|m|^2-1)^2+(n\mathbin\cdot m)^2.
\]

Its zero set consists of ordered orthonormal pairs. At \(n=e_1\), \(m=e_2\),
the exact Hessian spectrum is

\[
0,0,0,4,8,8.
\]

The three zero modes are precisely the broken (SO(3)) orbit; all physical
modes are positive. Any proper rotation fixing both ordered noncollinear
vectors also fixes \(n\mathbin\times m\), hence fixes an oriented basis and is
the identity. The source vacuum therefore has trivial stabilizer.

## Flavor response

The frame authorizes the relative word family

\[
\{I,J_n,J_m\}_{u,d}.
\]

At WP646's exact nondegenerate CP witness, its twelve real controls have exact
intrinsic response rank eight. This improves the one-reference rank six result
and removes the residual frame ambiguity, but it neither separates all ten
physical directions nor selects a proper numerical flavor family. The scalar
sector couplings remain undetermined source data.

## Classification and falsifier

This is a source-generated faithful frame and presentation rigidifier, not a
`physical16` selector. The smallest exact falsifier is a nonidentity proper
rotation fixing both ordered noncollinear triplets.

The next gate is a source action for the sector couplings and messenger
matching, followed by an ensemble-wide test and a detector-typed instrument.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp649_two_triplet_faithful_frame.py
```

Generated result: `results/wp649_two_triplet_faithful_frame.json`.
