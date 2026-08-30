# 2361 — The Soft Residue Port Faithfully Recovers the Rank-Four Quotient

## Question

Entry 2360 derives the exact sequence

\[
0\longrightarrow M_{16}^{\rm deleted}
\longrightarrow M_{20}^{X_1\text{-soft}}
\longrightarrow Q_4
\longrightarrow0.
\]

Does the source-admitted \(g_{23}\) residue port recover \(Q_4\), or is an
additional observer required?

## Residue map

At \(X_1=0\), the wall equation is \(q_{g_{23}}=b\).  In the ordered
simple-pole frame,

\[
\operatorname{Res}_{b=0}
\frac{P(a,b)\,da\wedge db}
{b\prod_{r\ne g_{23}}q_r}
=
\frac{P(a,0)\,da}
{\prod_{r\ne g_{23}}q_r|_{b=0}}.
\]

This is fixed by Poincare residue; no projector is fitted.

## Exact result

Reduction modulo the deletion image gives quotient pivots

\[
a^3,\qquad a^2,\qquad a,\qquad1.
\]

The quotient has rank four, and their residue polynomials also have rank
four.  Reducing those symbols in the independently constructed
one-dimensional twisted de Rham complex on \(b=0\)—with

\[
K|_{b=0}=-1024(a^2-125)
\]

and retained walls \(a-5,a+5,a-3\)—still gives rank four:

\[
\boxed{
\operatorname{rank}Q_4
=
\operatorname{rank}_{H^1(W_{g_{23}})}\operatorname{Res}_{b=0}(Q_4)
=4.
}
\]

Every term lies in the declared simple-pole frame; the unsupported-term
count is zero.  Consequently

\[
\boxed{
\ker\left(
\operatorname{Res}_{b=0}:M_{20}^{X_1\text{-soft}}\to R_4
\right)
=M_{16}^{\rm deleted}.
}

Thus the algebraic observer sequence is exact:

\[
0\longrightarrow M_{16}^{\rm deleted}
\longrightarrow M_{20}^{X_1\text{-soft}}
\xrightarrow{\operatorname{Res}_{b=0}}
R_4
\longrightarrow0.
\]

## Contextual-faithfulness consequence

The supported rank-four quotient is completely visible to an already
admitted marked-residue port.  The only remaining physical-faithfulness gate
is the deleted bulk:

\[
\lambda_{\rm BD}|_{M_{16}^{\rm deleted}}\stackrel?\ne0.
\]

No additional score, polarization port, or Carrier cell is needed to recover
the quotient.

## Scope

This is a finite-field de Rham/localization theorem.  It does not prove that
the physical soft limiting cycle pairs nontrivially with the deletion image,
nor does it construct nearby cycles.

## Artifacts

- `research/benincasa/check_x1_soft_residue_quotient_port.py`
- `research/benincasa/x1-soft-residue-quotient-port.json`

Sequence claim: `seqclaim-61dda23843054e06a1e17401`.
