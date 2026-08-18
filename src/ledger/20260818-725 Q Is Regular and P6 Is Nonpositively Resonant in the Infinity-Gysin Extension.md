---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 725 — Q Is Regular and P6 Is Nonpositively Resonant in the Infinity-Gysin Extension

## Frozen question

Entry 724 completed the residue analysis on eight parameterized source
divisors.  The two remaining declared factors are

\[
P_6=0,
\qquad
\mathcal Q=0.
\]

This calculation uses their function fields directly.  No points on either
divisor are sampled or fitted, and no three-divisor Čech comparison is formed.

## Exact function-field method

Serialize the validated bivariate rational connection in the Gysin-adapted
frame.  Regard (P_6) and \(\mathcal Q\) as monic quadratics in (v), and
reduce every numerator and denominator in

\[
\mathbf F_p(u)[v]/(f),
\qquad p=2^{61}-1.
\]

For the (v)-connection, exact divisibility by (f) determines the pole
order.  A simple residue is computed as

\[
R_f=left.\frac{fA_v}{\partial_vf}\right|_{f=0}.
\]

All matrix ranks and indicial polynomials are then computed inside the
quadratic function field itself.

## The (P_6) residue

In the ordered Gysin-adapted basis

\[
(e_6,v_{\rm alg};\widetilde\omega_0,\widetilde\omega_2),
\]

the exact residue is

\[
\boxed{
R_{P_6}=
\begin{pmatrix}
-\frac12&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
}
\]

In particular (R_E=0), so

\[
\operatorname{rank}L_0
=
\operatorname{rank}(L_0\mid-R_E)
=2.
\]

The exact indicial polynomial on
\(\operatorname{Hom}(\mathbb V_{\rm ell},\mathcal A_2)\) is

\[
\boxed{
\det(T-\lambda)=\lambda^2
\left(\lambda+\frac12\right)^2.
}
\]

Hence (P_6) has no positive integral resonance at any pole order.

## The \(\mathcal Q\) restriction

Every entry of the Gysin-adapted connection is regular at generic
\(\mathcal Q=0\).  Therefore

\[
\boxed{R_{\mathcal Q}=0_{4\times4}.}
\]

Consequently

\[
L_0=0,
\qquad
R_E=0,
\qquad
\det(T-\lambda)=\lambda^4.
\]

There is again no positive integral resonance.

This is stronger than the bounded simple-pole census of Entry 722:

\[
\boxed{
\mathcal Q=0
\text{ is not a logarithmic pole of the infinity-Gysin extension.}
}
\]

## Classification

Within the generic rank-four infinity-Gysin differential module:

- (P_6) is ordinary coefficient singular support internal to the algebraic
  kernel and carries no extension residue;
- \(\mathcal Q\) is regular and carries neither diagonal nor off-diagonal
  residue data;
- neither divisor supports a positive-order meromorphic splitting;
- no new carrier datum appears.

This does not prove the full extension globally nonsplit.  It excludes both
remaining declared divisors as local homes of its extension class.  A global
class may still be represented by overlap compatibility among resonant
ordinary divisors or by the physical relative-chain comparison absent from
the rank-four de Rham module.

## Evidence

- Entries 207, 721--724;
- `research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json`;
- `research/benincasa/gysin_function_field_residues.py`;
- `research/benincasa/marici-gm/gysin-function-field-residues.json`;
- allocator claim `seqclaim-cda193ea958844e3b1788bd5`.

## Next boundary

Per the frozen instruction, do not begin the three-divisor Čech calculation in
this entry.  The next admissible task is to predeclare its cover, local
splittings, overlap gauges, and cocycle target before computing compatibility.
