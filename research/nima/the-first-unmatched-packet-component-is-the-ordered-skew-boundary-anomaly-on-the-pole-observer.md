# The first unmatched packet component is the ordered skew boundary anomaly on the pole observer

## Question

Which packet coordinate remains first after global continuity of the polarized
Hermitian `C34` readout?

## Component audit

The following components already have compatible constructions:

- wall and jump: Sokhotski principal-value and residue coordinates, sewn to the
  weighted Hadamard endpoint frame;
- endpoint rows: finite-dimensional and source normalized;
- Hermitian relative current: the Tate/reference cross form with diagonal
  logarithmic-derivative symbol;
- regular-source skew transport: the generic Tate--Green connection comparison
  on the ordinary source-generated response graph.

The unresolved component is the ordered skew companion on the singular leg.
For ordered placement `P` and relative projection `Delta Q=Q^T-Q^0`, it is

\[
K_{\rm ord}(h,g)
=
\frac1{2i}
\left\langle h,[P,\Delta Q]g\right\rangle.
\]

On Schwartz observers its boundary value vanishes by the existing
trace-class/Riemann--Lebesgue argument. That proof cannot be applied unchanged
to

\[
g(t)=\frac{a(t)}{t-t_0\pm i0}.
\]

A pole can leave a boundary residue even when the regular oscillatory term
decays.

## Exact residual to compute

The required comparison is the ordered limit

\[
\mathcal A_{\rm skew}(\Phi,u_z)
=
\lim_{L\to\infty}
\frac1{2i}
\left\langle
\Phi,[P_L,Q^T-Q^0]u_z
\right\rangle.
\]

There are two admissible dispositions:

1. the limit is zero, extending regular-source skew vanishing to the polarized
   pole domain;
2. the limit equals a fixed residue row, which must be sewn to the retained
   Wronskian/jump coordinate with its source orientation.

Any other surviving term is an unmatched packet residual and rejects the
proposed interface.

## Disposition

The packet comparison should not yet be compressed to the Hermitian bulk
balance. Its first executable residual is `A_skew`. Computing this ordered
commutator boundary value determines whether the pole extension adds no new
coordinate or exactly supplies the retained Wronskian residue row.