# The Jacobi--Pade phase bypasses the raw Euler boundary

For every certified finite corner, define

\[
 Q_n(h)=\det(I+hJ_n).
\]

The tridiagonal determinant obeys the source-derived recurrence

\[
 Q_{k+1}(h)=(1+a_kh)Q_k(h)-b_kh^2Q_{k-1}(h).
\]

Because `J_n` is real symmetric and positive, all zeros of `Q_n` are real
negative and equal `-1/u_j`. The boundary phase

\[
 \delta_n(h)=\arg Q_n(h+i0)
\]

is canonical: it jumps by exactly `pi` at each Pade pole. This is a genuine
finite Sommerfeld quantization condition with no branch choice imported from
`arg zeta` and no raw Euler sum on the critical line.

At size five the determinant recurrence reproduces all five blind Pade poles
with numerical relative residual below `2e-11`. Its closest pole produces the
certified first-edge estimate discussed previously.

## Explanatory consequence

Prime information reaches this phase indirectly but legitimately: completed
eta/gamma source jets at the regular point determine moments; positivity turns
moments into Jacobi coefficients; the self-adjoint determinant supplies the
phase jumps. Thus the finite construction crosses the Euler Abel obstruction
through a regular resolvent rather than by assigning meaning to a divergent
critical-line prime phase.

The infinite problem is now sharply localized. Prove that the finite Weyl
functions and phases converge to a canonical self-adjoint limit and that its
source resolvent is the completed Xi resolvent. Without this convergence, the
bypass remains finite.

On the safe positive axis, compatible positive Jacobi extensions already give
monotone bounded resolvents `R_n(h)↑R(h)` by Schur-complement order. This
supplies pointwise infinite-limit existence before any negative-axis phase is
taken. See `jacobi-positive-axis-monotone-resolvent-theorem.md`.

## Scope

This constructs a canonical finite phase. It does not prove convergence of
`J_n`, identify the infinite phase with the Euler boundary, or prove RH.

## Durable verification

- Checker: `checkers/jacobi_pade_phase_bypass.py`
- Result: `results/jacobi-pade-phase-bypass.json`
