# DAG/crystal boundary search disposition

Date: 2026-09-08

## Question

Can the Stacks and DAG localization machinery construct a source-derived RH boundary-work map rather than merely host one after RH-equivalent support has been assumed?

## Surviving construction

The correct speculative base is the realification

\[
X=\operatorname{Spec}\mathbb R[x,y],
\qquad s-\frac12=x+iy,
\]

with reciprocal involution `(x,y)↦(-x,y)` and fixed seam `Z=V(x)`.  The boundary work

\[
D_{\mathrm{bw}}=-2xB
\]

is a first-order conormal section along `Z`.

Because the packet carries differential equations and Fourier transport, its closest DAG type is a crystal

\[
F_\theta\in\operatorname{Crys}(X)=\operatorname{IndCoh}(X_{\mathrm{dR}}).
\]

If the completed comparison fibre

\[
B_{\mathrm{rel}}(F_\theta)
=
\operatorname{fib}(F_\theta\to j_{\mathrm{dR},*}j^!_{\mathrm{dR}}F_\theta)
\]

is supported on `Z`, Kashiwara localization gives a canonical boundary crystal.  This construction sends zero to zero before scalar readout.

## Rejected shortcuts

1. The critical seam is not closed on the complex algebraic parameter line.
2. Reciprocal equivariance does not confine zeros to the seam.
3. Hard finite Fourier-cutoff leakage has generic rank one and is not seam-supported.
4. Fixed-observer cutoff convergence does not imply uniform strictification.
5. A raw endpoint Gram cannot be identified with the constant normalized three-port metric.
6. Summing the Pauli outputs deletes real correlation and reciprocal orientation.
7. Positive square-root Gram congruence does not preserve the source wall/odd frame.
8. The apparent endpoint `h_Pauli` is rephasing-dependent and supplies no invariant orientation baseline.
9. The resulting Euler-minus-Pauli rank-one Schur residual model is therefore superseded.

## Analytic completion status

The renormalized primitive--square Adams block has weight

\[
\frac12p^{-3/2-\sigma}
\]

and is absolutely Green-summable through the seam.  Its all-grade odd coordinate decomposes exactly as

\[
\frac{Lr}{1-r}=Lr+Lr^2+\frac{Lr^3}{1-r},
\qquad r=p^{-1/2},
\]

with an absolutely summable connected tail.  This closes existence of the mixed scalar and labelled completion, conditional on the established packet-growth estimates.  It does not prove support or quadratic representation.

## Exact finite target

The relative three-port quotient coordinate is

\[
\Pi(a,b,c)=(a-c,b-c).
\]

The reciprocal-even metric is fixed by the wall and odd norms.  The source Euler odd current supplies the remaining imaginary coordinate

\[
H_{p,K}=
\begin{pmatrix}
2&ih_{p,K}\\
-ih_{p,K}&2
\end{pmatrix},
\qquad
h_{p,K}=(\log p)\sum_{k=1}^Kp^{-k/2}.
\]

For every finite `K` and at completion its eigenvalues are `2±h`, both positive.

The endpoint comparison must retain the full Pauli linking Gram

\[
\Gamma_{\mathrm P}(G)
=
\begin{pmatrix}
XGX&XGY\\
YGX&YGY
\end{pmatrix}.
\]

This lift is positive and faithful, with explicit retraction `G=X Gamma_P(G)_{XX} X`.  Its summed frame is useful for uniform observability but cannot replace the four blocks.

## First missing theorem

Let `G_p^St` be the polarized Stieltjes endpoint form and let `Gamma_theta,p` be the completed wall/odd/tail representation produced by the fixed linear Adams constructor.  The next theorem is exactly

\[
\Gamma_{\mathrm P}(G_p^{\mathrm{St}})
=
\Gamma_{\theta,p}
\]

on the common rapid, wall-reduced core, together with closability and cutoff naturality.

This equality must be proved blockwise.  It is equivalent to all four endpoint matrix-unit identities and cannot be inferred from scalar agreement, positivity, frame bounds, equal dimensions, or DAG functoriality.

## Disposition

The speculative DAG search succeeds as a typing and localization architecture but does not produce the missing RH boundary map.  It isolates one nonredundant source theorem: the faithful four-block Pauli/Adams quadratic representation followed by proof that the completed comparison fibre restricts to zero on `X\setminus Z`.  Further manipulation of localization triangles before those inputs would restate the missing theorem rather than advance it.

## Verification set

- `check_marici_rh_realified_seam_conormal_20260908.py`
- `check_marici_rh_realified_localization_hostile_20260908.py`
- `check_marici_rh_finite_cutoff_seam_support_hostile_20260908.py`
- `check_marici_rh_three_port_oriented_hermitian_extension_20260908.py`
- `check_marici_rh_euler_odd_connected_tail_decomposition_20260908.py`
- `check_marici_rh_full_pauli_linking_gram_faithful_20260908.py`
- `check_marici_rh_pauli_quadratic_lift_20260908.py`
- `check_marici_rh_pauli_sum_false_positive_20260908.py`
