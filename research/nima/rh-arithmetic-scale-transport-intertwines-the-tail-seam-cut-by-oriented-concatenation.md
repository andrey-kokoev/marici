# Arithmetic scale transport intertwines the tail-seam cut by oriented concatenation

Author: `marici.Nima`

Date: 2026-08-26

Status: exact cut-cocycle coherence theorem

## Successive scale cuts

For displacements $p,q>0$, the retained-tail maps satisfy

\[
G_qG_p=G_{p+q}.
\]

The seam of the combined cut is not the sum of two untyped seam vectors. It
is the oriented concatenation of:

1. the interval removed by the second cut from the already translated tail;
2. the interval removed by the first cut.

Explicitly,

\[
H_{p+q}\Phi
=
\left(
H_qG_p\Phi
\right)
\mathbin{\#}
\left(
H_p\Phi
\right),
\]

where the concatenation places the reversed interval of length $q$ before
the reversed interval of length $p$.

## Exact coherence square

The one-step cut and the two-step cut therefore agree as complete typed
objects:

```text
source
  -> tail at p+q plus seam interval [0,p+q]

source
  -> tail at p plus seam interval [0,p]
  -> tail at p+q plus seam intervals [p,p+q] then [0,p]
```

The retained tails are equal, and the ordered seam packets are equal after
the source-authorized concatenation map.

This is the Hilbert-space version of the half-line interval-current cocycle.

## Polarized norm compatibility

The three disjoint pieces partition the source norm:

\[
\langle\Phi,\Psi\rangle
=
\langle G_{p+q}\Phi,G_{p+q}\Psi\rangle
+\langle H_qG_p\Phi,H_qG_p\Psi\rangle
+\langle H_p\Phi,H_p\Psi\rangle.
\]

Thus staged arithmetic translation introduces no supply anomaly at the cut
stage. An apparent anomaly arises only if seam order or one interval carrier
is erased.

## Prime-power specialization

For

\[
p=k\log\ell,
\qquad
q=j\log r,
\]

the theorem gives exact coherence for staged prime-power translation. Unique
factorization types the displacement labels, while oriented seam
concatenation records their ordered boundary incidence.

The scalar equality $p+q=q+p$ does not identify the two staged constructor
trees automatically. Their comparison cell is the interval resegmentation
that preserves each labelled subinterval.

## Consequence for the lossless cascade

The cut component of the source cascade is already functorial under
arithmetic translation. Therefore the next intertwining audit can compare the
direct passive tail-flow action

\[
N_{p+q}G_{p+q}
\]

with the transported staged action

\[
N_qG_qN_pG_p.
\]

The displayed comparison is only a typing target because the spectral-flow
node does not yet have a declared arithmetic action on all its ports.

Any genuine residual must arise from spectral forcing, modular sewing,
archimedean completion, or a failure of the arithmetic action to preserve the
Green defect state.

## Finite falsifiers

The cut coherence fails if:

- the retained tails differ;
- the two seam intervals are concatenated in the wrong orientation;
- a staged interval is omitted;
- scalar displacement equality is used to erase prime-power labels;
- the polarized norm partition fails.

The checker verifies exact vector equality and polarized norm preservation for
multiple finite sources and cut pairs.
