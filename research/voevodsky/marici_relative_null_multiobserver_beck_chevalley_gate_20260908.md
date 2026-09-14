# Relative-null / multiobserver Beck–Chevalley gate

Date: 2026-09-08

## Proposed constraint

Let `F` denote global Fourier–Poisson sewing, `P_X` a finite diagnostic projection, and `Fib(xi)` the relative-null object. The proposed compatibility asks observer formation to commute, coherently, with passage to the scalar zero fiber.

This cannot be tested by identifying the finite six-port object with the completed source. The relevant finite Beck–Chevalley residual is

\[
\mathfrak A_X=P_XF(1-P_X).
\]

## Exact finite result

The existing four-mode exact model gives

\[
\mathfrak A_X=
\begin{pmatrix}
0&0&1&1\\
0&0&-1&-1
\end{pmatrix},
\qquad \operatorname{rank}\mathfrak A_X=1.
\]

Therefore the finite square does not commute. This was rerun from

`research/nima/checkers/check_no_finite_completed_source_intertwiner.py`.

The failure is precisely an omitted Fourier-tail direction. Adding the six normal ports after projection can diagnose its image but cannot make the pre-sewing finite square Cartesian.

## Correct order

The viable comparison is

\[
\text{global restricted-product theta source}
\xrightarrow{F}
\text{completed rigged boundary correspondence}
\xrightarrow{\operatorname{Obs}}
\text{multiobserver node}
\xrightarrow{P_X}
\text{finite six-normal diagnostics}.
\]

Passage to the relative-null fiber must occur at the completed rigged-boundary level. Only afterward may one project to the finite normal family. In categorical terms, the desired global comparison is

\[
\operatorname{Obs}_{\infty}(\operatorname{Fib}(\xi))
\longrightarrow
\operatorname{Fib}(\operatorname{Obs}_{\infty}(\xi)),
\]

with a specified leakage/continuation cell whose finite projections reproduce `A_X`. Requiring strict finite Beck–Chevalley would contradict the exact rank-one witness.

## Relation to the boundary-work defect

The conjectural global mate should map the completed leakage/continuation class to the dynamic boundary-work class

\[
D_{\mathrm{bw}}=J_0(q_1)-J_0(q_0)+2R.
\]

RH-strength exactness is not that every finite leakage vanishes. It is that, on the completed source-admissible relative-null object, the total continuation class has zero boundary-work image while retaining positive bulk.

## Status

- Finite strict Beck–Chevalley: **falsified**, residual rank one.
- Ordering of global sewing before diagnostics: **proved necessary**.
- Completed relative-null/multiobserver comparison cell: **not yet constructed**.
- Identification of its boundary with `D_bw`: **not yet constructed**.

This sharpens the missing constraint: it is a completion-level lax Beck–Chevalley cell, not a finite Cartesian square.
