# The First Irreducible Five-Point Residue Is Eta Squared

## Target

Identify the first nonzero homotopy residue after the fillable nested
commutator has been removed.

## Homotopy class

The five-point spherical Brunnian quotient is

\[
\pi_4(S^2)\cong\mathbb Z/2.
\]

Its nonzero element is the secondary Hopf composite

\[
\eta^2=\eta\circ\Sigma\eta,
\]

where \(\eta:S^3\to S^2\) is the Hopf map and
\(\Sigma\eta:S^4\to S^3\) is its suspension. It satisfies

\[
\eta^2\ne0,
\qquad
2\eta^2=0.
\]

## Consequence for the braid compiler

The surjection

\[
\operatorname{Brun}_5(S^2)\longrightarrow\pi_4(S^2)
\]

guarantees that some five-strand spherical Brunnian braid represents
\(\eta^2\). Therefore a genuine unfillable five-point residue exists.

However, existence of a preimage does not provide an explicit braid word.
The nested commutator \(\beta_5\) from the previous packet lies in the kernel
and must not be reused as the lift.

## Structural advance

The first post-four-point coherence cell is not a higher commutator. It is a
secondary composition operation:

```text
Hopf class
   + suspension constructor
   + composition
   = binary five-point residue
```

This is the first evidence that higher arity is governed by operations on
lower coherence classes, not only by new independent generators.

## Remaining exact task

Compile a specific braid word

\[
\widehat{\eta^2}\in\operatorname{Brun}_5(S^2)
\]

and verify both:

1. every strand deletion is trivial;
2. its quotient class is the nonzero element of \(\mathbb Z/2\).

Until that lift is constructed, existence is theorem-level but the braid
realization is not executable.

## Verification

```powershell
uv run python research/strominger/checkers/five_point_eta_squared_residue_contract_checks.py
```
