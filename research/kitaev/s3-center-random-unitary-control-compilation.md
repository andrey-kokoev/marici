# Finite random-unitary compilation of the `D(S_3)` center quotient

Owner: `marici.Kitaev`

## Bounded question

Does the previously constructed center expectation admit a finite compilation
from random unitary channels, and what exact control surface would that
compilation require?

## Compilation

Label the eight simple sectors by `F_2^3`.  The eight Walsh characters define
block-sign unitaries

\[
U_k=\sum_a(-1)^{k\cdot a}P_a,
\qquad k\in\mathbf F_2^3.
\]

Character orthogonality makes their uniform twirl exactly the sector
dephasing channel.  Its orthogonality residual has rank zero.

For each nontrivial block `V_a` of dimension `d_a`, apply the uniform
generalized-Pauli twirl

\[
X\longmapsto\frac1{d_a^2}\sum_{p,q=0}^{d_a-1}
W_{pq}XW_{pq}^{\dagger}=\frac{\operatorname{Tr}X}{d_a}I.
\]

Composing the Walsh stage with the six nontrivial block stages gives exactly
the center expectation.  The compilation has seven sequential randomized
stages and 42 branch choices across those stages: eight Walsh choices, four
choices for each of four two-dimensional blocks, and nine choices for each of
two three-dimensional blocks.  Flattening all choices produces an ensemble
of 165888 unitaries.

The checker verifies the one-, two-, and three-dimensional Weyl identities on
every local matrix unit.  Together with Walsh orthogonality, these cover all
256 global matrix units: 36 within-block and 220 cross-block.

## Deliberate failure and repaired checker defect

Sector dephasing alone still fails on the traceless `C`-block witness, now
with residual rank two.  The first checker run also exposed a verification
defect: unevaluated exponential cubic roots of unity did not simplify to zero
under exact comparison.  The checker now freezes the algebraic root
`-1/2+i sqrt(3)/2`; the unweakened identity then passes.

## Typing boundary

This is a finite compilation theorem, not an availability theorem.  It
requires controlled sector-sign unitaries, independently randomized Weyl
controls inside every nontrivial simple block, and classical randomness.
Nothing in the frozen `D(S_3)` Hamiltonian has yet been shown to supply those
controls.  The result turns the apparatus blocker into a concrete control
inventory rather than dissolving it.

The Walsh support and finite twirl construction are reusable Carrier-level
control geometry.  The block decomposition, dimensions, and interpretation
of the controls as anyonic internal operations require the quantum
coefficient lens.

## Falsifiers and verification

Falsifiers are nonunitarity of any Weyl generator, nonzero Walsh
orthogonality residual, failure on a local matrix unit, or disagreement with
the center expectation on either basis partition.

Run:

```text
uv run --with sympy python -u research/kitaev/checkers/check_s3_center_random_unitary_compilation.py
```

Seven aggregate gates pass.  Post-objective excitement 9/10, confidence
10/10, realized information gain 9/10.  The abstract-channel branch is now a
finite control compilation; source availability remains the sole live typing
branch.
