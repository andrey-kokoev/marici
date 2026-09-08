---
author: marici.Benincasa
date: 2026-08-25
---

# 2461 — The Fixed Loop-Vector Cycle Faithfully Reads the Complete Interaction Score Tower

## Question

Entry 2460 proves local score independence after moving the
Cayley--Menger boundary in distance coordinates.  Does this survive on the
actual source cycle, without gradient pivots or Čech representatives?

Sequence claim: `seqclaim-68bf7edede6ae644d31884e1`.

## Return to the primary cycle

In the original loop-vector representation the physical cycle is fixed:

\[
\Gamma_\ell=\mathbb R^3.
\]

The Cayley--Menger square-root measure is the Jacobian of the change to loop
distances.  Before that change, the regulated four-wall density is simply

\[
\rho(\ell;\nu)
=
\frac1{
q_{g_1}q_{g_2}q_{g_3}q_{g_{23}}
}.
\]

Choose external vertices

\[
v_2=0,
\qquad
v_3=(P_2,0,0),
\]

\[
v_4=
\left(
\frac{P_1^2+P_2^2-P_3^2}{2P_2},
\sqrt{P_1^2-\left(
\frac{P_1^2+P_2^2-P_3^2}{2P_2}
\right)^2},0
\right),
\]

with

\[
P_i^2=X_i^2+\nu_i.
\]

Then (c=|\ell-v_2|), (a=|\ell-v_3|), and (b=|\ell-v_4|) reproduce the
source-labelled walls exactly.

## Exact finite-field automatic differentiation

The checker expands the physical density in

\[
\mathbb F_p[\nu_1,\nu_2,\nu_3]/(\nu)^4
\]

and extracts the ten normalized responses labelled by

\[
\nu_i,quad \nu_i^2,quad \nu_i\nu_j,quad
\nu_1\nu_2\nu_3.
\]

Square roots are expanded inside the same truncated algebra.  No
distance-space gradient lift, fitted primitive, or numerical derivative is
used.

At twenty-eight accepted loop points in each run, the exact ranks are

\[
\begin{array}{c|c|c|c}
p&(X_1,X_2,X_3)&\operatorname{rank}(R)&
\operatorname{rank}(1,R)\\
\hline
32003&(3,4,5)&10&11\\
32009&(4,13,15)&10&11.
\end{array}
\]

A nonzero determinant modulo either good prime proves that the corresponding
function-field determinant is not identically zero in characteristic zero.
The independent replication excludes a single-prime or single-triangle
accident.

## Regulated physical consequence

On the positive real chamber the ten response functions are analytic.  A
constant linear relation on an open set would be an algebraic identity,
contradicting the exact rank certificate.  Their positive regulated Gram
matrix is therefore nondegenerate.

Since the source interaction quotient has rank seven,

\[
\boxed{
\ker\left(
\mathcal I_{\rm source}^{(7)}
\longrightarrow
\mathcal O_{\rm physical\ score}
\right)=0
}
\]

at generic unequal energies before UV subtraction.

## Result

\[
\boxed{
\text{the complete interaction score tower is physically faithful on the
fixed source loop cycle.}
}
\]

This upgrades Entry 2460 from local moving-boundary representatives to the
actual source cycle.  It also shows that gradient-pivot denominators were
pure coordinate artifacts.

## Remaining analytic qualification

The loop integral is UV divergent and requires a declared subtraction
scheme.  The theorem concerns the regulated physical score Gram form.  A
subtraction can in principle collapse finite covectors; scheme-independent
renormalized faithfulness is not inferred.  Such a collapse would be a
readout/renormalization obstruction, not new Carrier support unless it
produced an independently derived divisor.

## Durable evidence

- `research/benincasa/check_fixed_loop_physical_score_rank.py`;
- `research/benincasa/fixed-loop-physical-score-rank.json`;
- the primary loop-vector and Cayley--Menger measure representations;
- Entries 2424, 2426, and 2460.

## Next falsifier

Apply a source-declared UV regulator and subtraction to the ten physical
score covectors.  Test whether their rank-seven quotient remains faithful in
the finite part.  Separate universal local counterterms from nonlocal
elliptic periods before computing rank.