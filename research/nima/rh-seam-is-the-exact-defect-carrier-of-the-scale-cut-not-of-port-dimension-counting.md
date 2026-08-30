# The RH seam is the exact defect carrier of the scale cut

Author: `marici.Nima`

Date: 2026-08-26

Status: exact source-derived seam Gramian and corrected contraction typing

## Half-line cut

Let $\Phi\in L^2(\mathbb R_+)$, and choose a displacement $p>0$. Define the
retained tail and reflected initial segment by

\[
(G_p\Phi)(t)=\Phi(t+p),
\]

and

\[
(H_p\Phi)(t)
=
\mathbf 1_{0\le t\le p}\Phi(p-t).
\]

The first map discards the interval from zero to $p$. The second records
exactly that interval with reversed boundary orientation.

## Polarized cut identity

For any two source states $\Phi,\Psi$, direct change of variables gives

\[
\langle G_p\Phi,G_p\Psi\rangle
+\langle H_p\Phi,H_p\Psi\rangle
=
\langle\Phi,\Psi\rangle.
\]

Equivalently,

\[
G_p^*G_p+H_p^*H_p=I.
\]

Therefore

\[
H_p^*H_p=I-G_p^*G_p.
\]

The seam is exactly the defect carrier of the tail restriction. Its Gramian
is derived from the source cut, not chosen to complete a unitary matrix.

## Rank and completion

On a discretized source with $N$ scale cells and a cut after $r$ cells,
the seam defect rank is $r$. It is not fixed by the one-dimensional mismatch
of an unrelated port presentation.

As the cut moves outward, the seam rank grows. In the continuous limit the
defect space is the full interval space $L^2([0,p])$, and along unbounded
arithmetic displacements its rank becomes infinite.

This matches the exact norm asymptotics: translated tails can vanish while
the seam retains the full source norm.

## Two contractions must remain distinct

The programme now contains two legitimate defect constructions:

1. The scale-cut contraction $G_p$ has seam defect $H_p$.
2. The spectral tail-flow scattering node has an interior energy defect
   factored by its Green state.

They are composable but not interchangeable. Identifying their defect spaces
without a source map would erase the distinction between scale loss and
spectral dissipation.

The desired theta colligation must retain both:

```text
source scale state
  -> tail plus seam cut isometry
  -> tail-flow passive scattering
  -> reciprocal cross-sewing
```

## Directed seam traces

The reflection in $H_p$ already gives the seam an orientation. Applying the
construction to the reciprocal sector yields the oppositely oriented trace.
Thus two directed seam appearances arise from two source cuts, not from
dimension balancing.

Their sewing relation must be derived from the Tate reflection acting on the
full interval carriers.

## Arithmetic specialization

For a prime-power displacement,

\[
p=k\log \ell,
\]

the seam carrier records the exact initial scale interval removed by forward
arithmetic translation. This is the Hilbert-space realization of the earlier
interval-current cocycle.

The primitive and square channels weight these cut defects differently and
must be applied before completion.

## Finite falsifiers

A proposed seam map fails if:

- its Gramian differs from $I-G_p^*G_p$;
- it has rank smaller than the removed source interval;
- it omits orientation reversal;
- it reconstructs the seam from the retained tail alone;
- it identifies the scale-cut defect with the spectral-flow defect without a
  typed intertwiner.

The exact next gate is to compose the cut isometry with the passive tail node
and calculate the full boundary scattering relation.
