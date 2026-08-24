# Physical-groupoid descent and the reference-port correction

## The gate

Let a physical equivalence groupoid \(G\) act on presentations \(X\). A
quantity \(f:X\to Y\) is a physical observable only when it is constant on
the \(G\)-orbits, equivalently when it descends through

\[
X\longrightarrow X/G.
\]

Invariance under a chart subgroup \(H\subset G\) establishes only descent to
\(X/H\). It does not establish physical descent.

The finite hostile model uses triples and the coordinate observable
\(f(x_0,x_1,x_2)=x_0\). It is invariant under the subgroup fixing the first
coordinate and fails under the full permutation group. This is the minimal
shape of the flavor warning: sparse-chart invariance is not weak-basis
invariance.

## What a reference port actually does

For phases in an additive group \(A\), begin with two independently
rephasable presentations. Under the full action of \(A^2\), the difference

\[
\delta(\alpha_0,\alpha_1)=\alpha_1-\alpha_0
\]

is not invariant. A physical comparison port is additional relational data
that couples the two occurrences and reduces the admissible action to the
diagonal subgroup

\[
A_{\mathrm{diag}}\hookrightarrow A^2.
\]

Only on this enlarged, coupled physical object does \(\delta\) descend. For
\(A=\mathbf Z/5\), exact enumeration shows that \(\delta\) labels every
diagonal orbit uniquely.

Therefore:

\[
\boxed{
\text{a reference port does not reveal a previously physical invariant;
it creates a new relational physical object with a smaller gauge group.}
}
\]

This is stronger than saying that a frame chooses coordinates. The port is
part of the source/preparation and changes which transformations preserve the
experiment.

## Toric correction: logical coordinates also require framing

The two loop probes in the toric pilot are jointly faithful after choosing a
primal/dual homology basis. They are not individually invariant under the
unframed torus mapping-class action. Its mod-two image is

\[
GL(2,\mathbf F_2),
\]

which acts transitively on the three nonzero logical vectors. Exact
enumeration shows:

- the first loop bit is not mapping-class invariant;
- zero versus nonzero logical class is invariant;
- the three nonzero classes form one unframed orbit.

Thus “two loop probes reconstruct the logical class” is a framed theorem.
Without a marked cycle basis, the absolute readout is the orbit structure,
not an ordered pair of bits.

## General criterion

A candidate observable must declare all four objects:

1. presentation space \(X\);
2. physical relational structure \(R\) included in the experiment;
3. automorphism groupoid \(G_R\) preserving \((X,R)\);
4. readout \(f_R\) and its descent through \((X,R)/G_R\).

Changing \(R\) may legitimately change \(G_R\). What is prohibited is
holding the physical experiment fixed while shrinking its gauge group merely
to rescue a desired observable.

## Cross-sector consequences

- Flavor loop phases remain chart data unless a source-derived relational
  preparation reduces the full weak-basis groupoid.
- Berry/open-transport values become physical only with endpoint framing or a
  closed cycle.
- Toric logical coordinates require marked noncontractible cycles; unframed
  topology retains only mapping-class orbits.
- A physical reference covector or Leray cycle is not merely a numerical
  functional. It is part of the relational object whose stabilizer defines
  the admissible quotient.

## Falsifier

For any proposed new port, hold the upstream source fixed and compute its full
automorphism groupoid. If the proposed readout becomes invariant only after
discarding transformations that still preserve the source experiment, the
port is fitted and nonphysical. If the source construction itself supplies
new relational data whose stabilizer is the smaller group, the new observable
is legitimately physical but belongs to the enlarged experiment.

## Verification

- `research/nima/checkers/check_physical_groupoid_descent_gate.py`
- dependency-free invocation:
  `python research/nima/checkers/check_physical_groupoid_descent_gate.py`

