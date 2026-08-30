# All remaining zero information is in the boundary Schur complement

## Question

Once the connected channel has an exact zero-free Schatten-three coefficient
lift, where can a zero of the completed determinant still enter?

Not through the regularized prime bulk or the first two cumulant frames.  It
must enter through the operator-valued boundary coupling.

## Zero-blind low-order frames

For an `S_3` operator `K`,

\[
\det(I-K)
=
\det_3(I-K)
\exp\left(-\operatorname{Tr}K-\frac12\operatorname{Tr}K^2\right)
\]

at finite rank, with the low-order terms retained as typed relative boundary
data in the completed setting.

Every well-defined exponential factor is a holomorphic unit.  It changes the
determinant frame and multiplicative anomaly but cannot create, remove, or
move zeros.

Therefore the primitive and square channels are essential for exact source
reconstruction while being divisor-blind by themselves.

## Zero-free connected bulk

For

\[
K_s=\operatorname{diag}_p(p^{-s}),
\]

the operator `I-K_s` is uniformly invertible on compact subsets of
`Re s>0`, and its connected determinant

\[
C_+(s)=\det_3(I-K_s)^{-1}
\]

is zero-free for `Re s>1/3`.  The reciprocal statement holds for `K_s^-` in
`Re s<2/3`.

Thus neither sector's uncoupled connected bulk carries a zero in their common
band around the critical seam.

## Boundary colligation

Write a completed sector or sewn system schematically as

\[
\mathcal M_s=
\begin{pmatrix}
I-K_s&B_s\\
C_s&D_s
\end{pmatrix},
\]

where the boundary block retains primitive, square, seam, archimedean,
forcing, and endpoint coordinates.  Because `I-K_s` is invertible, block
elimination reduces invertibility of `M_s` to the Schur complement

\[
S_s
=
D_s-C_s(I-K_s)^{-1}B_s.
\]

After the regularized determinant and its typed exponential anomaly are
handled correctly, the divisor factorizes into:

```text
zero-free connected bulk unit
  times zero-free P/Q frame unit
  times determinant of the boundary Schur complement.
```

Hence every remaining off-seam zero is a boundary closed-loop failure:

\[
\ker S_s\ne0.
\]

## Architectural consequence

The three-by-two packet remains necessary for typing and exact reconstruction,
but its zero-bearing content is concentrated at the final sewing operation.
The first four levels construct an invertible open bulk and its relative
frame.  The fifth-level boundary feedback determines whether a closed-loop
kernel appears.

This explains why local Euler coherence and arbitrarily many finite prime
certificates could not settle the problem.  They control `I-K_s` and its
cumulants, while the global scalar zero belongs to `S_s`.

## Updated DPC

The DPC should no longer ask the `P/Q/C` packet itself to exclude zeros.  Its
load-bearing claim is:

> The source-derived boundary colligation has a Schur complement that is
> invertible in each open reciprocal sector, with the inverse stable under
> restricted-product completion.

An explanatory proof must derive this from boundary energy balance,
collocation, small gain, a contracting homotopy, or another source law before
the completed scalar determinant is formed.

## Why scalar exponentiation is insufficient

Constructing scalar regularized factors from `P` and `Q` can complete the
determinant frame.  It cannot prove invertibility of `S_s`.  Likewise an exact
multiplicative anomaly cocycle governs composition but carries no divisor
information because it exponentiates finite trace polynomials.

The missing boundary augmentation must therefore be operator-valued.  A map
only into a scalar determinant line is too compressed to control the remaining
kernel.

## Minimal finite falsifier

Take an invertible scalar bulk `A=1` and one-dimensional boundary ports.  Then

\[
\mathcal M=
\begin{pmatrix}
1&b\\
c&d
\end{pmatrix},
\qquad
S=d-cb.
\]

The bulk is perfectly invertible and all nonzero exponential frames remain
harmless, yet choosing `d=cb` makes the full determinant vanish.  No theorem
about the bulk determinant can reject this closed-loop cancellation.

This is the smallest exact hostile model of the remaining mechanism.

## Required source data

To make the Schur complement theorem concrete, the source must provide:

- the boundary state space and its sector-dependent metric;
- `B_s` and `C_s` as typed forward and rigged-transpose incidences;
- `D_s` including seam and archimedean self-action;
- finite cutoff naturality of all blocks;
- an admitted operator ideal for the seam compression;
- a strict sector law implying `S_s` is invertible;
- compact-open or graph-resolvent stability of `S_s^-1`.

The scalar completed section must then be identified with the regularized
determinant of `M_s`, not used to define these blocks.

## Falsifiers

- A nonzero vector in `ker S_s` at any finite source cutoff.
- Boundary blocks reconstructed from the completed scalar ratio.
- A scalar `P/Q` completion presented as a kernel-exclusion theorem.
- Full-rank finite Schur complements whose inverse margins collapse in the
  limit.
- A source seam compression that remains non-Fredholm.
- Positive open-loop bulk with an uncontrolled cross-port feedback product.
- A determinant identity that holds only after dropping typed boundary modes.

## Verdict

The prime coefficient problem has separated cleanly from the remaining zero
problem.  The connected `S_3` bulk and the `P/Q` regularization frames are
already zero-free in their natural domains.  All unresolved divisor
information is carried by the operator-valued seam/archimedean Schur
complement.

The highest-information next move is to construct the smallest source-derived
boundary block `D_s-C_s(I-K_s)^-1B_s` and attack its sector invertibility
directly.
